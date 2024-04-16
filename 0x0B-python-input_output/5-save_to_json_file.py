#!/usr/bin/python3
"""Defines a JSON file-writning a function."""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
