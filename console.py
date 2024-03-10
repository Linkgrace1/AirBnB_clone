#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import cmd
import shlex

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]


    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """

        pass

    def do_quit(self, arg):
        """
        Quit the program.

        """

        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("**) class name missing**")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exit **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    
    def do_show(self, arg):
        """
        show the string representation of an instance
        Usage: create <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        
        commands = shlex.split(arg)

        if len(comands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0],commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string that represents all instances or a specific class
        Usage: all [class_name]
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(comands) == 0:
            for key, value in objects.items():
                print(str(value))
            elif commands[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                for key, value in objects.items():
                    if key.split('.')[0] == commands[0]:
                        print(str(value))

    def do_update(self, arg):
        """
        update an instance by updating and adding an attribute.
        usage: update <class_name> <attribute_name> "<attribute_value
        """
        
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0],commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]

                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()


    def help_quit(self, arg):
        """
        help the command to exit a program

        """

        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
        Handle the End-of-File (ctrl+D) event to exit the program.

        """

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
