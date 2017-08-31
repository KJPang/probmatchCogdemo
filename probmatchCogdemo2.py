#K Pang 2017
import sys
import psychopy.visual
import psychopy.event
import psychopy.core
import psychopy.gui
import random
import time

#initialize variables
timestr = time.strftime("%Y%m%d-%H%M%S")
goeshere = open(timestr + ".txt", 'w')
sys.stdout = goeshere
chancelist = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
textlist = ["1", "2", "3", "4"]
random.shuffle(chancelist)
order1 = int(0)
clock = psychopy.core.Clock()
exptrials = range(20)
countresponses = range(10)
condition = int(1) #this must be either 1 or 0

#make a gui, set up positions
win = psychopy.visual.Window(size=[1600, 900], units="pix", fullscr=True, color=[-1, -1, -1])
un = psychopy.visual.TextStim(win=win, pos=(0, -300), color=[1, 1, 1], height = 50)
du = psychopy.visual.TextStim(win=win, pos=(0, -325), color=[1, 1, 1], height = 50)
du.text = "__________________"
un.text = ""
responsestring = ""

#initialize text
text1a = "A 10 sided die has "
text1b = " face(s) that show squares and "
text1c = " that show triangles. \nThis die is rolled 10 times, guess the sequence of results."
text2a = "A 10 sided die has "
text2b = " blue face(s) and "
text2c = " orange face(s). \nThis die is rolled 10 times, guess the sequence of results."
text3a = "A wheel has "
text3b = " green section(s) and "
text3c = " blue. \nThe wheel is spun 10 times, guess the sequence of results."
text4a = "A wheel has "
text4b = " section(s) that show a circle and "
text4c = " section(s) that show a star. \nThe wheel is spun 10 times, guess the sequence of results."

midcross = psychopy.visual.TextStim(win=win, wrapWidth=100, height = 25)
midcross.text = " + "
inst1 = psychopy.visual.TextStim(win=win, wrapWidth=1000)

correctwords = "\n\nYou will gain $1 if the sequence is guessed correctly."
mistakewords = "\n\nYou will have to pay the experimenter $1 unless the sequence is guessed correctly."
instructionwords = "\n\nUse the Q and P keys to input a sequence. Use Q for the first option shown and P for the second."

#trials
for i in exptrials:
    #randomize order
    if order1 == 9:
        order1 = 0
        random.shuffle(chancelist)
    random.shuffle(textlist)
    textchoice = int(textlist[1])
    secondary = 10 - int(chancelist[order1])
    #choose text to display
    if textchoice == 1:
        if condition == 0: 
            inst1.text = text1a + chancelist[order1] + text1b + str(secondary) + text1c + correctwords + instructionwords
        else:
            inst1.text = text1a + chancelist[order1] + text1b + str(secondary) + text1c + mistakewords + instructionwords          
    elif textchoice == 2:
        if condition == 0: 
            inst1.text = text2a + chancelist[order1] + text2b + str(secondary) + text2c + correctwords + instructionwords
        else:
            inst1.text = text2a + chancelist[order1] + text2b + str(secondary) + text2c + mistakewords + instructionwords
    elif textchoice == 3:
        if condition == 0: 
            inst1.text = text3a + chancelist[order1] + text3b + str(secondary) + text3c + correctwords + instructionwords
        else:
            inst1.text = text3a + chancelist[order1] + text3b + str(secondary) + text3c + mistakewords + instructionwords
    elif textchoice == 4:
        if condition == 0: 
            inst1.text = text4a + chancelist[order1] + text4b + str(secondary) + text4c + correctwords + instructionwords 
        else:
            inst1.text = text4a + chancelist[order1] + text4b + str(secondary) + text4c + mistakewords + instructionwords
    inst1.draw()        
    un.draw()
    du.draw()
    win.flip()
    clock.reset()
    for i in countresponses:
        selection = psychopy.event.waitKeys(keyList=["q", "p", "m"])
        if selection == ["m"]:
            win.close()
            sys.exit()
        if selection == ["q"]:
            if textchoice == 1: 
                responsestring = responsestring + "S"
            if textchoice == 2: 
                responsestring = responsestring + "B"
            if textchoice == 3: 
                responsestring = responsestring + "G"
            if textchoice == 4:     
                responsestring = responsestring + "C"
        if selection == ["p"]:
            if textchoice == 1: 
                responsestring = responsestring + "T"
            if textchoice == 2: 
                responsestring = responsestring + "O"
            if textchoice == 3: 
                responsestring = responsestring + "B"
            if textchoice == 4:  
                responsestring = responsestring + "S"
        un.text = responsestring
        inst1.draw()
        du.draw()
        un.draw()
        win.flip()
    if textchoice == 1:
        print "S T"
    if textchoice == 2:
        print "B O"
    if textchoice == 3:
        print "G B"
    if textchoice == 4:
        print "C S"
    print str(chancelist[order1]) + " " + str(secondary)
    print responsestring
    print "\n"
    clock.reset()
    while clock.getTime() < 0.5:
        un.draw()
        win.flip()
    responsestring = ""
    un.text = ""
    order1 = order1 + 1
    win.flip()
    
win.flip()
psychopy.event.waitKeys()
win.close()
sys.exit()
#testing version
