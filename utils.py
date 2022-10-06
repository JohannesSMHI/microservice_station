#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-10-06 17:21

@author: johannes
"""
import os
from time import monotonic_ns
from functools import lru_cache, wraps


def get_list_path():
    return os.getenv(
        'SHARK_STATION_LIST',
        'handler/resources/station.txt'
    )


def timed_lru_cache(_func=None, *, seconds: int = 600,
                    maxsize: int = 128, typed: bool = False):
    def wrapper_cache(f):
        f = lru_cache(maxsize=maxsize, typed=typed)(f)
        f.delta = seconds * 10 ** 9
        f.expiration = monotonic_ns() + f.delta

        @wraps(f)
        def wrapped_f(*args, **kwargs):
            if monotonic_ns() >= f.expiration:
                f.cache_clear()
                f.expiration = monotonic_ns() + f.delta
            return f(*args, **kwargs)

        wrapped_f.cache_info = f.cache_info
        wrapped_f.cache_clear = f.cache_clear
        return wrapped_f

    # To allow decorator to be used without arguments
    if _func is None:
        return wrapper_cache
    else:
        return wrapper_cache(_func)
