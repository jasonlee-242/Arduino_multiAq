import pandas as pd
import numpy as np
import multiprocessing as mp

class Recorder:
    def __init__(self, name):
        self.name = name
        if self.name == "Cuff":
            self.cols = []
        else:
            self.cols = [[], [], []]
        self.count = 0
    
    def add(self, sensorNum, value):
        if self.name == "Cuff":
            self.cols.append(value)
        else:
            self.cols[sensorNum].append(value)

    def writeData(self):
        df = pd.DataFrame()
        if self.name == "Cuff":
            df.insert(0, column=self.name, value=self.cols)
        else:
            for i in range(3):
                df.insert(i, column=self.name + str(i), value=self.cols[i])
        df.to_csv(self.name + '_data.csv', index=False)

