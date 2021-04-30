#
# This file is part of pipelined.
#
# pipelined is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pipelined is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pipelined.  If not, see <http://www.gnu.org/licenses/>.

"""Constants and status codes used by pipelined"""

# pylint: disable=too-few-public-methods


class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2
    InvalidControlIP = 10
    ReferenceFrameError = 31
    DirectoryNotWritable = 50
    NewDirectoryFailed = 51

    _messages = {
        # General error codes
        1: 'error: command failed',
        2: 'error: another command is already running',
        10: 'error: command not accepted from this IP',
        50: 'error: directory doesn\'t exist or isn\'t writable',
        51: 'error: failed to create night directory (already exists?)',

        -101: 'error: unable to communicate with pipeline daemon',
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return 'error: Unknown error code {}'.format(error_code)
