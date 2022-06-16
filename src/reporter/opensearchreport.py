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
import click

# import YAML module
from yaml import load
try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import Loader


class OpenSearchReporter:
    def __init__(self, environment):
        self.environment = copy.deepcopy(environment)

        if self.environment['opensearch_port'] is None:
            self.environment['opensearch_port'] = 9200
        else:
            if not isinstance(self.environment['opensearch_port'], int):
                self.environment['opensearch_port'] = 9200

        if self.environment['opensearch_host'] is None:
            self.environment['opensearch_host'] = 'localhost'

        if self.environment['opensearch_index'] is None:
            self.environment['opensearch_index'] = ''

        if self.environment['opensearch_user'] is None:
            self.environment['opensearch_user'] = ''

        if self.environment['opensearch_password'] is None:
            self.environment['opensearch_password'] = ''

        # Create the client with SSL/TLS enabled, but hostname verification disabled.
        self.client = opensearchpy.OpenSearch(
            hosts = [{'host': host, 'port': port}],
            http_compress = True, # enables gzip compression for request bodies
            http_auth = auth,
            # client_cert = client_cert_path,
            # client_key = client_key_path,
            use_ssl = False,
            verify_certs = False,
            ssl_assert_hostname = False,
            ssl_show_warn = False
        )

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

@click.command(short_help='load results into OpenSearch')
@click.option('--config-file', '-c', required=True, help='configuration file', type=click.File('r'))
def main(config_file):
    # read the configuration file. This is in YAML format
    try:
        environment = load(config_file, Loader=Loader)
    except:
        print("Cannot open configuration file, exiting", file=sys.stderr)
        sys.exit(1)
    # some sanity checks:
    if 'config' not in config:
        print("Invalid configuration file, exiting", file=sys.stderr)
        sys.exit(1)

    # create an OpenSearch reporter object
    reporter = OpenSearchReporter(environment)

if __name__ == "__main__":
    main()
