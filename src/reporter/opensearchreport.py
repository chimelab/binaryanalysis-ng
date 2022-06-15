# Binary Analysis Next Generation (BANG!)
#
# This file is part of BANG.
#
# BANG is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License,
# version 3, as published by the Free Software Foundation.
#
# BANG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License, version 3, along with BANG.  If not, see
# <http://www.gnu.org/licenses/>
#
# Copyright 2019-2022 - Armijn Hemel
# Licensed under the terms of the GNU Affero General Public License
# version 3
# SPDX-License-Identifier: AGPL-3.0-only

'''
Write results to an instance of OpenSearch.
'''

import copy
import opensearchpy


class OpenSearchReporter:
    def __init__(self, environment):
        self.environment = environment

    def report(self, scanresult):
        '''Put results into OpenSearch'''
        # copy scanresult because json cannot serialize datetime objects by itself
        result = copy.deepcopy(scanresult)

        # pretty print datetime formats first before serializing
        result['session']['start'] = result['session']['start'].isoformat()
        result['session']['stop'] = result['session']['stop'].isoformat()

        # store the scan uuid in URN (RFC 4122) form
        result['session']['uuid'] = result['session']['uuid'].urn

        uuid = result['session']['uuid']

        # first create the OpenSearch connection string. TODO: sanitize
        connectionstring = 'http://%s:%s@%s:%d/'

        if self.environment['opensearch_port'] is None:
            opensearch_port = 9200
        else:
            opensearch_port = self.environment['opensearch_port']

        if self.environment['opensearch_host'] is None:
            opensearch_host = 'localhost'
        else:
            opensearch_host = self.environment['opensearch_host']

        if self.environment['opensearch_index'] is None:
            opensearch_index = ''
        else:
            opensearch_index = self.environment['opensearch_index']

        if self.environment['opensearch_user'] is None:
            opensearch_user = ''
        else:
            opensearch_user = self.environment['opensearch_user']

        if self.environment['opensearch_password'] is None:
            opensearch_password = ''
        else:
            opensearch_password = self.environment['opensearch_password']

        connectionstring = connectionstring % (opensearch_user, opensearch_password, opensearch_host, opensearch_port)

        es = elasticsearch.OpenSearch([connectionstring])

        # store some information about the session
        es.index(index=opensearch_index, doc_type='_doc', body=result['session'])

        # store information about the individual nodes.
        # TODO: use the bulk interface for this
        for scannode in result['scantree']:
            scannode_res = result['scantree'][scannode]
            scannode_res['uuid'] = uuid
            es.index(index=opensearch_index, doc_type='_doc', body=scannode_res)

    def update(self, scanresult):
        pass
