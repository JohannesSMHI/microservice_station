#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 10:57

@author: johannes
"""
import pandas as pd
from utils import timed_lru_cache, get_list_path

LIST_PATH = get_list_path()


def get_list_file():
    """Return file content."""
    with open(LIST_PATH, encoding='cp1252') as f:
        return f.read().encode('cp1252')


def get_list_file_path():
    """Return file path."""
    return LIST_PATH


class Station:
    """Handler for the station list at the datahost at SMHI."""

    def __init__(self):
        """Initialize."""
        self.valid_columns = set(self.df.columns)

    @property
    @timed_lru_cache(seconds=3600)
    def df(self):
        """Return cached dataframe with "time to live" set to 1 hour."""
        return pd.read_csv(
            LIST_PATH,
            sep='\t',
            header=0,
            encoding='cp1252',
            dtype=str,
            keep_default_na=False,
        )

    def get_list(self, attribute):
        return self.df[attribute].to_list()

    def get_column_list(self, column=None):
        """Return list.

        Get all values from a specific column (eg. STATION_NAME).
        """
        if column in self.valid_columns:
            return {column: self.get_list(column)}
        else:
            return None

    def get_dictionary(self, all_columns=False, columns=None):
        """Return list.

        Get all values for a list of columns.

        Args:
            all_columns (bool): The complete list? (True | False)
            columns (str): String list of columns.
                           Example: 'REG_ID,STATION_NAME,COMNT'
        """
        if all_columns:
            return self.df.to_dict(orient='list')
        elif columns:
            columns = list(map(str.strip, columns.split(',')))
            return self.df[columns].to_dict(orient='list')
        else:
            return None

    def get_data_for_id(self, local_id=None, station_local_id=None):
        """Return dictionary for id.

        Args:
            local_id (str): ID of the local (Provplats).
            station_local_id (str): ID of the station (Övervakningsstation).
        """
        if local_id:
            boolean = self.df['REG_ID'] == local_id
        elif station_local_id:
            boolean = self.df['REG_ID_GROUP'] == station_local_id
        else:
            return None

        if boolean.any():
            return self.df.loc[boolean, :].squeeze().to_dict()
        else:
            return None
