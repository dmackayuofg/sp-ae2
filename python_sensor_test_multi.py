import threading
import time

TASK_LENGTH = 10000000
completed = 0
lock = threading.Lock()

def sensor_task():
    x = 1.0
    global completed

    for i in range(TASK_LENGTH):
        x = x * 1.5 + 1.0
    
    with lock:
        completed += 1

n = 1326
threads = []
start = time.time()

for i in range(n):
    thread = threading.Thread(target=sensor_task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print(f"Sensors: {n}")
print(f"Completed: {completed}")
print(f"Time: {end-start}s")