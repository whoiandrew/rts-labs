from math import *
from cmath import exp, pi
import random
from time import time

w = 2000  # cutoff frequency
n = 8  # number of sine waves
N = 256  # number of discrete marks

amplitude = random.uniform(0, 1)
phi = random.uniform(0, 1)

DFT_PLOT_PATH = "plot_dft.png"
FFT_PLOT_PATH = "plot_fft.png"
DATA_PATH = "data.txt"


def time_counter(callback, *args):
    start = time()
    callback(*args)
    end = time()
    return end - start



def file_writer(data: str, path: str):
    with open(path, "w+") as file_handler:
        file_handler.write(data)


def output(name:str, values, plot_path: str):
    import matplotlib.pyplot as plt
    # generating and saving plots as a .png
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle(f'{name}')
    ax1.plot(list(map(lambda item: item.real, values)))
    ax1.set_title(f"{name} real")
    ax2.plot(list(map(lambda item: item.imag, values)), 'tab:orange')
    ax2.set_title(f"{name} imagine")
    ax3.plot(list(map(lambda item: abs(item), values)), 'tab:green')
    ax3.set_title("Amplitude spectrum")
    ax4.plot(list(map(lambda item: abs(item) ** 2, values)), 'tab:red')
    ax4.set_title("Power spectrum")

    for ax in fig.get_axes():
        ax.label_outer()

    plt.savefig(plot_path)


# 2.1 labwork (DFT) n*log(n)
signal = lambda t, w, ampl, phi: sin(w * t + phi) * ampl
iexp = lambda n: complex(cos(n), sin(n))
dft = lambda signal: [sum((signal[k] * iexp(-2 * pi * i * k / len(signal)) for k in range(len(signal))))
                      for i in range(len(signal))]


# 2.2 labwork (FFT) n**2
def fft(x):
    n = len(x)
    if n <= 1: return x
    even, odd = fft(x[0::2]), fft(x[1::2])
    t = [exp(-2j * pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + t[k] for k in range(n // 2)] + [even[k] - t[k] for k in range(n // 2)]

if __name__ == "__main__":
    my_signal = [sum([signal(i, (w * j) / n, amplitude, phi) for j in range(n)]) for i in range(N)]
    my_dft = dft(my_signal)
    my_fft = fft(my_signal)

    output("DFT", my_dft, DFT_PLOT_PATH)
    output("FFT", my_fft, FFT_PLOT_PATH)
    file_writer(
        f"DFT calculating time: {time_counter(dft, my_signal)} sec\n"
        f"FFT calculating time: {time_counter(fft, my_signal)} sec\n\n"
        f"{'FFT ' if time_counter(fft, my_signal) < time_counter(dft, my_signal) else 'DFT'} is faster",
        DATA_PATH)


