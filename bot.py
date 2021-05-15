import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller,Button
import pynput.mouse 
from time import sleep

mouse = Controller()
newMessage = True

class WhatsAppBot:
    def __init__(self,speed=0.5,clickSpeed=0.3):
        self.speed = speed
        self.clickSpeed=clickSpeed
        self.message = ''
        self.lastMessage = ''
        
    #Opening new message
    def checkNewMessage(self):   
        try:      
            postion = pt.locateOnScreen('greendot.png',confidence=0.9)
            pt.moveTo(postion[0:2],duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.clickSpeed)
            return True
        except Exception as e:
            print("Exception at greenDot:",e) 
            return False 
            
    def navInputBox(self):   
        try:      
            postion = pt.locateOnScreen('paperclip.png',confidence=0.9)
            pt.moveTo(postion[0:2],duration=self.speed)
            pt.moveRel(100,10,duration=self.speed)
            pt.doubleClick(interval=self.clickSpeed)
        except Exception as e:
            print("Exception at navInputBox:",e) 
             
    def locateMessage(self):   
        try:      
            postion = pt.locateOnScreen('paperclip.png',confidence=0.9)
            pt.moveTo(postion[0:2],duration=self.speed)
            pt.moveRel(60,-50,duration=self.speed)
        
        except Exception as e:
            print("Exception at locateMessage",e)  
            
    def noNewMsg(self):   
        try:      
            postion = pt.locateOnScreen('cancel.png',confidence=0.9)
            pt.moveTo(postion[0:2],duration=self.speed)
            pt.click(interval=self.speed)
        
        except Exception as e:
            print("Exception at locateMessage",e)  
            
    def getMessage(self):   
        try:      
            pt.tripleClick(interval=self.clickSpeed)
            sleep(1)
            pt.rightClick(interval=self.clickSpeed)
            pt.moveRel(30,-100,duration=self.speed)
            pt.click(interval=self.speed)
            sleep(1)
            
            self.message = pc.paste()
            print("Message is : ",self.message)
            
        except Exception as e:
            print("Exception at getMessage",e)  
            
    def sendMessage(self):   
        try: 
            message = "Good Evening from Chethans's personal chatBot!"
            if self.message != self.lastMessage :  
                self.navInputBox()
                pt.typewrite(message,interval=0.1)  
                pt.typewrite('\n')
                print("Message is : ",message)
                self.lastMessage = self.message
            else:
                print("No new messages!")
                
        except Exception as e:
            print("Exception at sendMessage",e)  
            
bot = WhatsAppBot(speed=0.5,clickSpeed=0.4)   
       
while newMessage:                      
    sleep(3)
    newMessage = bot.checkNewMessage()
    if newMessage:
        bot.noNewMsg()
        bot.locateMessage()
        bot.getMessage()
        bot.sendMessage()
    else:
        exit(0)   
       
        
        