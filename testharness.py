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
import numpy as np
import Pyro4
from warwick.observatory.common import daemons


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
    daemons.onemetre_telescope.launch(FakeTelescope())


class FakeEnvironment:
    @Pyro4.expose
    def status(self):
        return {"w1m_vaisala": {"label": "W1m Vaisala", "parameters": {"wind_speed": {"label": "Wind", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 120, "unit": "km/h", "limits": [0, 45], "warn_limits": [0, 30], "min": 9.3, "max": 19.3, "latest": 11.7}, "median_wind_speed": {"label": "Median Wind", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 120, "unit": "km/h", "limits": [0, 33], "warn_limits": [0, 15], "latest": 12.8}, "temperature": {"label": "Outside Temp.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 120, "unit": "\u00b0C", "limits": [0, 50], "warn_limits": [3, 30], "min": 3.1, "max": 3.9, "latest": 3.7}, "relative_humidity": {"label": "Outside Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 120, "unit": "%RH", "limits": [0, 75], "warn_limits": [0, 50], "min": 13.2, "max": 21.2, "latest": 16.3}, "pressure": {"label": "Pressure", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 120, "unit": "hPa", "latest": 768.2}, "accumulated_rain": {"label": "Accumulated Rain.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 120, "unit": "mm", "limits": [0, 0], "min": 0.0, "max": 0.0, "latest": 0.0}, "dew_point_delta": {"label": "Temp. > Dew Pt.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 120, "unit": "\u00b0C", "limits": [5, 100], "warn_limits": [10, 100], "min": 20.15, "max": 25.77, "latest": 23.31}}}, "goto_vaisala": {"label": "GOTO Vaisala", "parameters": {"wind_speed": {"label": "Wind", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:12Z", "date_end": "2021-04-30T23:49:52Z", "date_count": 119, "unit": "km/h", "limits": [0, 45], "warn_limits": [0, 30], "min": 12.2, "max": 17.7, "latest": 16.4}, "median_wind_speed": {"label": "Median Wind", "unsafe": False, "warning": True, "current": True, "date_start": "2021-04-30T23:30:12Z", "date_end": "2021-04-30T23:49:52Z", "date_count": 119, "unit": "km/h", "limits": [0, 30], "warn_limits": [0, 15], "latest": 15.1}, "temperature": {"label": "Outside Temp.", "unsafe": False, "warning": True, "current": True, "date_start": "2021-04-30T23:30:12Z", "date_end": "2021-04-30T23:49:52Z", "date_count": 119, "unit": "\u00b0C", "limits": [0, 50], "warn_limits": [3, 30], "min": 2.5, "max": 3.5, "latest": 3.1}, "relative_humidity": {"label": "Outside Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:12Z", "date_end": "2021-04-30T23:49:52Z", "date_count": 119, "unit": "%RH", "limits": [0, 75], "warn_limits": [0, 50], "min": 15.4, "max": 21.9, "latest": 17.1}, "pressure": {"label": "Pressure", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:12Z", "date_end": "2021-04-30T23:49:52Z", "date_count": 119, "unit": "hPa", "latest": 767.3}, "accumulated_rain": {"label": "Accumulated Rain.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:12Z", "date_end": "2021-04-30T23:49:52Z", "date_count": 119, "unit": "mm", "limits": [0, 0], "min": 0.0, "max": 0.0, "latest": 0.0}, "dew_point_delta": {"label": "Temp. > Dew Pt.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:12Z", "date_end": "2021-04-30T23:49:52Z", "date_count": 119, "unit": "\u00b0C", "limits": [5, 100], "warn_limits": [10, 100], "min": 19.68, "max": 23.88, "latest": 22.65}}}, "superwasp": {"label": "SuperWASP", "parameters": {"wind_speed": {"label": "Wind", "unsafe": False, "warning": False, "current": False, "date_start": "1-01-01T00:00:00Z", "date_end": "1-01-01T00:00:00Z", "date_count": 0, "unit": "km/h", "limits": [0, 40], "warn_limits": [0, 30]}, "median_wind_speed": {"label": "Median Wind", "unsafe": False, "warning": False, "current": False, "date_start": "1-01-01T00:00:00Z", "date_end": "1-01-01T00:00:00Z", "date_count": 0, "unit": "km/h", "limits": [0, 27], "warn_limits": [0, 15]}, "ext_temperature": {"label": "Outside Temp.", "unsafe": False, "warning": False, "current": False, "date_start": "1-01-01T00:00:00Z", "date_end": "1-01-01T00:00:00Z", "date_count": 0, "unit": "\u00b0C", "limits": [0, 50], "warn_limits": [3, 30]}, "ext_humidity": {"label": "Outside Hum.", "unsafe": False, "warning": False, "current": False, "date_start": "1-01-01T00:00:00Z", "date_end": "1-01-01T00:00:00Z", "date_count": 0, "unit": "%RH", "limits": [0, 75], "warn_limits": [0, 50]}, "dew_point_delta": {"label": "Temp. > Dew Pt.", "unsafe": False, "warning": False, "current": False, "date_start": "1-01-01T00:00:00Z", "date_end": "1-01-01T00:00:00Z", "date_count": 0, "unit": "\u00b0C", "limits": [5, 100], "warn_limits": [10, 100]}}}, "superwasp_aurora": {"label": "Aurora", "parameters": {"clarity": {"label": "Sky Clarity", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:10Z", "date_end": "2021-04-30T23:50:02Z", "date_count": 120, "unit": "\u00b0C", "warn_limits": [40, 60], "latest": 50.5}, "light_intensity": {"label": "Light Intensity", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:10Z", "date_end": "2021-04-30T23:50:02Z", "date_count": 120, "latest": 0.0}, "rain_intensity": {"label": "Rain Intensity", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:10Z", "date_end": "2021-04-30T23:50:02Z", "date_count": 120, "latest": 4.8}}}, "netping": {"label": "Network ping", "parameters": {"google": {"label": "Google", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:14Z", "date_count": 39, "unit": "ms", "limits": [0, 2000], "latest": 79.652}, "ngtshead": {"label": "NGTSHead", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:14Z", "date_count": 39, "unit": "ms", "limits": [0, 2000], "latest": 74.511}}}, "w1m_roomalert": {"label": "W1m RoomAlert", "parameters": {"internal_temp": {"label": "Internal Temp.", "unsafe": False, "warning": True, "current": True, "date_start": "2021-04-30T23:30:07Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 120, "unit": "\u00b0C", "limits": [0, 50], "warn_limits": [3, 30], "min": 0.22, "max": 0.47, "latest": 0.47}, "internal_humidity": {"label": "Internal Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:07Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 120, "unit": "%RH", "limits": [0, 75], "warn_limits": [0, 50], "min": 38.95, "max": 43.07, "latest": 39.08}, "truss_temp": {"label": "Truss Temp.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:07Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 120, "unit": "\u00b0C", "min": 2.5, "max": 2.56, "latest": 2.5}, "hatch_closed": {"label": "Side Hatch", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:07Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 120, "latest": True, "values": [True], "display": "BoolClosedOpen"}, "trap_closed": {"label": "Trap Door", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:07Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 120, "latest": True, "values": [True], "display": "BoolClosedOpen"}, "security_system_safe": {"label": "Tel. Sec. System", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:07Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 120, "latest": True, "display": "BoolSafeTripped"}}}, "goto_roomalert": {"label": "GOTO RoomAlert", "parameters": {"internal_temp": {"label": "GOTO Temp.", "unsafe": False, "warning": True, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:49:54Z", "date_count": 115, "unit": "\u00b0C", "limits": [0, 50], "warn_limits": [3, 30], "min": 1.6, "max": 2.6, "latest": 2.2}, "internal_humidity": {"label": "GOTO Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:49:54Z", "date_count": 115, "unit": "%RH", "limits": [0, 75], "warn_limits": [0, 50], "min": 21.88, "max": 26.43, "latest": 22.2}, "roomalert_temp": {"label": "Server Temp.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:49:54Z", "date_count": 115, "unit": "\u00b0C", "min": -1.96, "max": 0.66, "latest": -1.0}, "roomalert_humidity": {"label": "Server Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:11Z", "date_end": "2021-04-30T23:49:54Z", "date_count": 115, "unit": "%RH", "min": 10.53, "max": 17.67, "latest": 12.8}}}, "superwasp_roomalert": {"label": "SuperWASP RoomAlert", "parameters": {"comp_room_temp": {"label": "Comp. Room Temp.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:55Z", "date_count": 117, "unit": "\u00b0C", "limits": [0, 50], "warn_limits": [3, 30], "min": 21.1, "max": 22.6, "latest": 22.5}, "comp_room_humidity": {"label": "Comp. Room Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:55Z", "date_count": 117, "unit": "%RH", "limits": [0, 75], "warn_limits": [0, 50], "min": 21.98, "max": 23.29, "latest": 22.3}, "cam_room_temp": {"label": "Cam. Room Temp.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:55Z", "date_count": 117, "unit": "\u00b0C", "limits": [0, 50], "warn_limits": [3, 30], "min": 10.4, "max": 10.6, "latest": 10.5}, "cam_room_humidity": {"label": "Cam. Room Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:55Z", "date_count": 117, "unit": "%RH", "limits": [0, 75], "warn_limits": [0, 50], "min": 35.0, "max": 36.29, "latest": 35.0}, "roomalert_temp": {"label": "RoomAlert Temp.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:55Z", "date_count": 117, "unit": "\u00b0C", "min": 29.2, "max": 30.2, "latest": 30.1}, "roomalert_humidity": {"label": "RoomAlert Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:55Z", "date_count": 117, "unit": "%RH", "min": 9.62, "max": 10.27, "latest": 9.62}, "cam_rack_temp": {"label": "Cam. Rack Temp.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:49:55Z", "date_count": 117, "unit": "\u00b0C", "min": 17.68, "max": 17.87, "latest": 17.87}}}, "rasa_internal": {"label": "RASA Internal", "parameters": {"temperature": {"label": "RASA Temp.", "unsafe": False, "warning": True, "current": True, "date_start": "2021-04-30T23:30:15Z", "date_end": "2021-04-30T23:49:57Z", "date_count": 119, "unit": "\u00b0C", "warn_limits": [3, 30], "min": 2.0, "max": 2.2, "latest": 2.2}, "relative_humidity": {"label": "RASA Hum.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:15Z", "date_end": "2021-04-30T23:49:57Z", "date_count": 119, "unit": "%RH", "warn_limits": [0, 50], "min": 30.3, "max": 35.3, "latest": 30.4}}}, "w1m_power": {"label": "W1m UPS", "parameters": {"main_ups_status": {"label": "UPS Status", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:15Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 112, "latest": 2, "values": [2], "display": "UPSStatus", "valid_values": [2]}, "main_ups_battery_remaining": {"label": "UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:15Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 112, "limits": [85, 101], "warn_limits": [100, 101], "min": 100, "max": 100, "latest": 100}, "main_ups_battery_healthy": {"label": "UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:15Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 112, "latest": True, "values": [True], "display": "BoolHealthyUnhealthy", "valid_values": [True]}, "light": {"label": "Light", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:15Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 112, "latest": 0, "display": "BoolPowerOnOff"}, "dehumidifier": {"label": "Dehumidifier", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:15Z", "date_end": "2021-04-30T23:50:01Z", "date_count": 112, "latest": 0, "display": "BoolPowerOnOff"}}}, "rasa_power": {"label": "RASA UPS", "parameters": {"ups_status": {"label": "UPS Status", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:50:03Z", "date_count": 117, "latest": 2, "values": [2], "display": "UPSStatus", "valid_values": [2]}, "ups_battery_remaining": {"label": "UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:50:03Z", "date_count": 117, "limits": [85, 101], "warn_limits": [100, 101], "min": 100, "max": 100, "latest": 100}, "ups_battery_healthy": {"label": "UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:50:03Z", "date_count": 117, "latest": True, "values": [True], "display": "BoolHealthyUnhealthy", "valid_values": [True]}, "light": {"label": "Light", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:50:03Z", "date_count": 117, "latest": 0, "display": "BoolPowerOnOff"}, "dehumidifier": {"label": "Dehumidifier", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:13Z", "date_end": "2021-04-30T23:50:03Z", "date_count": 117, "latest": 0, "display": "BoolPowerOnOff"}}}, "superwasp_power": {"label": "SWASP UPS", "parameters": {"ups1_status": {"label": "UPS 1 Status", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "latest": 2, "values": [2], "display": "UPSStatus", "valid_values": [2]}, "ups1_battery_remaining": {"label": "UPS 1 Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "limits": [85, 101], "warn_limits": [100, 101], "min": 100, "max": 100, "latest": 100}, "ups1_battery_healthy": {"label": "UPS 1 Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "latest": True, "values": [True], "display": "BoolHealthyUnhealthy", "valid_values": [True]}, "ups2_status": {"label": "UPS 2 Status", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "latest": 2, "values": [2], "display": "UPSStatus", "valid_values": [2]}, "ups2_battery_remaining": {"label": "UPS 2 Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "limits": [85, 101], "warn_limits": [100, 101], "min": 100, "max": 100, "latest": 100}, "ups2_battery_healthy": {"label": "UPS 2 Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "latest": True, "values": [True], "display": "BoolHealthyUnhealthy", "valid_values": [True]}, "ups3_status": {"label": "UPS 3 Status", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "latest": 2, "values": [2], "display": "UPSStatus", "valid_values": [2]}, "ups3_battery_remaining": {"label": "UPS 3 Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "limits": [85, 101], "warn_limits": [100, 101], "min": 100.0, "max": 100.0, "latest": 100.0}, "ups3_battery_healthy": {"label": "UPS 3 Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 115, "latest": True, "values": [True], "display": "BoolHealthyUnhealthy", "valid_values": [True]}}}, "goto_ups": {"label": "GOTO UPS", "parameters": {"main_ups_status": {"label": "Main UPS Status", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:50:04Z", "date_count": 117, "latest": 2, "values": [2], "display": "UPSStatus", "valid_values": [2]}, "main_ups_battery_remaining": {"label": "Main UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:50:04Z", "date_count": 117, "limits": [85, 101], "warn_limits": [100, 101], "min": 100, "max": 100, "latest": 100}, "main_ups_battery_healthy": {"label": "Main UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:50:04Z", "date_count": 117, "latest": True, "values": [True], "display": "BoolHealthyUnhealthy", "valid_values": [True]}, "dome_ups_status": {"label": "Dome UPS Status", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:50:04Z", "date_count": 117, "latest": 2, "values": [2], "display": "UPSStatus", "valid_values": [2]}, "dome_ups_battery_remaining": {"label": "Dome UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:50:04Z", "date_count": 117, "limits": [85, 101], "warn_limits": [100, 101], "min": 100, "max": 100, "latest": 100}, "dome_ups_battery_healthy": {"label": "Dome UPS Battery", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:14Z", "date_end": "2021-04-30T23:50:04Z", "date_count": 117, "latest": True, "values": [True], "display": "BoolHealthyUnhealthy", "valid_values": [True]}}}, "w1m_diskspace": {"label": "W1m Diskspace", "parameters": {"data_fs_available_bytes": {"label": "Available", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:43Z", "date_end": "2021-04-30T23:47:43Z", "date_count": 18, "unit": "GiB", "limits": [5368709120, 1099511627776], "warn_limits": [21474836480, 1099511627776], "latest": 44739129344, "display": "DiskBytes"}}}, "rasa_diskspace": {"label": "RASA Diskspace", "parameters": {"data_fs_available_bytes": {"label": "Available", "unsafe": False, "warning": True, "current": True, "date_start": "2021-04-30T23:30:58Z", "date_end": "2021-04-30T23:49:59Z", "date_count": 20, "unit": "GiB", "limits": [5368709120, 2199023255552], "warn_limits": [214748364800, 2199023255552], "latest": 63162830848, "display": "DiskBytes"}}}, "tng": {"label": "TNG", "parameters": {"dust": {"label": "Dust Conc.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:22Z", "date_end": "2021-04-30T23:48:23Z", "date_count": 10, "unit": "ug/m\u00b3", "latest": 0.0897795578220544}, "seeing": {"label": "Seeing.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:22Z", "date_end": "2021-04-30T23:48:23Z", "date_count": 10, "unit": "\"", "latest": 0.5565460026264191}, "solarimeter": {"label": "Solarimeter.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:22Z", "date_end": "2021-04-30T23:48:23Z", "date_count": 10, "unit": "W/m\u00b2", "latest": 0.0}}}, "robodimm": {"label": "RoboDIMM", "parameters": {"seeing": {"label": "Seeing.", "unsafe": False, "warning": False, "current": False, "date_start": "1-01-01T00:00:00Z", "date_end": "1-01-01T00:00:00Z", "date_count": 0, "unit": "\""}}}, "ephem": {"label": "Ephemeris", "parameters": {"sun_alt": {"label": "Sun Alt.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:09Z", "date_end": "2021-04-30T23:49:44Z", "date_count": 40, "unit": "\u00b0", "limits": [-90, 5], "warn_limits": [-90, -10], "latest": -42.19616385627434}, "moon_alt": {"label": "Moon Alt.", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:09Z", "date_end": "2021-04-30T23:49:44Z", "date_count": 40, "unit": "\u00b0", "latest": -2.1275563045369914}, "moon_percent_illumination": {"label": "Moon Illumination", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:09Z", "date_end": "2021-04-30T23:49:44Z", "date_count": 40, "unit": "%", "latest": 79.1}}}, "rain": {"label": "Rain Detector", "parameters": {"unsafe_boards": {"label": "Triggered", "unsafe": False, "warning": False, "current": True, "date_start": "2021-04-30T23:30:10Z", "date_end": "2021-04-30T23:50:02Z", "date_count": 120, "limits": [0, 0], "latest": 0}}}}


def __fake_environment():
    daemons.localhost_test4.launch(FakeEnvironment())


class FakeOps:
    @Pyro4.expose
    def notify_processed_frame(self, headers):
        print('notified')
        print(headers)

    @Pyro4.expose
    def notify_guide_profiles(self, headers, profile_x, profile_y):
        print('profiles')
        print('x', np.array(profile_x).shape)
        print('y', np.array(profile_y).shape)

        import matplotlib.pyplot as plt
        plt.figure()
        plt.plot(np.array(profile_x), 'b-')
        plt.plot(np.array(profile_y), 'r-')
        plt.show()


def __fake_ops():
    daemons.localhost_test5.launch(FakeOps())


#threading.Thread(target=__fake_telescope).start()
threading.Thread(target=__fake_environment).start()
threading.Thread(target=__fake_ops).start()
