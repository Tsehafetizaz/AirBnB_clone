#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_help(self, arg):
        """List available commands with "help" or help with "help cmd"."""
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
