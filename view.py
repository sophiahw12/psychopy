import os
from psychopy import visual, core

class View():
    # https://en.wikipedia.org/wiki/Observer_pattern
    def __init__(self, observable):
        observable.register_observer(self)
        self.model = observable
        self.mywin = visual.Window([600,600], monitor="testMonitor", units="pix")

    def notify(self, observable, *args, **kwargs):
        if "state" in kwargs:
            if kwargs["state"] == None:
                visual.TextStim(self.mywin, text='Welcome').draw()
                self.mywin.flip()
            if kwargs["state"] == "stimuli":
                self.show_image(self.model.stimuli[-1])
            if kwargs["state"] == "response":
                visual.TextStim(self.mywin, text='Please press key 1 or 2').draw()
                self.mywin.flip()

    def show_image(self, file):
        img = visual.ImageStim(self.mywin, image=file, units="pix")
        img.draw()
        self.mywin.flip()
