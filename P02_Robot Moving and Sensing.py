'''
'''

# Libraries
import numpy as np 
import matplotlib.pyplot as plt 
import random


# Classes
class robot:
    def _init_ (self, world_size= 100.0 , measurment_range= 30.0 , measurments_noise= 1.0, motion_noise= 1.0):
        self.x = world_size /2
        self.y = world_size /2
        self.meaurment_range = measurment_range
        self.measurments_noise = 1.0
        self.motoin_noise = motion_noise
        self.landmarks = []
        self.num_landmarks = 0

    def rand(self):
        return(random.random( *2.0 - 1.0))

    def move(self, dx, dy):
        x = self.x + dx +self.rand() * self.motion_noise
        y = self.y + dy +self.rand() * self.motoin_noise
        if x < 0.0 or x > world_size or y < 0.0 or y > world_size:
            return False
        else : 
            x = self.x
            y = self.y
            return True

    def sense(self):
        measurements = []
        for i, lm in enumerate(self.landmarks):
            dx, dy = lm[0] - self.x , lm[1] - self.y
            dx += self.rand() * self.measurement_noise
            dy += self.rand() * self.measurement_noise
            if (dx**2 + dy**2 <= self.measurement_range**2):
                measurements.append([i, dx, dy])
                return measurements
            


    def make_landmarks(self, num_landmarks):
        self.landmarks = []
        for i in range(num_landmarks):
            self.landmarks.append([round(random.random() * self.world_size),
                                   round(random.random() * self.world_size)])
        self.num_landmarks = num_landmarks
    

    def _repr_(self):
        return 'Robot: [x=%.5f y=%.5f]'  % (self.x, self.y)
