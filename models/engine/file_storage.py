#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def get(self, cls, id):
        """returns the object of class cls and id == id & None
        if not found """
        # check that class is a valid class
        if cls in classes.values():
            obj_key = '{}.{}'.format(cls.__name__, id)
        elif cls in classes.keys():
            obj_key = '{}.{}'.format(cls, id)
            # print('cls in class.keys -> {}'.format(obj_key))
        else:
            return None  # invalid class
        # check for an object with key = cls.id
        for key, value in self.__objects.items():
            if key == obj_key:
                return value
        return None

    def count(self, cls=None):
        """returns the number of objects of a cls class in storage
        if defined and number of all objects if cls is undefined """
        if cls is None:
            return len(self.__objects.keys())
        else:
            count = 0
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    count += 1
            return count

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
<<<<<<< HEAD
        except Exception:
=======
        except Exception as e:
>>>>>>> 1042330aa0a4a27ec0b41ed3b05f8d8c54075e8a
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
                # save after changes
                self.save()

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
<<<<<<< HEAD
        self.reload()

    def get(self, cls, id):
        """Retrieve one object"""
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """Count in storage the number of objects"""
        all_class = classes.values()

        if not cls:
            count = 0
            for item in all_class:
                count += len(models.storage.all(item).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
=======
        self.reload()
>>>>>>> 1042330aa0a4a27ec0b41ed3b05f8d8c54075e8a
