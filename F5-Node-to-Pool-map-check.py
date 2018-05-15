from f5.bigip import ManagementRoot
import certifi
import urllib3
import requests
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

##Below lines open a file which contains the node names, reads it and stores it in a list##

x_file = open('/usr/local/bin/python_scripts/nodes.txt', 'r')
r=list()
for i in x_file:
    i=i.split('\n',1)[0]
    r.append(i)
x_file=open('nodes.txt', 'r')

## Below lines Connect to the BigIP##
mgmt = ManagementRoot("ip_address", "username", "password")
x_file=open('nodes.txt', 'r')

# Below lines Get a list of all pools on the BigIP and print their names and their
# members' names

pools = mgmt.tm.ltm.pools.get_collection()

##Below lines will print pool and pool members##

dict={}

#for pool in pools:
#     s=pool.name
#     print "Pool is:{} ".format(s)
#     for member in pool.members_s.get_collection():
#         t=member.name
#         print "members are: {}".format(t)

##Below lines will compare the list elements (which were read from a file earlier) in the file and the nodes in the F5, choose the Pool related to the F5 and print out both the Pool and Node name##

for pool in pools:
    test=list()
    t=list()
    u=list()
    for member in pool.members_s.get_collection():
          test.append((member.name).encode("utf-8"))
    for line in r:
        for i in test:
            if line in i: t.append(line)
        else: continue
    for i in t:
        if i in u: continue
        else: u.append(i)        
    dict[pool.name]=u

for k,v in dict.items():
    print k,v
