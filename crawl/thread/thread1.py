import threading
from Queue import Queue
import time
import shutil

print_lock = threading.Lock()

def copy_op(file_data):
    with print_lock:
        print("Starting thread : {}".format(threading.current_thread().name))

    mydata = threading.local()
    mydata.ip, mydata.op = next(iter(file_data.items()))

    shutil.copy(mydata.ip, mydata.op)

    with print_lock:
        print("Finished thread : {}".format(threading.current_thread().name))

def process_queue():
    while True:
        file_data = compress_queue.get()
        copy_op(file_data)
        compress_queue.task_done()

compress_queue = Queue()

output_names = [{'jdk-1.tar.gz' : 'jdk-11.tar.gz'},{'jdk-2.tar.gz' : 'jdk-22.tar.gz'}]

for i in range(2):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

start = time.time()

for file_data in output_names:
    compress_queue.put(file_data)

compress_queue.join()

print("Execution time = {0:.5f}".format(time.time() - start))