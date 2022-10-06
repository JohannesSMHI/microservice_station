#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 08:47

@author: johannes
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from routes.api import router as api_router
from src.models import ModelDoesNotExists


app = FastAPI()

origins = ['http://localhost:8010']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['GET'],
    allow_headers=['*'],
)

app.include_router(api_router)


@app.exception_handler(ModelDoesNotExists)
async def validation_exception_handler(request, exc):
    """Override exceptions."""
    return PlainTextResponse(str(exc), status_code=404)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """Override exceptions."""
    return PlainTextResponse(str(exc), status_code=400)


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='127.0.0.1',
        port=8010,
        log_level='info',
        reload=True
    )
