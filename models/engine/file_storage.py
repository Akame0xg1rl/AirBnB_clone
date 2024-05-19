import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of serialized instances."""
        return self.__objects

    def new(self, obj):
        """Sets an instance in __objects with the key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                try:
                    serialized_objects = json.load(f)
                    for key, value in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        if class_name == "BaseModel":
                            self.__objects[key] = BaseModel(**value)
                        elif class_name == "User":
                            self.__objects[key] = User(**value)
                except Exception as e:
                    print(f"Error: {e}")

