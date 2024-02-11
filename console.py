#!/usr/bin/python3
"""
This module defines the HolbertonBnB command interpreter.
"""

import cmd
import re
from shlex import split

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parse an argument string.

    Args:
        arg (str): The argument string to parse.

    Returns:
        list: A list of arguments parsed from the string.
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            ret_list = [i.strip(",") for i in lexer]
            ret_list.append(brackets.group())
            return ret_list
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        ret_list = [i.strip(",") for i in lexer]
        ret_list.append(curly_braces.group())
        return ret_list


class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command interpreter class.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Override method to do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for invalid input."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict:
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of a given class."""
        arg_list = parse(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Display the string representation of an instance."""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        arg_list = parse(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Display all instances of a class, or all instances."""
        arg_list = parse(arg)
        if arg_list and arg_list[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = [
                obj.__str__() for obj in storage.all().values()
                if not arg_list or obj.__class__.__name__ == arg_list[0]
            ]

            print(obj_list)

    def do_count(self, arg):
        """Count the number of instances of a given class."""
        arg_list = parse(arg)
        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == arg_list[0])
        print(count)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        arg_list = parse(arg)
        obj_dict = storage.all()

        if not arg_list:
            print("** class name missing **")
            return False
        if arg_list[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False

        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            print("** value missing **")
            return False

        obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
        if len(arg_list) == 4:
            setattr(obj, arg_list[2], eval(arg_list[3]))
        elif type(eval(arg_list[2])) == dict:
            for k, v in eval(arg_list[2]).items():
                setattr(obj, k, v)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
