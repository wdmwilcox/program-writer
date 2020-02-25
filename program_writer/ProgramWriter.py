from time import sleep
import keyboard
import os

from Programs import programs

class ProgramWriter(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def reset(self):
        #directory = os.getcwd()
        os.remove(self.file_name)

    def open_notepad(self):
        keyboard.send('left windows')
        sleep(1)
        keyboard.write('notepad++')
        sleep(1)
        keyboard.send('enter')
        sleep(1)
        return None
    
    def new_file_and_save(self):
        keyboard.send('ctrl+n')
        sleep(2)
        keyboard.send('ctrl+alt+s')
        sleep(1)
        keyboard.write(self.file_name)
        sleep(1)
        keyboard.send('enter')
        sleep(1)
        return None
        
    def type_program(self):
        for character in programs.get(self.file_name):
            keyboard.send(character) 
            sleep(0.2)       
        sleep(1)
        keyboard.send('ctrl+s')
        sleep(1)
        keyboard.send('ctrl+w')
        sleep(1)
        return None

    def open_cmd(self):
        keyboard.send('left windows')
        sleep(1)
        keyboard.write('cmd')
        sleep(1)
        keyboard.send('enter')
        sleep(1)
        return None

    def execute_program(self):
        keyboard.write(f"python {self.file_name}")
        sleep(1)
        keyboard.send('enter')
        sleep(1)
        return None

    def close_cmd(self):
        keyboard.write("exit")
        sleep(1)
        keyboard.send('enter')
        sleep(1)
        return None

    def run(self):
        try:
            self.reset()
        except:
            print("File Not Found")
        self.open_notepad()
        self.new_file_and_save()
        self.type_program()
        self.open_cmd()
        self.execute_program()
        self.close_cmd()
        

