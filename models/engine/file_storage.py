#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models import base_model, amenity, city, place, review, state, user
from datetime import datetime

<<<<<<< HEAD
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}
=======
strptime = datetime.strptime
to_json = base_model.BaseModel.to_json
>>>>>>> da57e888f888f6bc03d221d8305a11f81c28c10c


class FileStorage:
    """handles long term storage of all class instances"""
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    """CNC - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """
    __file_path = './dev/file.json'
    __objects = {}

    def all(self, cls=None):
        """returns private attribute: __objects"""
        if cls:
            objects_dict = {}
            for class_id, obj in FileStorage.__objects.items():
                if type(obj).__name__ == cls:
                    objects_dict[class_id] = obj
            return objects_dict
        return FileStorage.__objects

    def new(self, obj):
        """sets / updates in __objects the obj with key <obj class name>.id"""
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[bm_id] = obj

    def get(self, cls, id):
        """
        gets specific object
        :param cls: class
        :param id: id of instance
        :return: object or None
        """
        all_class = self.all(cls)

        for obj in all_class.values():
            if id == str(obj.id):
                return obj

        return None

    def count(self, cls=None):
        """
        count of instances
        :param cls: class
        :return: number of instances
        """

        return len(self.all(cls))

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
<<<<<<< HEAD
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)
=======
        fname = FileStorage.__file_path
        d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w+', encoding='utf-8') as f_io:
            json.dump(d, f_io)
>>>>>>> da57e888f888f6bc03d221d8305a11f81c28c10c

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
<<<<<<< HEAD
            with open(self.__file_path, "r") as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
=======
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
>>>>>>> da57e888f888f6bc03d221d8305a11f81c28c10c
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            d.pop("__class__", None)
            d["created_at"] = datetime.strptime(d["created_at"],
                                                "%Y-%m-%d %H:%M:%S.%f")
            d["updated_at"] = datetime.strptime(d["updated_at"],
                                                "%Y-%m-%d %H:%M:%S.%f")
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)

    def delete(self, obj=None):
<<<<<<< HEAD
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
=======
        """deletes obj"""
        if obj is None:
            return
        for k in list(FileStorage.__objects.keys()):
            if obj.id == k.split(".")[1] and k.split(".")[0] in str(obj):
                FileStorage.__objects.pop(k, None)
                self.save()
>>>>>>> da57e888f888f6bc03d221d8305a11f81c28c10c

    def close(self):
        """
            calls the reload() method for deserialization from JSON to objects
        """
        self.reload()

    def get(self, cls, id):
        """Gets string representation of the class name and object ID"""
        string_dict = self.all(cls)
        for key, value in string_dict.items():
            if key == cls + "." + id:
                return value

    def count(self, cls=None):
        """count objects in the storage"""
        counter = 0
        if cls is not None:
            for key in self.__objects:
                counter += 1
        else:
            if cls is None:
                for key in self.__objects:
                    counter += 1
        return counter
