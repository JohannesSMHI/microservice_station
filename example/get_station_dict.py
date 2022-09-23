#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 14:50

@author: johannes
"""
import requests


if __name__ == '__main__':
    url = "http://127.0.0.1:8010/attribute"

    response = requests.request(
        "POST", url,
        headers={"Content-type": "application/json"},
        json={"attribute": "STATION_NAME"}
    )
    data = response.json()
    print(data)
