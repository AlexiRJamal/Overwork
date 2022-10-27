from multiprocessing import Pool
import psutil
import time
def f(x):
    set_time = 1
    timeout = time.time() + 60*float(set_time)  # X minutes from now
    while True:
        if time.time() > timeout:
            break

processes = psutil.cpu_count()
print ('utilizing %d cores\n' % processes)
pool = Pool(processes)
pool.map(f, range(processes))