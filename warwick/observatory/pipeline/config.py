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
        'log_name', 'control_machines', 'notify_frame_machines', 'guiding_min_interval',
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
        'guiding_min_interval': {
            'type': 'number',
            'minimum': 0,
        },
        'cameras': {
            'type': 'object',
            # see CAMERA_CONFIG_SCHEMA for the sub-schema
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

CAMERA_CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': [
        'worker_daemon', 'worker_processes',
        'input_data_path', 'output_data_path',
        'dashboard_user', 'dashboard_key', 'dashboard_remote_user',
        'dashboard_remote_host', 'dashboard_remote_path', 'dashboard_prefix',
        'wcs_scale_high', 'wcs_scale_low', 'wcs_timeout',
        'wcs_search_ra_card', 'wcs_search_dec_card', 'wcs_search_radius',
        'platescale', 'image_region_card', 'object_minpix',
        'preview_min_interval', 'preview_max_instances', 'preview_ds9_width', 'preview_ds9_height',
        'preview_ds9_zoom', 'preview_ds9_annotation_margin',
        'dashboard_flip_vertical', 'dashboard_flip_horizontal',
        'dashboard_min_threshold', 'dashboard_max_threshold', 'dashboard_thumb_size', 'dashboard_clip_size'
        # Note: wcs_search_ra_card, 'wcs_search_dec_card, wcs_search_radius,
        #       spatial_median, overscan_region_card, ccd_bin_card are optional
    ],
    'properties': {
        'worker_daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'worker_processes': {
            'type': 'number',
            'minimum': 1
        },
        'input_data_path': {
            'type': 'string',
            'directory_path': True
        },
        'output_data_path': {
            'type': 'string',
            'directory_path': True
        },
        'dashboard_user': {
            'type': 'string',
        },
        'dashboard_key': {
            'type': 'string',
        },
        'dashboard_remote_user': {
            'type': 'string',
        },
        'dashboard_remote_host': {
            'type': 'string',
            'machine_name': True
        },
        'dashboard_remote_path': {
            'type': 'string',
        },
        'dashboard_prefix': {
            'type': 'string'
        },
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
        'overscan_region_card': {
            'type': 'string'
        },
        'platescale': {
            'type': 'number'
        },
        'spatial_median': {
            'type': 'integer'
        },
        'object_minpix': {
            'type': 'integer'
        },
        'preview_min_interval': {
            'type': 'integer'
        },
        'preview_max_instances': {
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
        'dashboard_min_interval': {
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


class Config:
    """Daemon configuration parsed from a json file"""
    def __init__(self, config_filename, validate_camera=None):
        # Will throw on file not found or invalid json
        with open(config_filename, 'r', encoding='utf-8') as config_file:
            config_json = json.load(config_file)

        # Will throw on schema violations
        validators = {
            'daemon_name': validation.daemon_name_validator,
            'machine_name': validation.machine_name_validator,
            'directory_path': validation.directory_path_validator
        }

        validation.validate_config(config_json, CONFIG_SCHEMA, validators)

        if validate_camera:
            validation.validate_config(config_json['cameras'][validate_camera], CAMERA_CONFIG_SCHEMA, validators)

        self.daemon = getattr(daemons, config_json['daemon'])
        self.environment_daemon_name = config_json['environment_daemon']
        self.environment_query_timeout = config_json['environment_query_timeout']
        self.telescope_query_timeout = config_json['telescope_query_timeout']
        self.ops_daemon_name = config_json['ops_daemon']
        self.log_name = config_json['log_name']
        self.control_ips = [getattr(IP, machine) for machine in config_json['control_machines']]
        self.notify_frame_machines = [getattr(IP, machine) for machine in config_json['notify_frame_machines']]
        self.guiding_min_interval = config_json['guiding_min_interval']
        self.cameras = config_json['cameras']

        self.environment_cards = config_json['environment_cards']
        self.telescope_cards = config_json['telescope_cards']
        for card in self.telescope_cards:
            card['daemon'] = getattr(daemons, card['daemon'])
