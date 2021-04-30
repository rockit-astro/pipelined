#
# This file is part of pipelined
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

"""pipelined common code"""

from .config import Config
from .constants import CommandStatus
from .validation import configure_flats_validation_schema, configure_standard_validation_schema
