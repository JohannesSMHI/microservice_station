#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-09-23 11:00

@author: johannes
"""
from fastapi import APIRouter, Depends
from src.models import StationModel

router = APIRouter(
    tags=['Station attributes'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/stations/')
async def stations(query: StationModel = Depends()):
    """Return list for the given attribute."""
    query.update_result()
    return query.dict()
