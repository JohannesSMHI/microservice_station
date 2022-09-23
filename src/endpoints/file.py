#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-09-23 11:08

@author: johannes
"""
from fastapi import APIRouter
from starlette.responses import PlainTextResponse
from handler import get_list_file_path


router = APIRouter(
    prefix='/file',
    tags=['File'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/')
async def get_file() -> PlainTextResponse:
    """Get station file as text."""
    with open(get_list_file_path(), encoding='cp1252') as file_like:
        text = file_like.read().encode('cp1252')
    return PlainTextResponse(text, media_type='text')
