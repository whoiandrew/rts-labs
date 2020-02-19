# 1st RTS labwork made by Andrii Doroshenko, IO-71
# 7309

import math
import random
from time import time, strftime
from datetime import datetime
import matplotlib.pyplot as plt

w = 2000  # cutoff frequency
n = 8  # number of sine waves
N = 256  # number of discrete marks
DATA_FILE_PATH = "/home/whoiandrew/Desktop/rts-data/firstLabData.txt"
PLOT_FILE_PATH = "/home/whoiandrew/Desktop/rts-data/firstLabPlot.pdf"

amplitude = random.uniform(0, 1)
phi = random.uniform(0, 1)


def file_writer(data: str):
    with open(DATA_FILE_PATH, "w+") as file_handler:
        file_handler.write(data)


signal = lambda t, w, ampl, phi: math.sin(w * t + phi) * ampl
expected_value = lambda func_arr, number: sum(func_arr) / number
dispersion = lambda xpctd, func_arr, number: sum([pow((i - xpctd), 2) for i in func_arr]) / N - 1

function_y_axis = [sum([signal(i, (j * N) / n, amplitude, phi) for j in range(n)]) for i in range(N)]
argument_x_axis = [i for i in range(N)]

m_start = time()
my_expected = expected_value(function_y_axis, N)
m_end = time()
m_time = m_end - m_start

disp_start = time()
my_dispertion = dispersion(my_expected, function_y_axis, N)
disp_end = time()
disp_time = disp_end - disp_start

file_writer(f"Math expectation value M(x) = {my_expected}\nM(x) calculations time = {m_time} seconds\n\n"
            f"Dispersion value D(x) = {my_dispertion}\nD(x) calculations time = {disp_time} seconds\n\n"
            f"Last update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

plt.title(f"Last update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
plt.ylabel("x(t) = A*sin(t * \u03a9 + \u03c6)")
plt.xlabel(f"x(t)")
plt.plot(argument_x_axis, function_y_axis)
plt.savefig(PLOT_FILE_PATH)
