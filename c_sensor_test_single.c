#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define TASK_LENGTH 500000

int completed = 0;

void* sensor_task() {
    double x = 1.0;

    for (int i = 0; i < TASK_LENGTH; i++) {
        x = x * 1.5 + 1.0;
    }

    completed++;

    return NULL;
}

enum { NS_PER_SECOND = 1000000000 };

void sub_timespec(struct timespec t1, struct timespec t2, struct timespec *td)
{
    td->tv_nsec = t2.tv_nsec - t1.tv_nsec;
    td->tv_sec  = t2.tv_sec - t1.tv_sec;
    if (td->tv_sec > 0 && td->tv_nsec < 0)
    {
        td->tv_nsec += NS_PER_SECOND;
        td->tv_sec--;
    }
    else if (td->tv_sec < 0 && td->tv_nsec > 0)
    {
        td->tv_nsec -= NS_PER_SECOND;
        td->tv_sec++;
    }
}

int main() {

    int n = 1326;

    struct timespec start, finish, delta;
    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int i = 0; i < n; i++) {
        sensor_task();
    }

    clock_gettime(CLOCK_MONOTONIC, &finish);
    sub_timespec(start, finish, &delta);

    printf("Sensors: %d\n", n);
    printf("Completed: %d\n", completed);
    printf("Time: %d.%.9lds\n", (int)delta.tv_sec, delta.tv_nsec);

    return 0;

}