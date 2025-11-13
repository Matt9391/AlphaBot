import threading as th
import time
import AlphaBot

class GestoreSensori(th.Thread):
    def __init__(self, ab):
        super().__init__()
        self.ab = ab
        self.running = True
    
    def stop(self):
        self.running = False
    
    def run(self):
        while self.running:
            time.sleep(0.5)
            if (self.ab.getSensors()[0] == 0) or (self.ab.getSensors()[1] == 0):
                self.ab.canMoveForward = False
                print("Sensori bloccati")
            else:
                self.ab.canMoveForward = True
            if not self.ab.canMoveForward:
                print("MANNAGGIA A QUEL STOP")
                self.ab.backwardTime(0.2)
