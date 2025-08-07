import threading
import time

# Shared data
dataStart = 0
dataLimit = 10

# Lock for synchronizing access to shared data
lock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    global lock
    while True:
        # Acquire the lock before accessing shared data
        with lock:
            if dataStart <= dataLimit:
                print(f"Thread {thread} accessing dataStart: {dataStart}")
                dataStart += 1
            else:
                break
        # Simulate some processing time
        time.sleep(0.1)

# Create and start threads
threads = []
for i in range(3):  # Let's say we want to use 3 threads
    t = threading.Thread(target=getData, args=(dataStart, dataLimit, i))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads have finished execution.")