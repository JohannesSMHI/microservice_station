#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 14:50

@author: johannes
"""
import requests


if __name__ == '__main__':
    url = "http://10.64.10.247:5000/getdata"

    response = requests.request(
        "GET", url, params={'local_id': 135404}
    )
    data = response.json()
    print(data)
