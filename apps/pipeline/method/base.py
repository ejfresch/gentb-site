#
# Copyright (C) 2017 Maha Farhat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
The base functions for a pipeline method manager.
"""

import os
import tempfile
import atexit

class ManagerBase(object):
    def __init__(self, pipedir=None):
        if pipedir is None:
            self.pipedir = tempfile.mkdtemp(prefix='pipeline-')
            atexit.register(self.clean_up)
        else:
            self.pipedir = pipedir

    def job_fn(self, job_id, ext='pid'):
        """Return the filename of the given job_id and type"""
        return os.path.join(self.pipedir, job_id + '.' + ext)

    @property
    def name(self):
        return type(self).__module__.split('.')[-1]
