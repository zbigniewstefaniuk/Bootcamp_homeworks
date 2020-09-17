# standard library imports
import os 
import subprocess 
import sys
import socket 
import platform 

from time import sleep
import socket

"""
This Script requires the user to provide 3 arguments when calling from a terminal:
1 - Select the system command (Ping, ipconfig, system info)
2 - Enter path to file (text or Python file)
3 - Type name of the environmental variable

Script will check what type of file is the file to which the path is given.
If it is a python file, the script will run it and if it is a text file, it will display the first line of the text.
If the file does not exist, an exception will be called and information about it will be printed.
If the task is successful, the script will set the FILE_FLAG flag to True

The script will then check if there is an environment variable with the name given by the user.
If so, the script will retrieve its value if it does not exist, create it and set it value to "DONE" and set the ENV_FLAG flag to True

If both flags are True, the script will extract information about the system and user name and inform the user that
in a moment the command which he has chosen in the introduction to the script will be run on this system.

Translated with www.DeepL.com/Translator (free version)
"""


class UserApp:

    def __init__(self, file_path: str):
        self.file_path = file_path                  # variable for user input path
        self.exist = os.path.exists(self.file_path)  # checking if path exist
        self.isfile = os.path.isfile(self.file_path)  # checking if file exist
        self.extension = os.path.splitext(file_path)

        self.hostname = socket.gethostname()
        self.maschine_name = platform.system()

        self.file_flag = False
        self.env_flag = False

        self.choices = {
            "1": self.cmd_ping,
            "2": self.cmd_ipconfig,
            "3": self.cmd_systeminfo,
            "4": self.exit_app
        }

        self.run()

    def display_menu(self):
        print("""
    AVAILABLE CMD OPTIONS
1: Ping http://google.com/
2: Windows IP Configuration
3: Getting System Information
4: Exit
                """)

    def run(self):
        """
        this function is a loop, dispaying menu
        and it's looping until user choose one of provided options
        """
        flag_menu = True
        while flag_menu:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:  # This checking if user input is corrent it pass trough
                self.file_check()
                flag_menu = False
                if self.file_flag and self.env_flag:
                    print(
                        f'Okay {self.hostname} Now your {self.maschine_name} will run command you choose in CMD MENU :)')
                    action()

            else:
                print("You have to select either 1, 2, 3 or 4")
                print(f'{choice} Please try again')

    def file_check(self):
        """"
            This function is checking if the path and file exist,
            if so, it's checking extension of given file.

            For .py extension - app is executing python script
            for .txt extension - app is reading only first line
        """
        if self.exist is True or self.isfile is True:
            print(f'Checking file: {self.file_path} \n')

            if self.extension[1] == '.py':
                print(f'Running "{self.file_path}" - as Python file')
                task = subprocess.Popen(["Python3", f"{user_path}"])
                print('Done!')
                self.file_flag = True

            elif self.extension[1] == '.txt':
                with open(self.file_path, 'r+', encoding='utf-8') as f:
                    print(f'First line of text file is: \n\n{f.readline()}')
                    print('Done!')
                    self.file_flag = True

            else:
                raise Exception(
                    'Could not read format of the file, choose diffrent file\n')
            # after succes of function above it will start next one that checks enviroments Variable
            self.env_check()
        else:
            print(f'{self.file_path}\nSorry, path does not exist!')

    def env_check(self):
        user_enviros_input = input(
            'Please type name of the environ, you looking for: ')
        if user_enviros_input is True:
            print('I found it!')
            system_environ_finder = os.environ.get(user_enviros_input)
            print(f'{system_environ_finder} \n')
        else:
            print(
                f'Program could not find "{user_enviros_input}" variable so creates it')
            os.environ[user_enviros_input] = 'DONE'
        self.env_flag = True

    def cmd_ping(self):
        print('Okay! I\'m pinging google.com\n')
        task = subprocess.Popen("ping google.com")
        sleep(4)  # not the best way to do this but it works !
        print('Done!')

    def cmd_ipconfig(self):
        print('Okay! I\'m checking Windows IP Configuration\n')
        task = subprocess.Popen("ipconfig")
        print('Done!')

    def cmd_systeminfo(self):
        print('Okay! I\'m getting systemInfo\n')
        task = subprocess.Popen("systeminfo")
        sleep(3)  # not the best way to do this but it works !
        print('Done!')

    def exit_app(self):
        print("Thank you for testing my code, bye.")
        sys.exit(0)


if __name__ == '__main__':
    user_path = input(r'Paste yor file path here > ')
    app = UserApp(user_path)
