import sys
import pyautogui as pt
import pyperclip as pc
from pyarabic import araby
from pyarabic.araby import strip_diacritics
from PIL import Image
from time import sleep
from pynput.mouse import Controller, Button
from responses import responses
from recognition import *
"""
The program should answer these questions and do these tasks:
1-what is the message?
2-who send it?
3-is it appropriate? if yes, then delete it.
"""
#Mouse clicker

mouse = Controller()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#BlackListing
BlackList = ['تقارير','حل','خدماتنا','خدمات','التقارير','حلول','منصة','التعليميه','طلابية','انشطة','الانشطة']

wordArray = []
wordArrayHar = []
wordArrayHarAr = []

#Instructions for the Whatsapp bot
class WhatsApp:
    
    #Define the starting values(constructor)
    def __init__(self, speed=.1, clickSpeed=.3):
        self.speed = speed
        self.clickSpeed = clickSpeed
        self.message = ''
        self.lastMessage = '#590482'

    def navGreenDot(self):
        try:
            position = pt.locateCenterOnScreen(Image.open('greenDot.png'), confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            """                ^ this takes the indices 0,1 which are x,y"""
            pt.moveRel(100,0,duration=self.speed)
            pt.doubleClick(interval=self.clickSpeed)
        except Exception as e:
            print("Exception (navGreenDot): ", e)

    def navInputBox(self):
            try:
                position = pt.locateCenterOnScreen(Image.open('paperClip.png'), confidence=.7)
                pt.moveTo(position[0:2], duration=self.speed)
                """                    ^ this takes the indices 0,1 which are x,y"""
                pt.moveRel(-100,10,duration=self.speed)
                pt.doubleClick(interval=self.clickSpeed)
            except Exception as e:
                print("Exception (navInputBox): ", e)

    def navMessage(self):
            try:
                position = pt.locateCenterOnScreen(Image.open('paperClip.png'), confidence=.7)
                pt.moveTo(position[0:2], duration=self.speed)
                """                    ^ this takes the indices 0,1 which are x,y"""
                pt.moveRel(10,-80,duration=self.speed)
                #pt.doubleClick(interval=self.clickSpeed)
            except Exception as e:
                print("Exception (navMessage): ", e)

    def navNewMessage(self):
        pass

    def getMessage(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        
        #mouse.click(Button.right,1)
        #sleep(self.speed)
        pt.hotkey('ctrl','c',interval=.1)
        
        self.message = pc.paste()
        pt.moveRel(-50,0)
        pt.moveRel(50,0) 
        pt.moveRel(0,-50)
        pt.moveRel(0,50)        
        print("user say: ",self.message)

    def sendMessage(self):
        try:
            botResponse = responses(self.message)
            self.lastMessage = self.message
            if botResponse != 'no messages match':
                pc.copy(botResponse)
                print('You say: ', botResponse)
                pt.moveTo(x=935, y=988) # corrdinates of the message box 
                pt.hotkey('ctrl','v', interval=.1)
                pt.typewrite('\n')# this press enter
            else:
                print(botResponse)
                #Assign the last to the first
                #self.lastMessage = self.message

        except Exception as e:
            print("Exception (sendMessage)", e)

    def navNumber(self):
        try:
            position = pt.locateCenterOnScreen(Image.open('number.png'), confidence=.7)
        except Exception as e:
            print("Exception (navNumber)", e)

    def searchForbiddenMessage(self):
        
        for i in range(len(BlackList)):
            #word = str[str.index(BlackList[ind]):(str.index(BlackList[ind])+len(BlackList[ind]))]
            if(BlackList[i] in wordArray):
                wordArrayHar.append(BlackList[i])
            else:
                pass
        return wordArrayHar

    def searchForbiddenAr(self):
        for i in BlackList:
            for j in wordArray:
                print(i," and ", j)
                if(araby.vocalizedlike(i, j)):
                    wordArrayHarAr.append(j)
                else:
                    pass
        return wordArrayHarAr
                
    def isForbiddenAr(self):
        for i in BlackList:
            for j in wordArray:
                #print(i," and ", j)
                if(araby.vocalizedlike(i, j)):
                    return True
                else:
                    pass
        return False

    def searchWordMessage(self):
        #analize the message and extracts the words in the black list (tokenize)
        #if self.message[-1]==' ':
        #    self.message[-1]=self.message[:-2]
        
        str = self.message+' '
        #str = strip_diacritics(str)
        
        #str = 'wow this'
        wordCounter = 0
        word=''
        for i in str:
            if i==' ':
                wordArray.append(word)
                wordCounter=wordCounter+1
                word=''
            elif str.index(i)==len(str)-1:
                i = str[len(str)-1]
                word=word+i
                wordArray.append(word)
                word=''
            else:
                word=word+i
        AnBot.normalize(wordArray)
        return wordArray

    def Del(self):
        #navigate to the down arrow and deletes the message
        try:
            position = pt.locateCenterOnScreen(Image.open('downArrow.png'), confidence=.8)
            pt.moveTo(position[0:2], duration=self.speed)
            sleep(self.speed)
            mouse.click(Button.left,1)
            sleep(self.speed)
            pt.moveRel(-10,-140, duration=self.speed)
            sleep(self.speed)
            mouse.click(Button.left,1)
            sleep(self.speed)
            pt.moveTo(x=770, y=600)
            mouse.click(Button.left,1)
            sleep(self.speed)
            pt.moveTo(x=742, y=700)
            sleep(self.speed)
            mouse.click(Button.left,1)

        except Exception as e:
            print("Exception (Del): ", e)

    def ratioOfForbidden(self):
    #simply checks the wordArrayHar and devide the founded words by the whole sentence in the wordArr and multiply it by 100
        return (len(wordArrayHar)/len(wordArray))


    def isForbiddenRatio(self):
        val=self.ratioOfForbidden()
        if val>=.1:
            #if it passes this then the ratio of the whole message is 50% contains forbidden words
            return True
        else:
            return False

    def isForbidden(self):
    #simply checks the wordArrayHar if it contains anything
        for i in range(len(wordArrayHar)):
            
            if wordArrayHar[i] in BlackList:
                return True
            else:
                return False
        return False
    
    def checkForX(self):
        try:
            position = pt.locateOnScreen(Image.open('x.png'), confidence=.8)
            pt.moveTo(position[0:2], duration=self.speed)
            mouse.click(Button.left, 1)
        except Exception as e:
            print("Exception (checkForX): ", e)

    def checkForConfirmation(self):
        try:
            position = pt.locateOnScreen(Image.open('AR\\wo\\confirm.png'), confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            mouse.click(Button.left, 1)
        except Exception as e:
            print("Exception (checkForX): ", e)

    def isNewMessage(self):
        print(self.message," wow ",self.lastMessage)
        if self.message == self.lastMessage:
            return False
        else:
            
            return True

    """
    this one uses iteration on the taken list
    def recognize(self):
        # the job for this function is to locate all the forbidden words if any make presence
        try:
            
            print("RECOGNITION STARTS...")
            
            #if(position := pt.locateAllOnScreen("AR\\alif1C.png")):
                #print("hello")
            #print(list(pt.locateAllOnScreen("AR\\wo\\forbidden\\kak.png",confidence=.8)))
                #pt.moveTo(position[0:2], duration=.2) 
            checker =(position:= list(pt.locateAllOnScreen("AR\\wo\\forbidden\\kak.png",confidence=.8)))==[]
            while(checker):
                checker =(position:= list(pt.locateAllOnScreen("AR\\wo\\forbidden\\kak.png",confidence=.8)))==[]
                #print("recognision state", False)
                pass
            print("recognision state", True)
            print("------------------------------------------------------------")
            print("first tuple value",position)
            for i in range(len(position)):
                print("------------------------------------------------------------")
                print("the value of i in position in kak",i, end=" # ")
                print("------------------------------------------------------------")
                pt.moveTo(position[i][0:2], duration=.3)
                sleep(self.speed) # this block moves to the message location then copies it to later analization
                
                self.getMessage()# copies the message then analize the ratio of the forbidden words
                self.searchWordMessage()# i need to do normalization of the sentence before analizing like مسلم = مسسسسللممم
                self.searchForbiddenMessage()
                print("forbidden ration exceeded 50%: ",AnBot.isForbiddenRatio(), AnBot.ratioOfForbidden())
                if(AnBot.isForbiddenRatio()):
                    #self.downArrow()# to delete the message one after another
                    print("deleted")
                    pass
                else:
                    print("not deleted")
                    pass
                print("position of [i][0:2]",position[i][0:2])
                sleep(6)
                print("------------------------------------------------------------")
                print("END OF RECOGNIZING, tuple of index",i)
                print("------------------------------------------------------------")
                
            #else:
                #print("wow")
                #print(pt.useImageNotFoundException())
        except Exception as e:
            print("Exception (recognition): ", e)
            """

    def recognize(self):
        # the job for this function is to locate the first detected forbidden word if any make presence
        try:
            
            
            print("STARTS RECOGNITION...")
            
            #if(position := pt.locateAllOnScreen("AR\\alif1C.png")):
                #print("hello")
            #print(list(pt.locateAllOnScreen("AR\\wo\\forbidden\\kak.png",confidence=.8)))
                #pt.moveTo(position[0:2], duration=.2) 
            while(True):
                if((position0:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 0")
                    position=position0
                    break
                elif((position1:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 1")
                    position=position1
                    break
                elif((position2:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 2")
                    position=position2
                    break
                elif((position3:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 3")
                    position=position3
                    break
                elif((position4:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 4")
                    position=position4
                    break
                elif((position5:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 5")
                    position=position5
                    break
                elif((position6:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 6")
                    position=position6
                    break
                elif((position7:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 7")
                    position=position7
                    break
                elif((position8:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 8")
                    position=position8
                    break
                elif((position9:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 9")
                    position=position9
                    break
                elif((position10:= (pt.locateCenterOnScreen("AR\\wo\\forbidden\\a1.png",confidence=.8)))!=None):
                    print("position: 10")
                    position=position10
                    break
                
            print("recognision state", True)
            print("------------------------------------------------------------")
            print("location of the detection",position[0:2])
            print("------------------------------------------------------------")
            pt.moveTo(position[0:2], duration=.3)
            sleep(self.speed) # this block moves to the message location then copies it to later analization
                
            self.getMessage()# copies the message then analize the ratio of the forbidden words
            print(self.searchWordMessage())# i need to do normalization of the sentence before analizing like مسلم = مسسسسللممم
            print(self.searchForbiddenMessage())
            print("forbidden ration exceeded 10%: ",AnBot.isForbiddenRatio(), AnBot.ratioOfForbidden())
            if(AnBot.isForbiddenRatio()):
                self.downArrow()# to delete the message one after another
                print("deleted")
            else:
                print("not deleted")
                
            
            print("position of [0:2]",position[0:2])
            print("------------------------------------------------------------")
            print("END OF RECOGNIZING")
            print("------------------------------------------------------------")
                
            #else:
                #print("wow")
                #print(pt.useImageNotFoundException())
        except Exception as e:
            print("Exception (recognition): ", e)


    def downArrow(self):
        try:
            print("Start of deletion operation")
            while((position := pt.locateCenterOnScreen("downArrow2.png", confidence=.8)) == None):
                #^ this means it detects the down arrow
                pt.vscroll(50)
                pass
            print("returned position of the down arrow",position)
            pt.moveTo(position[0:2], duration=self.speed)
            mouse.click(Button.left,1)
            sleep(self.speed)
            # i want to keep looking for the down arrow until it find it
            #now i want it to delete the message
            position0=None
            position1=None
            position2=None
            while((position0 := pt.locateCenterOnScreen("AR\\wo\\delmes2.png", confidence=.8)) == None):
                while((position1 := pt.locateCenterOnScreen("AR\\wo\\delmes.png", confidence=.8)) == None):
                    while((position2 := pt.locateCenterOnScreen("AR\\wo\\delmesC.png", confidence=.8)) == None):
                        break
                # this detects the deleting word
                    break
                if(position0!=None or position1!=None or position2!=None):
                    break
                else:
                    continue
            if(position0!=None):
                position=position0
            elif(position1!=None):
                position=position1
            else:
                position=position2
            print("returned position of the delete message box",position)
            pt.moveTo(position[0:2], duration=self.speed)
            mouse.click(Button.left,1)
            sleep(self.speed)

            while((position := pt.locateCenterOnScreen("AR\\wo\\delAll.png", confidence=.8)) == None):
                # this goes to the delete for all sentence
                pass
            print("returned position of the delete for all box",position)
            pt.moveTo(position[0:2], duration=self.speed)
            mouse.click(Button.left,1)
            sleep(self.speed)

            while((position := pt.locateCenterOnScreen("AR\\wo\\delAll2.png", confidence=.8)) == None):
                # this confirms the delete for all sentence
                pass
            print("returned position of the confirm delete for all box",position)
            pt.moveTo(position[0:2], duration=self.speed)
            mouse.click(Button.left,1)
            sleep(1)
            print("END OF DELETION")


        except Exception as e:
            print("Exception (downArrow): ", e)

    def normalize(self,str):
        # this function will take the wordArray and normalize its contents cuz duh why not lessen the analization
        newStr=''
        counter=0
        for i in str:
            for j in range(len(i)):
                #print(j)
                if ((j+1)<len(i) and i[j] != i[j+1]):
                    newStr+=i[j]
                elif((j+1)==len(i)):
                    newStr+=i[j]
                else:
                    pass
            str[counter]=newStr
            newStr=''
            counter+=1
        return str


#now the bot recognize the text that contains only the forbidden word instead of analizing the whole text and each and every text,
# then it locates the text position on the screen then it goes to the down arrow and chooses the deleting choice...
AnBot = WhatsApp(speed=.5, clickSpeed=.4)

#sleep(3)


#        ^ this function rely on the previous one
#AnBot.recognition()
sleep(3)
#AnBot.message = '/مات التعليميه'
#print(AnBot.searchWordMessage())
#print(AnBot.searchForbiddenMessage())
#print(AnBot.isForbiddenRatio(), AnBot.ratioOfForbidden())

while True:
    wordArray=[]
    wordArrayHar=[]
    AnBot.checkForX()
    AnBot.checkForConfirmation()
    AnBot.recognize()
"""
sss=True
ss=True
while(s:=True):
    while(ss:=False):
        while(sss:=True):
            break
        break
    if(sss!=True or ss!=True or s!=True):
        print(s,ss,sss)
        break
    else:
        continue
if(sss!=True):
    position = sss
elif(ss!=True):
    position=ss
else:
    position=s
Algorithm to determine which image get recognized
"""
#print(AnBot.normalize(["hello","duh"]))

"""
while True:
    wordArray = []
    wordArrayHar = []
    
    print("message",AnBot.message," last message:", AnBot.lastMessage)
    sleep(.1)
    pt.vscroll(-50)
    sleep(.1)
    AnBot.checkForX()
    #sleep(2)
    pt.moveTo(x=1118, y=867)
    #AnBot.navMessage()
    #sleep(2)
    AnBot.getMessage()
    
    while(AnBot.isNewMessage()):
        #AnBot.navGreenDot()
        #AnBot.navMessage() instead use a fixed positioned mouse
    
        AnBot.searchWordMessage()
        AnBot.searchForbiddenMessage()
    
        print(AnBot.isForbidden() ,"or", AnBot.isForbiddenAr())
    
        if(AnBot.isForbidden()):
    
            pt.moveTo(x=1118, y=1000)
    
            pt.moveTo(x=1118, y=867)
            print("del")
            #sleep(2)
            AnBot.Del()
            break
        
        else:
            print("message",AnBot.message," last message:", AnBot.lastMessage)
            print("send")
            
            AnBot.sendMessage()
            break
            up here is the automated way to delete the messages without any image recognition rely heavly on given coordinates"""
    
        # the program discovers where the delete option lies then saves its position for next operations