import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

# Mouse Click event
mouse = Controller()

#Instruction for our WhatsApp bot
class WhatsApp:
    def __init__(self,speed=.5,click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
    
    # Navigate to the green dots for new messages
    def nav_green_dot(self):
        print("Hello")
        try:
            position = pt.locateOnScreen('green_dot.png',confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
        except Exception as e:
            print('Exception (nav_green_dot): ')
   
        
    
