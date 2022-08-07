#!/usr/bin/python3
"""
    Console module
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import re


class HBNBCommand(cmd.Cmd):
    """
        Console
    """
    prompt = "(hbnb) "
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]
    __commands = ['all', 'count', 'create', 'destroy', 'show']

    def emptyline(self):
        pass

    def do_create(self, prmArg):
        """
            Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id.
        """
        try:
            if not prmArg:
                raise ValueError("** class name missing **")

            args = prmArg.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")

            instance = eval(args[0])()
            storage.save()
            print(instance.id)
        except Exception as exception:
            print(exception.args[0])

    def do_show(self, prmArgs):
        """
            Prints the string representation of an instance based on the
            class name and id.
        """
        try:
            if not prmArgs:
                raise ValueError("** class name missing **")

            args = prmArgs.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")
            if len(args) == 1:
                raise ValueError("** instance id missing **")

            dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dict:
                raise ValueError("** no instance found **")

            print(dict[key])
        except Exception as exception:
            print(exception.args[0])

    def do_all(self, prmArg):
        """
            Prints all string representation of all instances based or not
            on the class name.
        """
        try:
            list = []

            args = prmArg.split()

            if args and args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")

            for key, value in storage.all().items():
                if (not args or args[0] is None or
                        args[0] == type(value).__name__):
                    list.append(str(value))

            print(list)
        except Exception as exception:
            print(exception.args[0])

    def do_destroy(self, prmArgs):
        """
            Deletes an instance based on the class name and id (save the change
            into the JSON file).
        """
        try:
            if not prmArgs:
                raise ValueError("** class name missing **")

            args = prmArgs.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")
            if len(args) == 1:
                raise ValueError("** instance id missing **")

            dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dict:
                raise ValueError("** no instance found **")

            del dict[key]
            storage.save()
        except Exception as exception:
            print(exception.args[0])

    def do_update(self, prmArgs):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
        """
        try:
            if not prmArgs:
                raise ValueError("** class name missing **")

            args = prmArgs.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")
            if len(args) == 1:
                raise ValueError("** instance id missing **")

            dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in dict:
                raise ValueError("** no instance found **")
            obj = dict[key]

            if len(args) == 2:
                raise ValueError("** attribute name missing **")
            if len(args) == 3:
                raise ValueError("** value missing **")

            className, command, attribute, value = args

            if attribute not in ("id", "created_at", "updated_at"):
                setattr(obj, attribute, self.__type(value))
                storage.save()
        except Exception as exception:
            print(exception.args[0])

    def do_count(self, prmArg):
        """
            Update your command interpreter (console.py) to retrieve the number
            of instances of a class.
        """
        try:
            count = 0
            if not prmArg:
                raise ValueError("** class name missing **")

            args = prmArg.split()

            if args[0] not in self.__classes:
                raise ValueError("** class doesn't exist **")

            for key, value in storage.all().items():
                if args[0] is None or args[0] == type(value).__name__:
                    count += 1

            print(count)
        except Exception as exception:
            print(exception.args[0])

    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def help_create(self):
        print("Creates a new instance of BaseModel, \
saves it (to the JSON file) and prints the id.\n")

    def help_show(self):
        print("Prints the string representation of \
an instance based on the class name and id.\n")

    def help_all(self):
        print("Prints all string representation of \
all instances based or not on the class name.\n")

    def help_destroy(self):
        print("Deletes an instance based on the \
class name and id (save the change into the JSON file).\n")

    def help_update(self):
        print("Updates an instance based on the \
class name and id by adding or updating attribute (save the \
change into the JSON file).\n")

    def help_count(self):
        print("Update your command interpreter \
(console.py) to retrieve the number of instances of a class.\n")

    def default(self, line: str) -> bool:
        """
            Called when command prefix is not recognized in order
            to verify and catch or not the adequate function.
        """
        try:
            if self.__checkValidArguments(line):
                clName, cmd, args = self.__getArgumentsFromLine(line)
                if self.__checkValidCommand(cmd):
                    args = self.__cleanArguments(args)
                    formattedCommand = self.__buildCommand(clName, cmd, args)
                    eval(formattedCommand)
                    return
                elif (cmd == 'update'):
                    parameters = self.__getParametersFromArguments(args)
                    id = self.__cleanArguments(parameters[0])
                    if self.__isValidJson(parameters[1]):
                        jsonString = parameters[1].replace("'", '"')
                        jsonData = json.loads(jsonString)
                        for attribute, value in jsonData.items():
                            args = "{} {} {}".format(id, attribute, value)
                            formattedCommand = self.__buildCommand(
                                clName,
                                cmd,
                                args
                            )
                            eval(formattedCommand)
                        return
                    else:
                        args = self.__cleanArguments(args)
                        formattedCommand = self.__buildCommand(
                            clName,
                            cmd,
                            args
                        )
                        eval(formattedCommand)
                    return
        except:
            return super().default(line)

    def __getArgumentsFromLine(self, prmLine):
        """
            return argument from command line
        """
        regex = "^(.*)\.(.*)\((.*)\)$"
        regex_prog = re.compile(regex)
        results = regex_prog.findall(prmLine)
        arguments = results[0]

        return arguments

    def __isValidJson(self, prmString: str) -> bool:
        """
            check if a string is valid json
        """
        prmString = prmString.replace("'", '"')
        try:
            json_object = json.loads(prmString)
        except ValueError as e:
            return False
        return True

    def __getParametersFromArguments(self, prmArguments):
        """
            return parameter from argument
        """
        try:
            regex = "^\"(.*)\"((,? ?)(\{.*\}))?$"
            regex_prog = re.compile(regex)
            results = regex_prog.findall(prmArguments)
            parameters = results[0]

            return parameters[0], parameters[3]
        except:
            return '', ''

    def __checkValidArguments(self, prmLine: str) -> bool:
        """
            check argument's validity
        """
        arguments = self.__getArgumentsFromLine(prmLine)

        if arguments and not arguments[0]:
            print("** class name missing **")
        elif arguments and arguments[0] not in self.__classes:
            print("** class doesn't exist **")

        return (arguments and arguments[0] in self.__classes and
                len(arguments) == 3)

    def __checkValidParameters(self, prmArguments, prmClassName) -> bool:
        parameters = self.__getParametersFromArguments(prmArguments)

        if not parameters or not parameters[0]:
            print("** instance id missing **")
            return False
        else:
            key = "{}.{}".format(prmClassName, parameters[0])
            if key not in storage.all():
                print("** no instance found **")
                return False

        return True if parameters else False

    def __checkValidCommand(self, prmCommand: str) -> bool:
        """
            check command validity
        """
        return prmCommand in self.__commands

    def __cleanArguments(self, prmArguments) -> str:
        """
            clean arguments
        """
        prmArguments = prmArguments.replace(", ", " ")
        prmArguments = prmArguments.replace(",", " ")
        prmArguments = prmArguments.replace('"', "")

        return prmArguments

    def __buildCommand(self, prmClassName, prmCommand, prmArguments):
        """
            build command
        """
        if len(prmArguments) > 0:
            arguments = "{} {}".format(prmClassName, prmArguments)
        else:
            arguments = "{}".format(prmClassName)

        return "self.do_{}(\"{}\")".format(prmCommand, arguments)

    def __type(self, prmStr: str):
        try:
            return int(prmStr)
        except:
            try:
                return float(prmStr)
            except:
                return str(prmStr).replace('"', "").replace("'", "")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
