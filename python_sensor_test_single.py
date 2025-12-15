import time

TASK_LENGTH = 500000
completed = 0

def sensor_task():
    x = 1.0
    global completed

    for i in range(TASK_LENGTH):
        x = x * 1.5 + 1.0

    completed += 1

n = 1326
threads = []
start = time.time()

for i in range(n):
    sensor_task()

end = time.time()

print(f"Sensors: {n}")
print(f"Completed: {completed}")
print(f"Time: {end-start}s")
