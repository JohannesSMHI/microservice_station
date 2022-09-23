#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-09-23 11:00

@author: johannes
"""
from fastapi import APIRouter, HTTPException
from src.models import (
    AttributeModel,
    AttributeListModel,
    AttributeAllModel,
    LocalIdModel,
    StationIdModel
)


router = APIRouter(
    tags=['Station attributes'],
    responses={404: {'description': 'Not found'}},
)


@router.post('/attribute/')
async def get_attribute(content: AttributeModel):
    """Return list for the given attribute."""
    if not content.attribute:
        raise HTTPException(
            status_code=404,
            detail='Could not find your attribute'
        )
    return content.attribute


@router.post('/attribute-list/')
async def get_attribute_list(content: AttributeListModel):
    """Return list for the given attribute list.

    The attribute list should be in a string format, eg. 'REG_ID,STATION_NAME'.
    """
    if not content.attribute_list:
        raise HTTPException(
            status_code=404,
            detail=('Could not find one or more of your attributes.',
                    'Make sure all of the given attributes are valid.')
        )
    return content.attribute_list


@router.post('/attribute-all/')
async def get_all_attributes(content: AttributeAllModel):
    """Return a complete dictionary representation of the station list."""
    if not content.all_attributes:
        raise HTTPException(
            status_code=404,
            detail=('Could not deliver any data.',
                    'Did you pass the bool argument as false?')
        )
    return content.all_attributes


@router.post('/local-id/')
async def get_attributes_for_local_id(content: LocalIdModel):
    """Return all attributes for the given local-id."""
    if not content.local_id:
        raise HTTPException(
            status_code=404,
            detail=('Could not find your data for your id.',
                    'Perhaps you used a station id and not a local id?')
        )
    return content.local_id


@router.post('/station-id/')
async def get_attributes_for_station_id(content: StationIdModel):
    """Return all attributes for the given station-id."""
    if not content.station_id:
        raise HTTPException(
            status_code=404,
            detail=('Could not find your data for your id.',
                    'Perhaps you used a local id and not a station id?')
        )
    return content.station_id
