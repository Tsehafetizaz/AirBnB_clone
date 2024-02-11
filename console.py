#!/usr/bin/python3
"""Console module for the HBNBCommand interpreter."""

import cmd
from models import storage, classes


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance, saves it, and prints the id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] in classes:
            instance = classes[args[0]]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] in classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] in classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = arg.split()
        obj_list = []
        if not arg or args[0] in classes:
            for key, value in storage.all().items():
                if not arg or args[0] == key.split('.')[0]:
                    obj_list.append(str(value))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] in classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], args[2], args[3].strip('"'))
            storage.all()[key].save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
