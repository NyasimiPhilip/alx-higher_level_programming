#!/usr/bin/python3


"""Defines locked class
"""


class LockedClass:
    """LockedClass prevents the creation of new instance attributes."""

    __slots__ = 'first_name'
