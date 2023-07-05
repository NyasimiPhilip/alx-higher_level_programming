#!/usr/bin/python3
"""Defines locked class
"""
class LockedClass:
    """
    Prevent object instantiation of new LockedClass attribute
    other thatn first_name"""
    __slots__ = ["first_name"]
