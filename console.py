#!/usr/bin/python3
import cmd,sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_create(self,arg):
        """ reates a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        """ Exit the console and commit all changes"""
        return True
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    