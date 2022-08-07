#!/usr/bin/python3
"""HBNBCommand module"""
import sys
import shlex
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = '(hbnb) '
    methods = ['all', 'show', 'count', 'update', 'destroy']
    classes = [
        'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

    def precmd(self, line):
        """Implement custom commands"""

        if line == '' or not line.endswith(')'):
            return line

        flag = 1

        for x in self.classes:
            for y in self.methods:
                if line.startswith("{}.{}(".format(x, y)):
                    flag = 0
        if flag:
            return line

        tmp = ''
        for x in self.methods:
            tmp = line.replace('(', '.').replace(')', '.').split('.')
            if tmp[0] not in self.classes:
                return ' '.join(tmp)
            while tmp[-1] == '':
                tmp.pop()
            if len(tmp) < 2:
                return line
            if len(tmp) == 2:
                tmp = '{} {}'.format(tmp[1], tmp[0])
            else:
                tmp = '{} {} {}'.format(tmp[1], tmp[0], tmp[2])
            if tmp.startswith(x):
                return tmp

        return ''

    def emptyline(self):
        """Overrides default empty line behavior so no command is executed"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = eval("{}()".format(args[0]))
            print(obj.id)
            models.storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                objs.pop(key)
                del obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based on class"""
        args = parse(line)
        objs = models.storage.all()
        obj_list = []
        if len(args) >= 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, obj in objs.items():
                    if key.startswith(args[0]):
                        obj_list.append(obj.__str__())
                print(obj_list)
        else:
            for obj in objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id and attr name"""
        args = parse(line)
        objs = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    try:
                        eval(args[3])
                    except (SyntaxError, NameError):
                        args[3] = "'{}'".format(args[3])
                    setattr(obj, args[2], eval(args[3]))
                    obj.save()
            except KeyError:
                print("** no instance found **")


def parse(line):
    """Parses a given string, and returns a list"""
    return shlex.split(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
