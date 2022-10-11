#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-09-23 10:30

@author: johannes
"""
from pydantic import BaseModel, Field, validator
from handler import Station
from .exceptions import ModelDoesNotExists


station_handler = Station()


class AttributeModel(BaseModel):
    attribute: dict = Field(
        default='STATION_NAME',
        title='Station attribute',
        description='Return list for the given attribute'
    )
    _name = 'AttributeModel'

    @validator('attribute', pre=True)
    def validate_attribute(cls, value):
        value = station_handler.get_attribute_list(attribute=value)
        if value:
            return value
        else:
            raise ModelDoesNotExists(
                cls._name,
                detail='Could not find your attribute'
            )


class AttributeListModel(BaseModel):
    attribute_list: dict = Field(
        default='REG_ID,STATION_NAME,MEDIA',
        title='Return attribute values',
        description='Return dictionary based on a list of attributes'
    )
    _name = 'AttributeListModel'

    @validator('attribute_list', pre=True)
    def validate_attribute_list(cls, value):
        if value:
            return station_handler.get_dictionary(attribute_list=value)
        else:
            raise ModelDoesNotExists(
                cls._name,
                detail=('Could not find one or more of your attributes.',
                        'Make sure all of the given attributes are valid.')
            )


class AttributeAllModel(BaseModel):
    all_attributes: dict = Field(
        default=True,
        title='',
        description='Return a complete dictionary representation '
                    'of the station list'
    )
    _name = 'AttributeAllModel'

    @validator('all_attributes', pre=True)
    def validate_all_attributes(cls, value):
        if value:
            return station_handler.get_dictionary(all_attributes=value)
        else:
            raise ModelDoesNotExists(
                cls._name,
                detail=('Could not deliver any data.',
                        'Did you pass the bool argument as false?')
            )


class LocalIdModel(BaseModel):
    local_id: dict = Field(
        default='135404',
        title='Return station attributes',
        description='Return all attribute values for one '
                    'station based on local-id'
    )
    _name = 'LocalIdModel'

    @validator('local_id', pre=True)
    def validate_local_id(cls, value):
        value = station_handler.get_data_for_id(local_id=str(value))
        if value:
            return value
        else:
            raise ModelDoesNotExists(
                cls._name,
                detail=('Could not find data for your id.',
                        'Perhaps you used a station id and not a local id?')
            )


class StationIdModel(BaseModel):
    station_id: dict = Field(
        default='263732',
        title='Return station attributes',
        description='Return all attribute values for one '
                    'station based on station-local-id'
    )
    _name = 'StationIdModel'

    @validator('station_id', pre=True)
    def validate_station_local_id(cls, value):
        if value:
            return station_handler.get_data_for_id(station_local_id=str(value))
        else:
            raise ModelDoesNotExists(
                cls._name,
                detail=('Could not find data for your id.',
                        'Perhaps you used a local id and not a station id?')
            )
