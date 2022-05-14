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

"""Helper function to validate and parse the json config file"""

import json
from warwick.observatory.common import daemons, IP, validation

CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': [
        'daemon', 'environment_daemon', 'environment_query_timeout', 'telescope_query_timeout', 'ops_daemon',
        'log_name', 'control_machines', 'notify_frame_machines', 'incoming_data_path', 'data_root_path', 'dashboard_output_path',
        'cameras', 'environment_cards', 'telescope_cards'
    ],
    'properties': {
        'daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'environment_daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'environment_query_timeout': {
            'type': 'number',
            'minimum': 0,
        },
        'telescope_query_timeout': {
            'type': 'number',
            'minimum': 0,
        },
        'ops_daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'log_name': {
            'type': 'string',
        },
        'control_machines': {
            'type': 'array',
            'items': {
                'type': 'string',
                'machine_name': True
            }
        },
        'notify_frame_machines': {
            'type': 'array',
            'items': {
                'type': 'string',
                'machine_name': True
            }
        },
        'incoming_data_path': {
            'type': 'string',
            'directory_path': True
        },
        'data_root_path': {
            'type': 'string',
            'directory_path': True
        },
        'dashboard_output_path': {
            'type': 'string',
            'directory_path': True
        },
        'cameras': {
            'type': 'object',
            'additionalProperties': {
                'type': 'object',
                'additionalProperties': False,
                'required': [
                    'wcs_scale_high', 'wcs_scale_low', 'wcs_timeout',
                    'wcs_search_ra_card', 'wcs_search_dec_card', 'wcs_search_radius',
                    'platescale', 'image_region_card', 'object_minpix',
                    'preview_ds9_width', 'preview_ds9_height', 'preview_ds9_zoom', 'preview_ds9_annotation_margin',
                    'dashboard_flip_vertical', 'dashboard_flip_horizontal',
                    'dashboard_min_threshold', 'dashboard_max_threshold', 'dashboard_thumb_size', 'dashboard_clip_size'
                    # Note: wcs_search_ra_card, 'wcs_search_dec_card, wcs_search_radius, ccd_bin_card are optional
                ],
                'properties': {
                    'wcs_scale_high': {
                        'type': 'number'
                    },
                    'wcs_scale_low': {
                        'type': 'number'
                    },
                    'wcs_timeout': {
                        'type': 'number'
                    },
                    'wcs_search_ra_card': {
                        'type': 'string'
                    },
                    'wcs_search_dec_card': {
                        'type': 'string'
                    },
                    'wcs_search_radius': {
                        'type': 'number'
                    },
                    'ccd_bin_card': {
                        'type': 'string'
                    },
                    'image_region_card': {
                        'type': 'string'
                    },
                    'platescale': {
                        'type': 'number'
                    },
                    'object_minpix': {
                        'type': 'integer'
                    },
                    'preview_ds9_width': {
                        'type': 'integer'
                    },
                    'preview_ds9_height': {
                        'type': 'integer'
                    },
                    'preview_ds9_zoom': {
                        'type': 'number'
                    },
                    'preview_ds9_annotation_margin': {
                        'type': 'number'
                    },
                    'dashboard_flip_vertical': {
                        'type': 'boolean'
                    },
                    'dashboard_flip_horizontal': {
                        'type': 'boolean'
                    },
                    'dashboard_min_threshold': {
                        'type': 'number'
                    },
                    'dashboard_max_threshold': {
                        'type': 'number'
                    },
                    'dashboard_thumb_size': {
                        'type': 'integer'
                    },
                    'dashboard_clip_size': {
                        'type': 'integer'
                    },
                    'dashboard_max_cadence': {
                        'type': 'number',
                        'minimum': 0
                    },
                    'hfd_grid_tiles_x': {
                        'type': 'integer',
                        'minimum': 1
                    },
                    'hfd_grid_tiles_y': {
                        'type': 'integer',
                        'minimum': 1
                    }
                }
            }
        },
        'environment_cards': {
            'type': 'array',
            'items': {
                'type': 'object',
                'additionalProperties': False,
                'required': [
                    'key', 'comment', 'sensor', 'parameter', 'type'
                ],
                'properties': {
                    'key': {
                        'type': 'string',
                        'maxLength': 8
                    },
                    'comment': {
                        'type': 'string',
                        'maxLength': 68
                    },
                    'camera': {
                        'type': 'string'
                    },
                    'sensor': {
                        'type': 'string'
                    },
                    'parameter': {
                        'type': 'string'
                    },
                    'type': {
                        'type': 'string',
                        'enum': [
                            'float1dp', 'float2dp', 'float5dp',
                            'int', 'string', 'bool'
                        ]
                    }
                }
            }
        },
        'telescope_cards': {
            'type': 'array',
            'items': {
                'type': 'object',
                'additionalProperties': False,
                'required': [
                    'key', 'comment', 'daemon', 'parameter', 'type'
                ],
                'properties': {
                    'key': {
                        'type': 'string',
                        'maxLength': 8
                    },
                    'comment': {
                        'type': 'string',
                        'maxLength': 68
                    },
                    'camera': {
                        'type': 'string'
                    },
                    'daemon': {
                        'type': 'string',
                        'daemon_name': True
                    },
                    'method': {
                        'type': 'string'
                    },
                    'parameter': {
                        'type': 'string'
                    },
                    'type': {
                        'type': 'string',
                        'enum': [
                            'float1dp', 'float2dp', 'float5dp',
                            'sexagesimalha', 'sexagesimaldeg',
                            'int', 'string', 'bool'
                        ]
                    }
                }
            }
        }
    }
}


class Config:
    """Daemon configuration parsed from a json file"""
    def __init__(self, config_filename, validate_directories=True):
        # Will throw on file not found or invalid json
        with open(config_filename, 'r') as config_file:
            config_json = json.load(config_file)

        # Will throw on schema violations
        validators = {
            'daemon_name': validation.daemon_name_validator,
            'machine_name': validation.machine_name_validator
        }

        # Don't validate directories if we are loading the config on a different machine
        if validate_directories:
            validators['directory_path'] = validation.directory_path_validator

        validation.validate_config(config_json, CONFIG_SCHEMA, validators)

        self.daemon = getattr(daemons, config_json['daemon'])
        self.environment_daemon = getattr(daemons, config_json['environment_daemon'])
        self.environment_query_timeout = config_json['environment_query_timeout']
        self.telescope_query_timeout = config_json['telescope_query_timeout']
        self.ops_daemon = getattr(daemons, config_json['ops_daemon'])
        self.log_name = config_json['log_name']
        self.control_ips = [getattr(IP, machine) for machine in config_json['control_machines']]
        self.notify_frame_machines = [getattr(IP, machine) for machine in config_json['notify_frame_machines']]
        self.incoming_data_path = config_json['incoming_data_path']
        self.data_root_path = config_json['data_root_path']
        self.dashboard_output_path = config_json['dashboard_output_path']
        self.cameras = config_json['cameras']
        self.environment_cards = config_json['environment_cards']
        self.telescope_cards = config_json['telescope_cards']
        for card in self.telescope_cards:
            card['daemon'] = getattr(daemons, card['daemon'])
