#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """create the commands for the HBNB console"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """create class"""
        if not line:
            raise SyntaxError("class name missing")

    def do_show(self, line):
        """show class"""
        if not line:
            raise SyntaxError("class name missing")
        if id is not line:
            raise 
    def do_destroy(self, line):
        """destroy class"""

    def do_all(self, line):
        """show all classes"""

    def do_update(self, line):
        """update class"""

    def do_empty_line(self):
        """print an empty line"""
        pass

    def do_quit(self, line):
        """quit the console"""
        return True
    
    def do_EOF(self, line):
        """End of file"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()