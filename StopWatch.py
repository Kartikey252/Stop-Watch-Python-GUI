# Importing Stop Watch Class from Main.py
from Main import StopWatch


if __name__ == '__main__':
    # Creating An Stop Watch App using StopWatch Class from Main.py
    App = StopWatch()
    App.addFrames()
    App.timerPlace()
    App.startButtonPlace()
    App.stopButtonPlace()
    App.resetButtonPlace()
    App.mainloop()