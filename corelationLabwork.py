from randomSignalsFirstLab import function_y_axis, signal, my_expected, w, n, N, file_writer, expected_value
import random
from time import time, strftime
import matplotlib.pyplot as plt
from datetime import datetime
from stab import stabylizer as st

DATA_FILE_PATH = "/home/whoiandrew/Desktop/rts-data/secondLabData.txt"
PLOT_FILE_PATH = "/home/whoiandrew/Desktop/rts-data/secondLabPlot.pdf"

amplitude2, phi2 = random.uniform(0, 1), random.uniform(0, 1)
function2_y_axis = [sum([signal(i, (j * N) / n, amplitude2, phi2) for j in range(n)]) for i in range(N)]
function2_half_y_axis = function_y_axis[:len(function_y_axis)//2]
my_expected2 = expected_value(function2_y_axis, N)

function_half_y_axis = function_y_axis[:len(function_y_axis)//2]

correlation = lambda t_arr, tau_arr, mx, number: sum(((t_arr[i] - mx)*(tau_arr[i] - mx)) for i in range(number)) / (number - 1) 

start_xx = time()
correlation_y_axis = [correlation(function_half_y_axis, function_y_axis[i: i + N//2], my_expected, N // 2) for i in range(N//2)]
end_xx = time()
xx_time = end_xx - start_xx

start_xy = time()
correlation_y2_axis = [correlation(function_half_y_axis, function2_y_axis[i: i + N//2], my_expected2, N // 2) for i in range(N//2)]
end_xy = time()

xy_time = end_xy - start_xy

correlation_y_axis, correlation_y2_axis = list(map(st, [correlation_y_axis, correlation_y2_axis]))



file_writer(f"Last update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    f"Time of R(xx) calculations = {xx_time}\nTime of R(xy) calculations = {xy_time}\n"
    f"R(xx) corelation values array:\n{correlation_y_axis}\n\n\nR(xy) corelation values array:\n{correlation_y2_axis}\n", DATA_FILE_PATH)


plt.subplot(2, 1, 1)
plt.title(f"Last update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
plt.ylabel("R(xx)")
plt.plot([i for i in range(N//2)], correlation_y_axis)
plt.subplot(2, 1, 2)
plt.ylabel("R(xy)")
plt.plot([i for i in range(N//2)], correlation_y2_axis)
plt.savefig(PLOT_FILE_PATH)



