public class java_sensor_test_single {
    private static final int TASK_LENGTH = 5000000;
    private static final int NUM_SENSORS = 1326;

    private static int completed = 0;

    static class SensorTask {
        public void run() {
            double x = 1.0;

            for (int i = 0; i < TASK_LENGTH; i++) {
                x = x * 1.5 + 1.0;
            }

            completed++;
        }
    }

    public static void main(String[] args) throws InterruptedException {

        long startTime = System.nanoTime();

        SensorTask task = new SensorTask();
        for (int i = 0; i < NUM_SENSORS; i++) {
            task.run();
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