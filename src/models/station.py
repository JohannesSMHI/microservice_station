#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-09-23 10:30

@author: johannes
"""
from pydantic import BaseModel, Field, validator
from typing import Union
from handler import Station

station_handler = Station()


class AttributeModel(BaseModel):
    attribute: Union[str, dict, None] = Field(
        default='STATION_NAME',
        title='Station attribute',
        description='Return list for the given attribute'
    )

    @validator('attribute', pre=True)
    def parse_attribute(cls, value):
        if value:
            if value in station_handler.valid_attributes:
                return station_handler.get_attribute_list(attribute=value)
            else:
                return None
        else:
            return None


class AttributeListModel(BaseModel):
    attribute_list: Union[str, dict, None] = Field(
        default='REG_ID,STATION_NAME,MEDIA',
        title='Return attribute values',
        description='Return dictionary based on a list of attributes'
    )

    @validator('attribute_list', pre=True)
    def parse_attribute_list(cls, value):
        if value:
            return station_handler.get_dictionary(attribute_list=value)
        else:
            return None


class AttributeAllModel(BaseModel):
    all_attributes: Union[bool, dict] = Field(
        default=True,
        title='',
        description='Return a complete dictionary representation '
                    'of the station list'
    )

    @validator('all_attributes', pre=True)
    def parse_all_attributes(cls, value):
        if value:
            return station_handler.get_dictionary(all_attributes=value)
        else:
            return None


class LocalIdModel(BaseModel):
    local_id: Union[str, dict, None] = Field(
        default='135404',
        title='Return station attributes',
        description='Return all attribute values for one '
                    'station based on local-id'
    )

    @validator('local_id', pre=True)
    def parse_local_id(cls, value):
        if value:
            return station_handler.get_data_for_id(local_id=str(value))
        else:
            return None


class StationIdModel(BaseModel):
    station_id: Union[str, dict, None] = Field(
        default='263732',
        title='Return station attributes',
        description='Return all attribute values for one '
                    'station based on station-local-id'
    )

    @validator('station_id', pre=True)
    def parse_station_local_id(cls, value):
        if value:
            return station_handler.get_data_for_id(station_local_id=str(value))
        else:
            return None
