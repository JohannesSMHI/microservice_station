#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-09-23 11:00

@author: johannes
"""
from fastapi import APIRouter
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


@router.get('/attribute', response_model=AttributeModel)
async def get_attribute(attribute: str):
    """Return list for the given attribute."""
    return {'attribute': attribute}


@router.get('/attribute-list', response_model=AttributeListModel)
async def get_attribute_list(attribute_list: str):
    """Return list for the given attribute list.

    The attribute list should be in a string format, eg. 'REG_ID,STATION_NAME'.
    """
    return {'attribute_list': attribute_list}


@router.get('/attribute-all', response_model=AttributeAllModel)
async def get_all_attributes(all_attributes: bool):
    """Return a complete dictionary representation of the station list."""
    return {'all_attributes': all_attributes}


@router.get('/local-id', response_model=LocalIdModel)
async def get_attributes_for_local_id(local_id: str):
    """Return all attributes for the given local-id."""
    return {'local_id': local_id}


@router.get('/station-id', response_model=StationIdModel)
async def get_attributes_for_station_id(station_id: str):
    """Return all attributes for the given station-id."""
    return {'station_id': station_id}
