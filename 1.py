import time
import os, psutil


def is_heap(arr, size_arr):
    for i in range(size_arr//2):
        main = arr[i]
        child_1_index = 2*i
        child_2_index = 2*i+1
        if child_1_index < size_arr and child_2_index < size_arr:
            first_child, second_child = arr[child_1_index], arr[child_2_index]
            if first_child >= main and second_child >= main:
                continue
            else:
                return False
    return True


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