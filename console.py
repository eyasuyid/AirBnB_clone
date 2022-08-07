#!/usr/bin/python3
"""HBNBCommand module"""
import sys
import shlex
import re
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
        # TODO: add error mgmt for class (missing, valid), id, attribute, value
        if line == '' or not line.endswith(')'):
            return line

        cmd_split = line.split('.', 1)

        if len(cmd_split) < 2:
            print('double check split')
            for cls in self.classes:
                if cls in cmd_split:
                    print('class found:', cls)
                    continue
            print("** class name missing **")
            return ''

        cls = cmd_split[0]
        cmdrgx = re.compile("(a?[^(]+)")
        command = cmdrgx.findall(cmd_split[1])[0]
        options = cmd_split[1].split(command)[1]

        if command == 'all':
            return "{} {}".format(command, cls)

        objs = models.storage.all()
        if command == 'count':
            #print('use all() to count, add validation')
            count = 0
            for key in objs.keys():
                if key.startswith(cls):
                    count += 1
            print(count)
            return ''

        if command == 'show' or command == 'destroy':
            inst_id = eval(options)
            if len(inst_id) == 0:
                inst_id = ''
            return "{} {} {}".format(command, cls, inst_id)

        if command == 'update':
            opt_tup = eval(options)
            inst_id = opt_tup[0]
            if type(opt_tup[1]) is dict:
                obj_dict = opt_tup[1]
                key = '{}.{}'.format(cls, inst_id)
                try:
                    obj = objs[key]
                    for name, value in obj_dict.items():
                        setattr(obj, name, value)
                    models.storage.save()
                    return ''
                except KeyError:
                    print("** no instance found **")
                    return ''

            return "{} {} {} {} {}".format(
                command, cls, inst_id, opt_tup[1], opt_tup[2])

        return line

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
