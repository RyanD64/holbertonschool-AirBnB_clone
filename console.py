#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """"""
        if not line:
            raise SyntaxError("class name missing")

    def do_show(self, line):
        """"""
        if not line:
            raise SyntaxError("class name missing")
        if id is not line:
            raise 
    def do_destroy(self, line):
        """"""

    def do_all(self, line):
        """"""

    def do_update(self, line):
        """"""

    def do_empty_line(self):
        pass

    def do_quit(self, line):
        """"""
        return True
    
    def do_EOF(self, line):
        """"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()