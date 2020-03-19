import matplotlib.pyplot as plt
import math
import random
from time import time

w = 2000  # cutoff frequency
n = 8  # number of sine waves
N = 256  # number of discrete marks

amplitude = random.uniform(0, 1)
phi = random.uniform(0, 1)

DFT_PLOT1_PATH = "plot_dft.png"
DATA_PATH = "data.txt"


def time_counter(callback, *args):
    start = time()
    callback(*args)
    end = time()
    return end - start


def file_writer(data: str, path: str):
    with open(path, "w+") as file_handler:
        file_handler.write(data)


# 2.1 labwork (DFT)
signal = lambda t, w, ampl, phi: math.sin(w * t + phi) * ampl
iexp = lambda n: complex(math.cos(n), math.sin(n))
dft = lambda signal: [sum((signal[k] * iexp(-2 * math.pi * i * k / len(signal)) for k in range(len(signal))))
                      for i in range(len(signal))]

my_dft = dft([sum([signal(i, (w * j) / n, amplitude, phi) for j in range(n)]) for i in range(N)])

if __name__ == "__main__":
    # generating and saving plots as a .png
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Discrete Fourier Transform')
    ax1.plot(list(map(lambda item: item.real, my_dft)))
    ax1.set_title("DFT real")
    ax2.plot(list(map(lambda item: item.imag, my_dft)), 'tab:orange')
    ax2.set_title("DFT imagine")
    ax3.plot(list(map(lambda item: abs(item), my_dft)), 'tab:green')
    ax3.set_title("Amplitude spectrum")
    ax4.plot(list(map(lambda item: abs(item) ** 2, my_dft)), 'tab:red')
    ax4.set_title("Power spectrum")

    # calculating dft execution time and saving as a .txt file
    file_writer(
        f"DFT calculating time: {time_counter(dft, [sum([signal(i, (w * j) / n, amplitude, phi) for j in range(n)]) for i in range(N)])} sec",
        DATA_PATH)

    for ax in fig.get_axes():
        ax.label_outer()

    plt.savefig(DFT_PLOT1_PATH)
