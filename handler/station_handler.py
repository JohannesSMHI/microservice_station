#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 10:57

@author: johannes
"""
from pathlib import Path
import pandas as pd

LIST_PATH = Path(__file__).parent.joinpath('resources/station.txt')


def get_list_file():
    """Return file content."""
    with open(LIST_PATH) as f:
        return f.read().encode('cp1252')


class Station:
    """Handler for the station list at the datahost at SMHI."""

    def __init__(self):
        """Initialize."""
        self.df = pd.read_csv(
            LIST_PATH,
            sep='\t',
            header=0,
            encoding='cp1252',
            dtype=str,
            keep_default_na=False,
        )

    def get_attribute_list(self, attribute=None):
        """Return list.

        Get all values from a specific attribute (eg. STATION_NAME).
        """
        return {attribute: self.df[attribute].to_list()}

    def get_dictionary(self, all_attributes=None, attribute_list=None):
        """Return list.

        Get all values for a list of attributes.

        Args:
            all_attributes (bool): The complete list? (True | False)
            attribute_list (str): String list of attributes.
                                  Example: 'REG_ID,STATION_NAME,COMNT'
        """
        if all_attributes:
            return self.df.to_dict(orient='list')
        elif attribute_list:
            lista = list(map(str.strip, attribute_list.split(',')))
            return self.df[lista].to_dict(orient='list')
        else:
            return 'No parameters given', 404

    def get_data_for_id(self, local_id=None, station_localid=None):
        """Return dictionary for id.

        Args:
            local_id (str): ID of the local (Provplats).
            station_localid (str): ID of the station (Övervakningsstation).
        """
        if local_id:
            boolean = self.df['REG_ID'] == local_id
        elif station_localid:
            boolean = self.df['REG_ID_GROUP'] == station_localid
        else:
            return None
        return self.df.loc[boolean, :].squeeze().to_dict()


if __name__ == "__main__":
    statn = Station()
