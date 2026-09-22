import numpy as np  
import pandas as pd 
from dataclasses import dataclass
import csv

@dataclass
class Cone:
    x: float
    y: float
    color: str 

@dataclass
class CarPose:
    x: float
    y: float


class Track:
    def __init__(self, csv_path : str):
        self.blue_cones = []
        self.yellow_cones = []
        self.orange_cones = []
        car_start = None
        
        self.load_from_csv(csv_path)

    def load_from_csv(self, csv_path: str):
        with open(csv_path, mode='r', encoding='utf-8') as f:
            rows = csv.DictReader(f)
            for row in rows:
                tag = row['tag'].strip()
                x = float(row['x'])
                y = float(row['y'])

                if tag == 'car_start':
                    self.car_start = CarPose(x=x, y=y)
                elif tag == 'blue':
                    self.blue_cones.append(Cone(x=x, y=y, color='blue'))
                elif tag == 'yellow':
                    self.yellow_cones.append(Cone(x=x,y=y, color='yellow'))
                elif 'orange' in tag:
                    self.orange_cones.append(Cone(x=x,y=y, color='orange'))


