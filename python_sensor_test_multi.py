import threading
import time

TASK_LENGTH = 1000
completed = 0
lock = threading.Lock()

def sensor_task():
    x = 1.0
    global completed

    for i in range(TASK_LENGTH):
        x = x * 1.5 + 1.0
    
    with lock:
        completed += 1

NUM_SENSORS = 1326
threads = []
start = time.time()

for i in range(NUM_SENSORS):
    thread = threading.Thread(target=sensor_task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print(f"Sensors: {NUM_SENSORS}")
print(f"Completed: {completed}")
print(f"Time: {(end-start):.9f}s")
