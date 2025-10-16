import threading as th
import AlphaBot

class GestoreSensori(th.Thread):
    def __init__(self, ab):
        self.sensor = ()
        self.ab = ab
    
    def start(self):
        pass
    
    def run(self):
        if self.ab.getSensors() == (0,0):
            self.ab.stop()