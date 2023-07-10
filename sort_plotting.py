import time
import random
import matplotlib.pyplot as plt
# importy funkcji sortujących z odpowiednich plików
from quick_sort import quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort


def x_times_loop(loops: int, function, lista: list):
    """ Funkcja bierze jako argumenty: krotność wykonania pętli, funkcję sortującą oraz
    rodzaj listy do sortowania. Zwraca średni czas wykoniania podanej funkcji sortującej """
    measurements = []
    for i in range(loops):
        start = time.time_ns()
        function(lista)
        end = time.time_ns()
        measurements.append(end - start)
    avg = sum(measurements) / loops
    return avg


quick_results = []
merge_results = []
insertion_results = []
axis_x = ['small', 'avg', 'big', 'sorted', 'reversed']
l_o_l = [[random.randint(1, 10) for x in range(500)], [random.randint(1, 10) for y in range(1000)],
         [random.randint(1, 10) for z in range(10000)], [x for x in range(1, 1000)],
         [x for x in range(1, 1000)][::-1]]

# pętla podająca do funkcji x_times_loop kolejne listy zawarte w l_o_l. Zwracane
# z wywołania funkcji wyniki zapisywane są do list stanowiących dane do wykresu
for li in l_o_l:
    quick_results.append(x_times_loop(10, quick_sort, li))
    merge_results.append(x_times_loop(10, merge_sort, li))
    insertion_results.append(x_times_loop(10, insertion_sort, li))
print(quick_results)
print(merge_results)
print(insertion_results)

plt.plot(axis_x, quick_results, label='Quick sort', c='green')
plt.plot(axis_x, merge_results, label='Merge sort', c='blue')
plt.plot(axis_x, insertion_results, label='Insertion sort', c='pink')
plt.title("Sorting performance")
plt.legend()
plt.yscale("log")
plt.ylabel("Time ns")
plt.xlabel("List type")
plt.show()
