public class java_sensor_test_multi {
    private static final int TASK_LENGTH = 10000000;
    private static final int NUM_SENSORS = 1326;

    private static final Object mutex = new Object();
    private static int completed = 0;

    static class SensorTask implements Runnable {
        @Override
        public void run() {
            double x = 1.0;

            for (int i = 0; i < TASK_LENGTH; i++) {
                x = x * 1.5 + 1.0;
            }

            synchronized (mutex) {
                completed++;
            }
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread[] threads = new Thread[NUM_SENSORS];

        SensorTask task = new SensorTask();
        
        long startTime = System.nanoTime();

        for (int i = 0; i < NUM_SENSORS; i++) {
            threads[i] = new Thread(task);
            threads[i].start();
        }

        for (int i = 0; i < NUM_SENSORS; i++) {
            threads[i].join();
        }

        long endTime = System.nanoTime();
        long delta = endTime - startTime;

        long seconds = delta / 1_000_000_000L;
        long nanoseconds = delta % 1_000_000_000L;

        System.out.println("Sensors: " + NUM_SENSORS);
        System.out.println("Completed: " + completed);
        System.out.printf("Time: %d.%09ds%n", seconds, nanoseconds);
    }
}