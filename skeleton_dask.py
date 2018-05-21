from dask.distributed import Client
from functions import add, inc, dec, whitespace
 
#initalize client from script and automatically allocate workers 
client = Client()
print (client)

#alternatively run "dask-scheduler" in linux and allocate "dask-workers"
#seperately then point script to scheduler
#client = Client('127.0.0.1:8786')

#Monitor on local machine 
# http://localhost:8787/status

#Use the map and submit methods to launch functions to the scheduler

x = client.submit(inc, 10)

y = client.submit(dec, 10)

z = client.submit(add, 10,10)

w = client.submit(whitespace, "sammy has a balloon")

L = client.map(inc, range(20))

#The map/submit functions return Future objects, lightweight tokens that refer to results on the cluster. 
#By default the results of computations stay on the cluster in memory.

#Gather results to your local machine either with the Future.result method for a single future 
#or with the Client.gather method for many futures at once (using map).

x.result()

w.result()

client.gather(L)

#long running processes can be canceled
#client.cancel(L)

#Close this client, Clients will also close automatically when your Python session ends
client.close()