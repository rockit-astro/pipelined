#!/usr/bin/env python3.6
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

import threading
import Pyro4
import warwick.observatory as observatory

class FakeTelescope:
    @Pyro4.expose
    def report_status(self):
        """Returns fake status"""
        return {
            'state': 4,
            'state_label': 'GUIDING',
            'software_version': '1.15 (git-0e36a5e)',
            'site_latitude': 0,
            'site_longitude': 0,
            'site_elevation': 0,
            'ra': 4.015007771165315,
            'dec': -0.43680355189662085,
            'offset_ra': 0,
            'offset_dec': 0,
            'alt': 0.607880725177105,
            'az': 2.900353244379137,
            'lst': 0,
            'telescope_focus_um': 7750,
        }

def __fake_telescope():
    observatory.daemons.onemetre_telescope.launch(FakeTelescope())

class FakeVaisala:
    @Pyro4.expose
    def last_measurement(self):
        return {
            'dew_point_delta': 26.45,
            'wind_speed': 6.7,
            'accumulated_rain': 0.0,
            'date': '2016-07-05T13:36:23Z',
            'dew_point_delta_valid': True,
            'temperature': 19.9,
            'relative_humidity': 16.1,
            'pressure': 777.2,
            'software_version': '1.10 (git-976caac)',
            'accumulated_rain_valid': True,
            'relative_humidity_valid': True,
            'pressure_valid': True,
            'temperature_valid': True,
            'wind_direction': 317.0,
            'wind_direction_valid': True,
            'wind_speed_valid': True
        }

def __fake_vaisala():
    observatory.daemons.onemetre_vaisala.launch(FakeVaisala())

class FakeRoomalert:
    @Pyro4.expose
    def last_measurement(self):
        return {
            'date': '2016-07-05T13:37:50Z',
            'external_humidity': 1.49,
            'trap_closed': True,
            'roomalert_humidity': 7.93,
            'security_system_safe': True,
            'external_temp': 23.0,
            'roomalert_temp': 26.2,
            'software_version': '1.8 (git-d730d6c)',
            'truss_temp': 25.31,
            'internal_temp': 24.5,
            'internal_humidity': 11.5,
            'hatch_closed': True
        }

def __fake_roomalert():
    observatory.daemons.onemetre_roomalert.launch(FakeRoomalert())

class FakeSwasp:
    @Pyro4.expose
    def last_measurement(self):
        return {
            'dew_point_delta': 23.93,
            'wind_speed': 8,
            'jd': 2457575.06781,
            'date': '2016-07-05T13:39:02Z',
            'wind_direction': 291,
            'ext_temperature': 20.3,
            'ext_humidity': 19.0,
            'sky_temp': -43.8,
            'software_version': '1.10 (git-11c0ced)'
        }

def __fake_swasp():
    observatory.daemons.superwasp_log.launch(FakeSwasp())

class FakeLog:
    @Pyro4.expose
    def log_info(self, table, message):
        print('LOG INFO ' + table + ': ' + message)

    @Pyro4.expose
    def log_warning(self, table, message):
        print('LOG WARNING ' + table + ': ' + message)

    @Pyro4.expose
    def log_error(self, table, message):
        print('LOG ERROR ' + table + ': ' + message)

def __fake_log():
    observatory.daemons.observatory_log.launch(FakeLog())

observatory.daemons.observatory_log.host = '127.0.0.1'
observatory.daemons.onemetre_vaisala.host = '127.0.0.1'
observatory.daemons.onemetre_roomalert.host = '127.0.0.1'
observatory.daemons.superwasp_log.host = '127.0.0.1'
observatory.daemons.onemetre_telescope.host = '127.0.0.1'
observatory.daemons.onemetre_pipeline.host = '127.0.0.1'

threading.Thread(target=__fake_telescope).start()
threading.Thread(target=__fake_vaisala).start()
threading.Thread(target=__fake_roomalert).start()
threading.Thread(target=__fake_swasp).start()
threading.Thread(target=__fake_log).start()
