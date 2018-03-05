#!/usr/bin/env python3
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

"""Validation schema used by opsd to verify observation schedule blocks"""

# pylint: disable=invalid-name

def configure_flats_validation_schema():
    """Path and Prefix are the only valid user-configurable properties when taking flats"""
    return {
        'type': 'object',
        'additionalProperties': False,
        'required': ['path', 'prefix'],
        'properties': {
            'path': {
                'type': 'string',
            },
            'prefix': {
                'type': 'string'
            },
        }
    }

def configure_standard_validation_schema():
    """Standard observations support all properties"""
    return {
        'type': 'object',
        'additionalProperties': False,
        'required': ['path', 'prefix', 'type', 'archive'],
        'properties': {
            'path': {
                'type': 'string',
            },
            'prefix': {
                'type': 'string'
            },
            'type': {
                'type': 'string',
                'enum': ['BIAS', 'DARK', 'FLAT', 'SCIENCE', 'JUNK']
            },
            'object': {
                'type': 'string'
            },
            'archive': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'RED': {
                        'type': 'boolean',
                    },
                    'BLUE': {
                        'type': 'boolean',
                    }
                }
            },
            'wcs': {
                'type': 'boolean'
            },
            'intstats': {
                'type': 'boolean'
            },
            'fwhm': {
                'type': 'boolean'
            },
            'compression': {
                'type': 'boolean'
            }
        }
    }
