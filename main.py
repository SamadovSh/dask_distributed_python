""""
First of all find 2 or more machines ( computers).
On both of them install the same version python and Dask.
After that, open a command line and type:

dask-scheduler

after that there will be a number like 'tcp://.....'
this is IP of tour cluster

On that machine (scheduler computer) open a command line again and type:
dask-worker tcp://... - this is your IP

the same thing ( dask-worker YOUR_IP) type on another computer in a command line
"""


import time
from dask.distributed import Client
from dask import delayed


@delayed
def slow(x, y):
    time.sleep(1)
    return x + y


client = Client('tcp://192.168.43.40:8786') # here your scheduler IP
# print(client.dashboard_link)

start = time.time()
l1, l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], []
for i in l1:
    a = slow(i, 1)
    l2.append(a)

total = sum(l2)
print(total.compute())
print(time.time() - start)
