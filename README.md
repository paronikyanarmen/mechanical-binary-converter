# Mechanical Binary Converter
Binary to decimal converter by springs for AUA mechanics class.

## Idea
Simulate combinations of springs to make a system that will map to 0 or 1. Combine this systems to represent a byte then transform it to decimal representation.

## Step 1: Fourier transform

I researched on fourier transforms and found some information [here](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/) and [here](https://blog.endaq.com/fourier-transform-basics).

I decided to implement the project in Python since this is the language I am most proficient in. I searched the web to find any libraries that implement Fourier transforms. It turns out that SciPy has a [method](https://docs.scipy.org/doc/scipy/tutorial/fft.html) that covers Fourier Transforms.

I used some code examples and documentation from [here](https://realpython.com/python-scipy-fft/).