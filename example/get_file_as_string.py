#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 14:51

@author: johannes
"""
import requests
import pandas as pd
from io import StringIO


if __name__ == '__main__':
    url = "http://10.64.10.247:5000/getfile"

    response = requests.request("GET", url)

    # Store string data in a pandas Dataframe.
    df = pd.read_csv(
        StringIO(response.text),
        sep='\t',
        header=0,
        encoding='cp1252',
        dtype=str,
        keep_default_na=False,
    )
