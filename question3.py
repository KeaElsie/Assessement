import os
import time
import requests

site = ["http://api.open-notify.org/astros.json"]
times = 15

total= 0
for i in range(len(site)):
    if total < times :
        start = time.time()
        end = time.time()
        print ('Hits:', times)
        s = requests.get(site[i])
        total = end - start
        print (" Total Time: ", total)
        print ('site:' , site[i])
        
        
