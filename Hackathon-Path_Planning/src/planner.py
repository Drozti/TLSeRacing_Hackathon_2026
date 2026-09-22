from src.track import Track
import numpy as np

class PathPlanner:
    def __init__(self, step_size : float = 0.5, smoothing : float = 1.0):
        self.step_size = step_size
        self.smoothing = smoothing

    def simple_compute_path(self, track : Track):

        start_coo = (track.car_start.x, track.car_start.y)
        path = [start_coo]

        # TODO 

        return path


