#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 08:47

@author: johannes
"""
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
# from routes.api import router as api_router
from fastapi import APIRouter
from starlette.responses import StreamingResponse

from handler import Station, get_list_file, get_list_file_path
from pydantic import BaseModel, Field
from typing import Union


api_router = APIRouter(
    # prefix="/",
    tags=["Station list"],
    responses={404: {"description": "Not found"}},
)

app = FastAPI()

origins = ["http://localhost:8010"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)


class StationModel(BaseModel):
    attribute: Union[str, None] = Field(
        default=None,
        title='Station attribute',
        description='Return list for the given attribute'
    )
    attribute_list: Union[str, None] = Field(
        default=None,
        title='Return attribute values',
        description='Return dictionary based on a list of attributes'
    )
    all_attributes: bool = Field(
        default=False,
        title='Return all attributes',
        description='description Station list attribute'
    )
    local_id: Union[str, None] = Field(
        default=None,
        title='Return station attributes',
        description='Return all attribute values for one '
                    'station based on local-id'
    )
    station_local_id: Union[str, None] = Field(
        default=None,
        title='Return station attributes',
        description='Return all attribute values for one '
                    'station based on station-local-id'
    )


@app.get('/getdata/')
async def get_data(content: StationModel):
    """Get data from master station list."""
    if content.attribute:
        return station_handler.get_attribute_list(
            attribute=content.attribute)
    elif content.attribute_list:
        return station_handler.get_dictionary(
            attribute_list=content.attribute_list)
    elif content.all_attributes:
        return station_handler.get_dictionary(
            all_attributes=content.all_attributes)
    elif content.local_id:
        return station_handler.get_data_for_id(
            local_id=content.local_id)
    elif content.station_local_id:
        return station_handler.get_data_for_id(
            station_local_id=content.station_local_id)
    else:
        return 'No parameters given', 404


@app.get('/getfile/')
async def get_file() -> StreamingResponse:
    """Get station file."""
    def iterate_file():
        with open(get_list_file_path(), encoding='cp1252') as file_like:
            yield from file_like
            # return file_like.read().encode('cp1252')
    return StreamingResponse(iterate_file(), media_type='text')


station_handler = Station()


app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host='127.0.0.1',
        port=8010,
        log_level="info",
        reload=True
    )

