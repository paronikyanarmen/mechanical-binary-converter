from collections import namedtuple

import numpy as np

from scipy import fft
from spring_array import SpringArray
from spring import Spring


class Converter:
    spring: Spring
    spring_array: SpringArray

    DURATION = 5
    SAMPLE_RATE = 100

    def __init__(self, spring_array):
        self.spring_array = spring_array

    def set_spring_from_binary(self, byte):
        springs = []
        for index, bit in enumerate(byte):
            if bit == '1':
                stiffness = 2 ** (8 - 1 - index)
                springs.append(Spring(k=stiffness))

        spring_expression = 'armen'

        self.spring = self.spring_array.equivalent_spring(spring_expression, springs)

    def get_oscillations(self):
        return self.spring.move(self.DURATION, 1 / self.SAMPLE_RATE, 2)

    def get_frequency_amplitudes(self, oscillations):
        frequency_powers = fft.rfft(oscillations)

        total_number_of_samples = self.SAMPLE_RATE * self.DURATION
        frequency_values = fft.rfftfreq(total_number_of_samples, 1 / self.SAMPLE_RATE)

        frequency_amplitudes = np.abs(frequency_powers)

        FFTResult = namedtuple('FFTResult', 'frequency_values frequency_amplitudes')

        return FFTResult(frequency_values=frequency_values, frequency_amplitudes=frequency_amplitudes)

    def get_decimal(self, fft_result):

        max_index = np.argmax(fft_result.frequency_amplitudes)

        max_freq = fft_result.frequency_values[max_index]

        return int(max_freq * max_freq)
