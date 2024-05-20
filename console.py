#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Exit the program"
        return True

    def do_EOF(self, arg):
        "Exit the program"
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        "Create a new instance and print its id"
        if not arg:
            print("** class name missing **")
            return
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        "Show an instance based on class name and id"
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        print(storage.all()[args[0]][key])

    def do_destroy(self, arg):
        "Delete an instance based on class name and id"
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        storage.all()[args[0]].pop(key)
        storage.save()

    def do_all(self, arg):
        "Show all instances, or all instances of a class"
        args = arg.split()
        obj_list = []
        if args and args[0] in storage.all():
            for value in storage.all()[args[0]].values():
                obj_list.append(str(value))
        elif not args:
            for obj_dict in storage.all().values():
                for value in obj_dict.values():
                    obj_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        "Update an instance by adding or updating an attribute"
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[args[0]][key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
