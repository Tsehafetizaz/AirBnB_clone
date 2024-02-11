#!/usr/bin/python3
"""Console module for the HBNBCommand interpreter."""
import cmd
from models import storage, classes
from models.base_model import BaseModel
from models.user import User
# Add other model imports here if needed


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = '(hbnb) '
    class_names = ["BaseModel", "User"]  # Add other class names as needed

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
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.class_names:
            print("** class doesn't exist **")
            return
        instance = eval(arg)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        if arg and arg not in self.class_names:
            print("** class doesn't exist **")
            return
        obj_list = []
        for key, value in storage.all().items():
            if not arg or arg == key.split('.')[0]:
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] in classes:
            instance = classes[args[0]]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **") == '__main__':


if __name__ == '__main__':
    HBNBCommand().cmdloop()
