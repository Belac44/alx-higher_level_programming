#!/usr/bin/python3

def lookup(obj):
    return sorted((list(obj.__dict__)) + (dir(obj)))