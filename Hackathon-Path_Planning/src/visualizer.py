import matplotlib.pyplot as plt 
import numpy as np  
from src.track import Track


def plot_track_and_path(track : Track, path : np.ndarray | None = None):
        
        bx = [c.x for c in track.blue_cones]
        by = [c.y for c in track.blue_cones]

        yx = [c.x for c in track.yellow_cones]
        yy = [c.y for c in track.yellow_cones]

        ox = [c.x for c in track.orange_cones]
        oy = [c.y for c in track.orange_cones]

        plt.figure()
        plt.scatter(bx,
                by, 
                c='b',
                alpha = 0.5,
                label='blue cones (inside)')
        plt.scatter(yx,
                 yy,
                 c='gold',
                 alpha=0.5,
                 label='yellow_cones (outside)')
        
        plt.scatter(bx, by, color="blue", s=20)
        plt.scatter(yx, yy, color="gold", s=20)

        plt.scatter(ox,
                   oy, 
                   c='darkorange',
                   s=50,
                   alpha=0.7,
                   label='starting cones')
        
        plt.scatter(track.car_start.x,
                 track.car_start.y,
                 color='red',
                 marker='x',
                 alpha=0.8,
                 label='starting position')

        
        if path is not None and len(path) > 0:
            path = np.asarray(path, dtype=float)

            if path.ndim == 2 and path.shape[0] == 2 and path.shape[1] != 2:
                path = path.T

            plt.plot(
                path[:, 0],
                path[:, 1],
                color="limegreen",
                linewidth=2,
                alpha=0.9,
                label="Path",
            )

        plt.xlabel("X (m)")
        plt.ylabel("Y (m)")
        plt.axis('equal')
        plt.grid(True, linestyle='--',alpha=0.4)
        plt.legend()
        plt.tight_layout()
        plt.show()
