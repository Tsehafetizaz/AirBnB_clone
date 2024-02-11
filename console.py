#!/usr/bin/python
"""
Console module to handle command line interactions.
"""

import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def split_curly_braces(e_arg):
    """
    Splits the argument string at curly braces for update method parsing.

    Args:
        e_arg (str): The argument string containing potential curly braces.

    Returns:
        tuple: The ID and a dictionary of attribute-value pairs if curly
               braces are found, or a modified version of `e_arg` otherwise.
    """
    curly_braces = re.search(r"\{(.*?)\}", e_arg)
    if curly_braces:
        id_with_comma = shlex.split(e_arg[:curly_braces.span()[0]])
        obj_id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return obj_id, arg_dict
    else:
        commands = e_arg.split(",")
        if commands:
            obj_id = commands[0]
            attr_name = commands[1] if len(commands) > 1 else ""
            attr_value = commands[2] if len(commands) > 2 else ""
            return obj_id, f"{attr_name} {attr_value}"
