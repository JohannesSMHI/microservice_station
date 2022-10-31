#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-09-23 10:30

@author: johannes
"""
from typing import Union
from pydantic import BaseModel, Field
from handler import Station
from .exceptions import ModelDoesNotExists


station_handler = Station()


class StationModel(BaseModel):
    column: Union[str, None] = Field(
        default=None,
        title='Station list column information',
        description='Return list for the given column'
    )
    columns: Union[str, None] = Field(
        # example='REG_ID,STATION_NAME,MEDIA',
        default=None,
        title='Return lists for the given columns',
        description='Return dictionary based on a list of columns'
    )
    all_columns: Union[bool, None] = Field(
        default=None,
        title='Return complete information as dictionary',
        description='Return a complete dictionary representation '
                    'of the station list'
    )
    local_id: Union[int, None] = Field(
        default=None,
        title='Local station ID',
        description='Return all column values for one station based on local-id'
    )
    station_id: Union[int, None] = Field(
        default=None,
        title='Monitoring station ID',
        description='Return all column values for one station based on '
                    'station-id'
    )
    result: None = None

    _name = 'StationModel'

    def update_result(self):
        if self.column:
            value = station_handler.get_column_list(
                column=self.column
            )
        elif self.columns or self.all_columns:
            value = station_handler.get_dictionary(
                all_columns=self.all_columns,
                columns=self.columns
            )
        elif self.local_id or self.station_id:
            value = station_handler.get_data_for_id(
                local_id=self.local_id,
                station_local_id=self.station_id
            )
        else:
            value = None

        if value:
            self.result = value
        else:
            raise ModelDoesNotExists(
                self._name,
                detail='Could not find your query specifications..'
            )
