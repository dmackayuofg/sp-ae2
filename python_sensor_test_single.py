import time

TASK_LENGTH = 10000000
completed = 0

def sensor_task():
    x = 1.0
    global completed

    for i in range(TASK_LENGTH):
        x = x * 1.5 + 1.0

    completed += 1

NUM_SENSORS = 1326
start = time.time()

for i in range(NUM_SENSORS):
    sensor_task()

end = time.time()

print(f"Sensors: {NUM_SENSORS}")
print(f"Completed: {completed}")
print(f"Time: {(end-start):.9f}s")
