#
# This file is part of the Robotic Observatory Control Kit (rockit)
#
# rockit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rockit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rockit.  If not, see <http://www.gnu.org/licenses/>.

"""Helper function to validate and parse the json config file"""

import json
from rockit.common import daemons, IP, validation

CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': [
        'daemon', 'log_name', 'control_machines', 'notify_frame_machines', 'cameras'
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
        'preview_clients': {
            'type': 'array',
            'items': {
                'type': 'object',
                'additionalProperties': False,
                'required': ['remote_machine', 'remote_user', 'remote_path', 'remote_command', 'key'],
                'properties': {
                    'remote_machine': {
                        'type': 'string',
                        'machine_name': True
                    },
                    'remote_user': {
                        'type': 'string',
                    },
                    'remote_path': {
                        'type': 'string',
                    },
                    'remote_command': {
                        'type': 'string',
                    },
                    'key': {
                        'type': 'string',
                    }
                }
            }
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
                            'float1dp', 'float2dp', 'float3dp', 'float5dp',
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
                        'type': ['string', 'array'],
                        'items': {
                            'type': 'string'
                        }
                    },
                    'type': {
                        'type': 'string',
                        'enum': [
                            'float1dp', 'float2dp', 'float3dp', 'float5dp',
                            'sexagesimalha', 'sexagesimaldeg',
                            'int', 'string', 'bool'
                        ]
                    }
                }
            }
        }
    },
    'dependencies': {
        'ops_daemon': ['guiding_min_interval'],
        'guiding_min_interval': ['ops_daemon'],
        'environment_cards': ['environment_query_timeout', 'environment_daemon'],
        'environment_query_timeout': ['environment_cards', 'environment_daemon'],
        'environment_daemon': ['environment_cards', 'environment_query_timeout'],
        'telescope_cards': ['telescope_query_timeout'],
        'telescope_query_timeout': ['telescope_cards']
    }
}

CAMERA_CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': [
        'worker_daemon', 'worker_processes',
        'input_data_path', 'output_data_path', 'ssh_root_path',
        'platescale', 'image_region_card', 'object_minpix',
        'preview_min_interval', 'preview_max_instances', 'preview_ds9_width', 'preview_ds9_height',
        'preview_ds9_zoom', 'preview_display_camera_id', 'preview_display_filter'
        # Note: overscan_region_card, binning_card, coadditions_card are optional
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
        'ssh_root_path': {
            'type': 'string',
            'directory_path': True
        },
        'output_filename_add_camera_id': {
            'type': 'boolean'
        },
        'output_filename_add_filter': {
            'type': 'boolean'
        },
        'binning_card': {
            'type': 'string'
        },
        'image_region_card': {
            'type': 'string'
        },
        'overscan_region_card': {
            'type': 'string'
        },
        'window_region_card': {
            'type': 'string'
        },
        'coadditions_card': {
            'type': 'string'
        },
        'platescale': {
            'type': 'number'
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
        'preview_display_camera_id': {
            'type': 'boolean'
        },
        'preview_display_filter': {
            'type': 'boolean'
        },
        'hfd_grid_tiles_x': {
            'type': 'integer',
            'minimum': 1
        },
        'hfd_grid_tiles_y': {
            'type': 'integer',
            'minimum': 1
        },
        'calibrations_path': {
            'type': 'string'
        },
        'wcs': {
            'type': 'object',
            'additionalProperties': False,
            'required': [
                'scale_high', 'scale_low', 'timeout'
                # Note: astrometry_daemon, tel_ra_card, tel_dec_card, search_radius are optional
            ],
            'properties': {
                'astrometry_daemon': {
                    'type': 'string',
                    'daemon_name': True
                },
                'scale_high': {
                    'type': 'number'
                },
                'scale_low': {
                    'type': 'number'
                },
                'timeout': {
                    'type': 'number'
                },
                'tel_ra_card': {
                    'type': 'string'
                },
                'tel_dec_card': {
                    'type': 'string'
                },
                'search_radius': {
                    'type': 'number'
                }
            },
            'dependencies': {
                'tel_ra_card': ['tel_dec_card', 'search_radius'],
                'tel_dec_card': ['tel_ra_card', 'search_radius'],
                'search_radius': ['tel_ra_card', 'tel_dec_card'],
            }
        },
        'dashboard': {
            'type': 'object',
            'additionalProperties': False,
            'required': [
                'prefix', 'flip_vertical', 'flip_horizontal',
                'min_threshold', 'max_threshold', 'thumb_size', 'clip_size'
            ],
            'properties': {
                'user': {
                    'type': 'string',
                },
                'group': {
                    'type': 'string',
                },
                'key': {
                    'type': 'string',
                },
                'remote_user': {
                    'type': 'string',
                },
                'remote_machine': {
                    'type': 'string',
                    'machine_name': True
                },
                'remote_path': {
                    'type': 'string',
                },
                'local_path': {
                    'type': 'string',
                },
                'prefix': {
                    'type': 'string'
                },
                'flip_vertical': {
                    'type': 'boolean'
                },
                'flip_horizontal': {
                    'type': 'boolean'
                },
                'min_threshold': {
                    'type': 'number'
                },
                'max_threshold': {
                    'type': 'number'
                },
                'thumb_size': {
                    'type': 'integer'
                },
                'clip_size': {
                    'type': 'integer'
                },
                'min_interval': {
                    'type': 'number',
                    'minimum': 0
                }
            },
            'anyOf': [
                {'required': ['key', 'remote_user', 'remote_machine', 'remote_path']},
                {'required': ['user', 'group', 'local_path']}
            ]
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
        self.log_name = config_json['log_name']
        self.control_ips = [getattr(IP, machine) for machine in config_json['control_machines']]
        self.notify_frame_machines = [getattr(IP, machine) for machine in config_json['notify_frame_machines']]
        self.guiding_min_interval = 0
        self.ops_daemon_name = None
        self.environment_daemon_name = None
        self.environment_cards = []
        self.environment_query_timeout = 0
        self.telescope_cards = []
        self.telescope_query_timeout = 0
        self.preview_client_config = config_json.get('preview_clients', [])
        self.cameras = config_json['cameras']

        if 'ops_daemon' in config_json:
            self.ops_daemon_name = config_json['ops_daemon']
            self.guiding_min_interval = config_json['guiding_min_interval']

        if 'environment_cards' in config_json:
            self.environment_cards = config_json['environment_cards']
            self.environment_daemon_name = config_json['environment_daemon']
            self.environment_query_timeout = config_json['environment_query_timeout']

        if 'telescope_cards' in config_json:
            self.telescope_cards = config_json['telescope_cards']
            self.telescope_query_timeout = config_json['telescope_query_timeout']
            for card in self.telescope_cards:
                card['daemon'] = getattr(daemons, card['daemon'])
