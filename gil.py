import threading
import time

# A CPU-heavy task (calculating the sum of numbers)
def cpu_bound_task():
    total = 0
    for i in range(1, 10**7):
        total += i
    print(f"Task finished with total: {total}")

# Create two threads to run the task
thread1 = threading.Thread(target=cpu_bound_task)
thread2 = threading.Thread(target=cpu_bound_task)

# Start the threads
start_time = time.time()
thread1.start()  # Start the first thread
thread2.start()  # Start the second thread

# Wait for both threads to finish
thread1.join()  
thread2.join()

end_time = time.time()

print(f"Total time with threads: {end_time - start_time:.4f} seconds")
print("******************")
import multiprocessing
import time

# A CPU-heavy task
def cpu_bound_task():
    total = 0
    for i in range(1, 10**7):
        total += i
    print(f"Task finished with total: {total}")

# Create two processes to run the task
process1 = multiprocessing.Process(target=cpu_bound_task)
process2 = multiprocessing.Process(target=cpu_bound_task)

# Start the processes
start_time = time.time()
process1.start()  # Start the first process
process2.start()  # Start the second process

# Wait for both processes to finish
process1.join()
process2.join()

end_time = time.time()

print(f"Total time with processes: {end_time - start_time:.4f} seconds")
print("**********************")
class MyClass:
    def instance_method(self):
        print("This is an instance method.")
        print(f"Instance attribute: {self}")

obj = MyClass()
obj.instance_method()  # Call using an instance
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

MyClass.static_method()  # Call using the class
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

MyClass.static_method()  # Call using the class