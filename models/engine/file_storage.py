#!/usr/bin/python3
"""Define FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances

    Represents an abstracted storage enginr

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_data = obj_dict[key]
                    obj = eval(class_name)(**obj_data)
                    self.__objects[key] = obj
        except (FileNotFoundError, json.JSONDecodeError):
            pass

