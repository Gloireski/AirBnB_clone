#!/usr/bin/python3
import cmd
""" this is the command prompte file
that contains storage engine commands
"""
class Console(cmd.Cmd):
    ''' this is the console class'''
    prompt = '(hbnb) '

    def do_craeteUser(self, arg):
        ''' create a new User'''
        if not arg:
            print("Please provide a new user. ")
            return
        User = arg
        try:
            print(f"new user'{User}' created successfully.")
        except Exception as e:
            print(f"Error creating the new user")

    def do_craetePlace(self, arg):
        ''' create a new place'''
        if not arg:
            print("Please provide a new place. ")
            return
        Place = arg
        try:
            print(f"new place'{Place}' created successfully.")
        except Exception as e:
            print(f"Error creating the new place")

   def do_quit(self, arg):
        '''Quit the command-line interpreter'''
        print("Quitting...")
        return True
if __name__ == '__main__':
    Console().cmdloop()
