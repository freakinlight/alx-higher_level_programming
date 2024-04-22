#!/usr/bin/python3
""" Base Module """
import json

class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert list of dictionaries to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Convert JSON string to list of dictionaries """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a list of objects to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """ Load a list of objects from a file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                objs = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in objs]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ Create a new instance from a dictionary """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file_csv(cls):
        """ Load a list of objects from a CSV file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                objs = f.read()
                objs = objs.split('\n')[:-1]
                objs = [obj.split(',') for obj in objs]
                objs = [[int(x) for x in obj] for obj in objs]
                return [cls.create(*obj) for obj in objs]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save a list of objects to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is not None:
                list_csv = [','.join(map(str, obj.to_csv())) + '\n' for obj in list_objs]
                f.writelines(list_csv)
