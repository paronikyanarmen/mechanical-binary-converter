import math
from dataclasses import dataclass
import numpy as np


@dataclass
class Spring:
    k: float = 1

    def _set_k(self, k):
        self.k = k

    def get_k(self):
        return self.k

    def move(self, t_end, dt, x_start, v_start=0, t_start=0, m=1):
        res = np.array([])

        freq = math.sqrt(self.k / m)

        print(freq)

        t = t_start
        while t <= t_end:
            cosine_part = x_start * np.cos(freq * t * 2 * np.pi)
            sine_part = v_start / freq * np.sin(freq * t * 2 * np.pi)
            val = cosine_part + sine_part
            res = np.append(res, val)
            t += dt

        return res

    def in_series(self, other):
        k = self.get_k()
        other_k = other.get_k()

        new_k = k * other_k / (k + other_k)

        return Spring(k=new_k)

    def in_parallel(self, other):
        return Spring(self.get_k() + other.get_k())
