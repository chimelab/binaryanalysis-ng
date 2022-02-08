# Binary Analysis Next Generation (BANG!)
#
# This file is part of BANG.
#
# BANG is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
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
# Copyright Armijn Hemel
# Licensed under the terms of the GNU Affero General Public License
# version 3
# SPDX-License-Identifier: AGPL-3.0-only


import os
import pathlib
import stat
import tarfile

from UnpackParser import UnpackParser, WrappedUnpackParser
from UnpackParserException import UnpackParserException
from FileResult import FileResult
from bangunpack import unpack_tar

'''
class wTarUnpackParser(WrappedUnpackParser):
    extensions = ['.tar']
    signatures = [
        (0x101, b'ustar\x00'),
        (0x101, b'ustar\x20\x20\x00')
    ]
    pretty_name = 'tar'

    def unpack_function(self, fileresult, scan_environment, offset, unpack_dir):
        return unpack_tar(fileresult, scan_environment, offset, unpack_dir)
'''


class TarUnpackParser(UnpackParser):
    extensions = ['.tar']
    extensions = []
    signatures = [
        (0x101, b'ustar\x00'),
        (0x101, b'ustar\x20\x20\x00')
    ]
    pretty_name = 'tar'

    def parse(self):
        try:
            self.unpacktar = tarfile.open(fileobj=self.infile, mode='r')
        except tarfile.TarError as e:
            raise UnpackParserException(e.args)
        try:
            self.tarinfos = self.unpacktar.getmembers()
        except tarfile.TarError as e:
            raise UnpackParserException(e.args)

        tar_filenames = set()
        for tarinfo in self.tarinfos:
            file_path = pathlib.Path(tarinfo.name)
            if file_path.is_absolute():
                tarinfo.name = file_path.relative_to('/')

            # TODO: rename files properly with minimum chance of clashes
            if tarinfo.name in tar_filenames:
                pass
            tar_filenames.add(tarinfo.name)


    def unpack(self):
        unpacked_files = []
        for tarinfo in self.tarinfos:
            out_labels = []
            file_path = pathlib.Path(tarinfo.name)
            outfile_rel = self.rel_unpack_dir / file_path
            outfile_full = self.scan_environment.unpack_path(outfile_rel)
            os.makedirs(outfile_full.parent, exist_ok=True)

            if tarinfo.issym():
                out_labels.append('symbolic link')
            elif tarinfo.islnk():
                out_labels.append('hardlink')
            elif tarinfo.isdir():
                out_labels.append('directory')

            if tarinfo.isfile() or tarinfo.issym() or tarinfo.isdir() or tarinfo.islnk():
                self.unpacktar.extract(tarinfo, path=self.rel_unpack_dir)

                # tar can change permissions after unpacking, so change
                # them back to something a bit more sensible
                if tarinfo.isfile() or tarinfo.isdir():
                    outfile_full.chmod(stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
                fr = FileResult(self.fileresult, self.rel_unpack_dir / file_path, set(out_labels))
                unpacked_files.append(fr)
            else:
                # block/device characters, sockets, etc. TODO
                pass

        return unpacked_files

    # no need to carve from the file
    def carve(self):
        pass

    def set_metadata_and_labels(self):
        """sets metadata and labels for the unpackresults"""
        labels = ['tar', 'archive']
        metadata = {}

        self.unpack_results.set_labels(labels)
        self.unpack_results.set_metadata(metadata)
