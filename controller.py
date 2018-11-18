import os
import glob
import time
import random

class Controller:
    def __init__(self, model, dir, time, num):
        self.model = model
        self.time = time
        self.num = num
        self.imgs = []
        for f in glob.glob(dir + "/*.jpg"):
            ext = os.path.splitext(f)[-1]
            if ext.lower() not in ['.jpg']: # if extension is not .jpg
                continue
            else:
                self.imgs.append(os.path.abspath(f))
        random.shuffle(self.imgs)
        self.imgs = self.imgs[:self.num]

    def start(self):
        for stimuli in self.imgs:
            self.model.add_stimuli(stimuli)
            self.model.set_state("stimuli")
            time.sleep(self.time)
            self.model.set_state("response")
            response = input("Please press key 1 or 2: \n")
            self.model.add_response(response)
        self.model.set_state(None)
        print("responses: ", self.model.responses)
        print("stimuli: ", self.model.stimuli)
