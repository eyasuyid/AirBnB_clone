#!/usr/bin/python3


from os import system
from models.engine.file_storage import FileStorage
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import os


class ConsolePromptingTest(unittest.TestCase):

    def testPrompt(self):
        """
            Prompt command
        """
        self.assertEqual(HBNBCommand().prompt,
                         "(hbnb) ")

    def testEmptyLine(self):
        """
            Empty line
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual(output.getvalue().strip(), "")


class ConsoleHelpTest(unittest.TestCase):
    def testHelpCreate(self):
        """
            create() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Creates a new instance of BaseModel, \
saves it (to the JSON file) and prints the id.\n\n")

    def testHelpAll(self):
        """
            all() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Prints all string representation of \
all instances based or not on the class name.\n\n")

    def testHelpDestroy(self):
        """
            destroy() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Deletes an instance based on the \
class name and id (save the change into the JSON file).\n\n")

    def testHelpUpdate(self):
        """
            update() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Updates an instance based on the \
class name and id by adding or updating attribute (save the \
change into the JSON file).\n\n")

    def testHelpShow(self):
        """
            show() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Prints the string representation of \
an instance based on the class name and id.\n\n")

    def testHelpQuit(self):
        """
            quit have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(),
                             "Quit command to exit the program\n\n")

    def testHelpEOF(self):
        """
            EOF command have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(),
                             "EOF command to exit the program\n\n")

    def testHelpCount(self):
        """
            count() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help count")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Update your command interpreter \
(console.py) to retrieve the number of instances of a class.\
\n\n")


class ConsoleExitTest(unittest.TestCase):

    def testDoQuit(self):
        """
            Quit
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def testDoEOF(self):
        """
            EOF
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("EOF")


class ConsoleAllTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testAllInvalidClass(self):
        """
            all invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.all()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testAllMissingClass(self):
        """
            all() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(".all()")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testAllInstanceSpaceNotation(self):
        """
            all instance command
        """
        self.__allInstanceSpaceNotation("Amenity", "User")
        self.__allInstanceSpaceNotation("BaseModel", "User")
        self.__allInstanceSpaceNotation("City", "User")
        self.__allInstanceSpaceNotation("Place", "User")
        self.__allInstanceSpaceNotation("Review", "User")
        self.__allInstanceSpaceNotation("State", "User")
        self.__allInstanceSpaceNotation("User", "BaseModel")

    def testAllInstanceDotNotation(self):
        """
            all() instance command
        """
        self.__allInstanceDotNotation("Amenity", "User")
        self.__allInstanceDotNotation("BaseModel", "User")
        self.__allInstanceDotNotation("City", "User")
        self.__allInstanceDotNotation("Place", "User")
        self.__allInstanceDotNotation("Review", "User")
        self.__allInstanceDotNotation("State", "User")
        self.__allInstanceDotNotation("User", "BaseModel")

    def __allInstanceSpaceNotation(self, prmClassName, prmOtherClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        id = output.getvalue()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "all {}".format(prmClassName)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertIn(prmClassName, output.getvalue().strip())
            self.assertNotIn(prmOtherClassName, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __allInstanceDotNotation(self, prmClassName, prmOtherClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        id = output.getvalue()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "{}.all()".format(prmClassName)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertIn(prmClassName, output.getvalue().strip())
            self.assertNotIn(prmOtherClassName, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))


class ConsoleCountTest(unittest.TestCase):
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testCountMissingClass(self):
        """
            count() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("count")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testCountInvalidClass(self):
        """
            count() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("count toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testCountInstanceSpaceNotation(self):
        """
            count instance command.
        """
        for className in self.__classes:
            self.__testCountSpaceNotation(className)

    def testCountInstanceDotNotation(self):
        """
            count() instance command.
        """
        for className in self.__classes:
            self.__testCountDotNotation(className)

    def __testCountSpaceNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "count {}".format(prmClassName)))
        count = int(output.getvalue())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        id = output.getvalue()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "count {}".format(prmClassName)))
            self.assertEqual(output.getvalue().strip(), str(count + 1))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __testCountDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.count()".format(prmClassName)))
        count = int(output.getvalue())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        id = output.getvalue()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.count()".format(prmClassName)))
            self.assertEqual(output.getvalue().strip(), str(count + 1))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))


class ConsoleCreateTest(unittest.TestCase):
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testCreateMissingClass(self):
        """
            create() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testInvalidClass(self):
        """
            create() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testCreateInstance(self):
        """
            create() Amenity
        """
        for prmClassName in self.__classes:
            self.__testCreateObject(prmClassName)

    def __testCreateObject(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
            key = "{}.{}".format(prmClassName, id)
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))


class ConsoleDestroyTest(unittest.TestCase):
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testDestroyMissingClass(self):
        """
            destroy() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(".destroy()")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testDestroyInvalidClass(self):
        """
            destroy() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.destroy()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testDestroyMissingIdSpaceNotation(self):
        """
            destroy missing id command
        """
        for className in self.__classes:
            self.__missingIdSpaceNotation(className)

    def testDestroyMissingIdDotNotation(self):
        """
            destroy() missing id command
        """
        for className in self.__classes:
            self.__missingIdDotNotation(className)

    def testDestroyNoInstanceFoundSpaceNotation(self):
        """
            destroy no instance command
        """
        for className in self.__classes:
            self.__noInstanceFoundSpaceNotation(className)

    def testDestroyNoInstanceFoundDotNotation(self):
        """
            destroy() no instance command
        """
        for className in self.__classes:
            self.__noInstanceFoundDotNotation(className)

    def testDestroyInstanceSpaceNotation(self):
        """
            destroy instance command
        """
        for className in self.__classes:
            self.__destroyInstanceSpaceNotation(className)

    def testDestroyInstanceDotNotation(self):
        """
            destroy() instance command
        """
        for className in self.__classes:
            self.__destroyInstanceDotNotation(className)

    def __missingIdSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "destroy {}".format(prmClassName)))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def __missingIdDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy()".format(prmClassName)))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def __noInstanceFoundSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "destroy {} 1".format(prmClassName)))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def __noInstanceFoundDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy(1)".format(prmClassName)))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def __destroyInstanceSpaceNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "destroy {} {}".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def __destroyInstanceDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "{}.destroy({})".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def __getObj(self, prmClassName: str, prmUuid: str):
        return storage.all()["{}.{}".format(prmClassName, prmUuid)]


class ConsoleShowTest(unittest.TestCase):
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testShowMissingClass(self):
        """
            show() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testInvalidClass(self):
        """
            show() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.show()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testMissingIdSpaceNotation(self):
        """
            show missing id command
        """
        for className in self.__classes:
            self.__missingIdSpaceNotation(className)

    def testMissingIdDotNotation(self):
        """
            show() missing id command
        """
        for className in self.__classes:
            self.__missingIdDotNotation(className)

    def testNoInstanceFoundSpaceNotation(self):
        """
            show no instance command
        """
        for className in self.__classes:
            self.__noInstanceFoundSpaceNotation(className)

    def testNoInstanceFoundDotNotation(self):
        """
            show() no instance command
        """
        for className in self.__classes:
            self.__noInstanceFoundDotNotation(className)

    def testShowInstanceSpaceNotation(self):
        """
            show instance command
        """
        for className in self.__classes:
            self.__showInstanceSpaceNotation(className)

    def testShowInstanceDotNotation(self):
        """
            show() instance command
        """
        for className in self.__classes:
            self.__showInstanceDotNotation(className)

    def __missingIdSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "show {}".format(prmClassName)))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def __missingIdDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.show()".format(prmClassName)))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def __noInstanceFoundSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "show {} 1".format(prmClassName)))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def __noInstanceFoundDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.show(1)".format(prmClassName)))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def __showInstanceSpaceNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "show {} {}".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __showInstanceDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            command = "{}.show({})".format(prmClassName, id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "destroy {} {}".format(prmClassName, id)))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __getObj(self, prmClassName: str, prmUuid: str):
        return storage.all()["{}.{}".format(prmClassName, prmUuid)]


class ConsoleUpdateTest(unittest.TestCase):
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testShowMissingClass(self):
        """
            update() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testInvalidClass(self):
        """
            update() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.update()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testMissingIdSpaceNotation(self):
        """
            update missing id command
        """
        for className in self.__classes:
            self.__missingIdSpaceNotation(className)

    def testMissingIdDotNotation(self):
        """
            update() missing id command
        """
        for className in self.__classes:
            self.__missingIdDotNotation(className)

    def testNoInstanceFoundSpaceNotation(self):
        """
            update no instance command
        """
        for className in self.__classes:
            self.__noInstanceFoundSpaceNotation(className)

    def testNoInstanceFoundDotNotation(self):
        """
            update() no instance command
        """
        for className in self.__classes:
            self.__noInstanceFoundDotNotation(className)

    def testMissingAttributeSpaceNotation(self):
        """
            update() no instance command
        """
        for className in self.__classes:
            self.__missingAttributeSpaceNotation(className)

    def testMissingAttributeDotNotation(self):
        """
            update() no instance command
        """
        for className in self.__classes:
            self.__missingAttributeDotNotation(className)

    def testUpdateInstanceSpaceNotation(self):
        """
            update no instance command
        """
        for className in self.__classes:
            self.__updateInstanceSpaceNotation(className)

    def testUpdateInstanceDotNotation(self):
        """
            update() no instance command
        """
        for className in self.__classes:
            self.__updateInstanceDotNotation(className)
            self.__updateInstanceWithJSONDotNotation(className)

    def __missingIdSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "update {}".format(prmClassName)))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def __missingIdDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.update()".format(prmClassName)))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def __noInstanceFoundSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "update {} 1".format(prmClassName)))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def __noInstanceFoundDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.update(1)".format(prmClassName)))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def __missingAttributeSpaceNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
            obj = self.__getObj(prmClassName, id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "update {} {}".format(prmClassName, id)))
            self.assertEqual("** attribute name missing **",
                             output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __missingAttributeDotNotation(self, prmClassName: str):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
            obj = self.__getObj(prmClassName, id)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.update(\"{}\")".format(prmClassName, id)))
            self.assertEqual("** attribute name missing **",
                             output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __updateInstanceSpaceNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            self.assertNotIn("first_name", obj.__dict__.keys())
            command = "update {} {} {} {}".format(
                prmClassName, id, "first_name", "john")
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.first_name, "john")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __updateInstanceDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
<<<<<<< HEAD
            obj = self.__getObj(prmClassName, id)
=======
[O            obj = self.__getObj(prmClassName, id)
>>>>>>> tasks
            self.assertNotIn("first_name", obj.__dict__.keys())
            command = "{}.update(\"{}\", \"{}\", \"{}\")".format(
                prmClassName, id, "first_name", "john")
            self.assertFalse(HBNBCommand().onecmd(command))
            obj = self.__getObj(prmClassName, id)
            self.assertIn("first_name", obj.__dict__.keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __updateInstanceWithJSONDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = self.__getObj(prmClassName, id)
            self.assertNotIn("first_name", obj.__dict__.keys())
            jsonData = "{'first_name': 'john'}"
            command = "{}.update(\"{}\", {})".format(
                prmClassName, id, jsonData)
            self.assertFalse(HBNBCommand().onecmd(command))
            obj = self.__getObj(prmClassName, id)
            self.assertIn("first_name", obj.__dict__.keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __getObj(self, prmClassName: str, prmUuid: str):
        return storage.all()["{}.{}".format(prmClassName, prmUuid)]
