import time
import os, psutil


def is_heap(arr, size_arr):
    flag = False
    for i in range(1, size_arr//2):
        if (i*2 <= size_arr) and (arr[i] > arr[i*2]):
            flag = True
            break
        if (i*2 + 1 <= size_arr) and (arr[i] > arr[i*2 + 1]):
            flag = True
            break
    return flag


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("1_input.txt")
m = open("1_output.txt", "w")

size = int(f.readline())
string = f.readline()
elements = list(map(str, string.split()))

if is_heap(elements, size):
    m.write("YES")
else:
    m.write("NO")


f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")