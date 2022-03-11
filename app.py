#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 08:47

@author: johannes
"""
import flask
from flask_caching import Cache
import connexion
from handler import Station, get_list_file

"""
Microservice Template:
    - https://github.com/shark-microservices/microservice_station

This service is intended for SMHI-NODC use.
    - It handles the station list file (station.txt) and versioning (SVN)
    - Examples: See ./example/
"""


def get_file(*args, **kwargs):
    """Get station file."""
    content = get_list_file()
    response = flask.Response(content)
    response.headers['Content-Type'] = 'text/csv'
    return response


def get_data(*args, attribute=None, attribute_list=None, all_attributes=False,
             local_id=None, station_localid=None, **kwargs):
    """Get data from master station list.

    Args:
        attribute (str): Attribute
        attribute_list (str): List of attributes
        all_attributes (bool): The complete list? (True | False)
        local_id (str): ID of the local (Provplats)
        station_localid (str): ID of the station (Övervakningsstation)
    """
    if attribute:
        return station_handler.get_attribute_list(attribute=attribute)
    elif attribute_list:
        return station_handler.get_dictionary(attribute_list=attribute_list)
    elif all_attributes:
        return station_handler.get_dictionary(all_attributes=all_attributes)
    elif local_id:
        return station_handler.get_data_for_id(local_id=local_id)
    elif station_localid:
        return station_handler.get_data_for_id(station_localid=station_localid)
    else:
        return 'No parameters given', 404


app = connexion.FlaskApp(
    __name__,
    specification_dir='./',
    options={'swagger_url': '/'},
)
app.add_api('openapi.yaml')
cache = Cache(config={
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 100 * 24 * 60 * 60  # days*hours*minutes*seconds
})
cache.init_app(app.app)


@cache.cached(timeout=100 * 24 * 60 * 60, key_prefix='all_comments')
def get_station_object():
    """Return a station object."""
    # TODO Needs to be cleared once the station list is updated.
    return Station()


station_handler = get_station_object()


if __name__ == "__main__":
    app.run(port=5000)
