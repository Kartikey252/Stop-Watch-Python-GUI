# Importing tkinter and Time Modules
from tkinter import *
from tkinter.font import BOLD
import time


# Creating a Stop Watch Class
class StopWatch(Tk):

    __goOn = False
    __time = 0
    
    def __init__(self):
        """ Takes Methods From Tk Class of Tkinter Module """
        super().__init__()
        self.geometry('400x300+750+250')
        self.title('Sky Dive Stop Watch')
        self.config(bg='#10111b')
        self.wm_iconbitmap(r'icon.ico')
        self.resizable(False, False)
    
    def addFrames(self):
        """ Adds two diefferent Frames in App 
        These Frames are :
            timerFrame -> Shows Time Lapsed
            buttonFrame -> Shows Control Buttons of App
        """
        self.timerFrame = Frame(bg='#10111b', bd=0)
        self.buttonFrame = Frame(bg='#10111b', bd=0)
        self.timerFrame.pack(fill=BOTH, expand=YES)
        self.buttonFrame.pack(fill=BOTH, expand=NO)

    def timerPlace(self):
        """ Adds Time Label in App """
        self.timer = Label(self.timerFrame, font=('@MS Gothic', 39, BOLD), text='00:00:00:00', bg='#10111b', fg='white')
        self.timer.pack(anchor=CENTER, expand=YES, fill=BOTH)
    
    def startButtonPlace(self):
        """ Adds Start Button in App 
        Function -> Start The Stop Watch
        """
        self.startButton = Button(self.buttonFrame, command=self.__startStopWatch, font=('Courier New', 20, BOLD), text='Start', activebackground='grey', activeforeground='white', bd=0, relief=FLAT)
        self.startButton.pack(side=LEFT, fill=BOTH, expand=YES, padx=4, pady=5)
    
    def stopButtonPlace(self):
        """ Adds Stop Button in App
        Function -> Stop and Resume Time"""
        self.stopButton = Button(self.buttonFrame, command=self.__stopStopWatch, font=('Courier New', 20, BOLD), text='Stop', activebackground='grey', activeforeground='white', bd=0, relief=FLAT, state=DISABLED)
        self.stopButton.pack(side=LEFT, fill=BOTH, expand=YES, padx=4, pady=5)
        
    def resetButtonPlace(self):
        """ Adds Reset Button in App
        Function -> Resets the Timer in App
        """
        self.resetButton = Button(self.buttonFrame, command=self.__resetStopWatch, font=('Courier New', 20, BOLD), text='Reset', activebackground='grey', activeforeground='white', bd=0, relief=FLAT, state=DISABLED)
        self.resetButton.pack(side=LEFT, fill=BOTH, expand=YES, padx=4, pady=5)

    def __startStopWatch(self):
        """ Function for Start Button in App 
        Starts Stop Watch
        """
        # Main Updation of Timer
        if self.__time:
            x = time.time()-self.__time
            hms = time.strftime('%H:%M:%S', time.gmtime(x))
            mlsec = repr(x).split('.')[1][:3]
            self.timer.config(text=f'{hms}:{mlsec}'[:11])
        # if __time variable of App is 0 and state of start Button is Normal
        elif not self.__time and self.startButton['state'] == NORMAL:
            self.__time = time.time()
            self.startButton.config(state=DISABLED)
            self.__goOn = True
            self.stopButton.config(state=NORMAL)
            self.resetButton.config(state=NORMAL)
            self.stopButton.config(text='Stop')
        # Update time every 10 miliseconds
        if self.__goOn:
            self.after(10, self.__startStopWatch)
        
    def __stopStopWatch(self):
        """ Function for Stop Button in App
        Stop/Resume Stop Watch
        """
        # When text in Stop Button in Stop
        # Do 'stop' Method
        if self.stopButton['text'] == 'Stop':
            self.x1 = time.time()
            self.__goOn = False
            self.stopButton.config(text='Resume')
        # When text in Stop Button in Resume
        # Do 'resume' Method
        else:
            self.__time += time.time() - self.x1
            self.__goOn = True
            self.__startStopWatch()
            self.stopButton.config(text='Stop')
    
    def __resetStopWatch(self):
        """ Reset Function for Reset Button in App
        Resets the Timer
        Two Cases to Use This Button :
            Case 1 -> Reset Buttton Pressed with Timer Running
                Resets the Timer and Starts the Timer Again
            Case 2 -> Reset Button Pressed with Timer Stopped
                Resets the App (as Started in Beginning)
        """
        self.__goOn = 0
        self.__time = 0
        self.startButton.config(state=NORMAL)
        self.timer.config(text='00:00:00:00')
        self.stopButton.config(state=DISABLED)
        self.resetButton.config(state=DISABLED)


if __name__=='__main__':
    print("Please Run 'StopWatch.py'\n")
    input()