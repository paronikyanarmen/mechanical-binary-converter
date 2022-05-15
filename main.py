from SpringArray import SpringArray
from converter import Converter

if __name__ == '__main__':

    spring_array = SpringArray()

    converter = Converter(spring_array)

    converter.set_spring_from_binary('11001001')

    oscillations = converter.get_oscillations()

    fft_result = converter.get_frequency_amplitudes(oscillations)

    print(converter.get_decimal(fft_result))
