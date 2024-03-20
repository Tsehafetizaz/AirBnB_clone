#!/usr/bin/python3
"""
This module defines the HolbertonBnB command interpreter.
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex  # for splitting the line into arguments


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        'Do nothing on empty input line'
        pass

    def do_create(self, arg):
        'Creates a new instance of BaseModel'
        if not arg:
            print("** class name missing **")
            return
        try:
            args = shlex.split(arg)
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            new_instance = eval(args[0])()
            for param in args[1:]:
                if "=" not in param:
                    continue
                key, value = param.split("=", 1)
                value = value.strip('"').replace('_', ' ')
                if hasattr(new_instance, key):
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        pass
                    setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    # ... existing methods ...

    # Additional methods will go here


if __name__ == '__main__':
    HBNBCommand().cmdloop()
