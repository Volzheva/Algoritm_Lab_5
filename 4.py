import time
import os, psutil


def swap(arr, a, i, answer_arr):
    n = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < a and arr[i] > arr[left]:
        n = left
    if right < a and arr[n] > arr[right]:
        n = right
    if n != i:
        arr[i], arr[n] = arr[n], arr[i]
        answer_arr.append([i, n])
        swap(arr, a, n, swaps)


def heapsort(arr, answer_arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        swap(arr, len(arr), i, answer_arr)


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("4_input.txt")
m = open("4_output.txt", "w")

size = int(f.readline())
string = f.readline()
elements = list(map(str, string.split()))
swaps = []

heapsort(elements, swaps)

m.write(str(len(swaps)) + "\n")
for each in swaps:
    m.write(f"{each[0]} {each[1]} \n")


f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")