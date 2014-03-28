import math
import time
import pymongo
import random

from pprint import pprint

NUM_DOCS = 125000
NUM_FIELDS = 100
NUM_UPDATES = 125000
NUM_FIELDS_UPDATED = 10

client = pymongo.MongoClient();
coll = client['test']['update_test']

def load():
    for i in range(NUM_DOCS):
        tmp = {"_id": i}
        for j in range(NUM_FIELDS):
            tmp[str(j)] = random.random()
        coll.insert(tmp);

def drive():
    for i in range(NUM_UPDATES):
        query = {"_id": i % NUM_DOCS}
        update = {}
        for j in range(NUM_FIELDS_UPDATED):
            randfield = int(math.floor(random.random() * NUM_FIELDS))
            update[str(randfield)] = random.random()
        update = {"$set": update}
        coll.update(query, update)

def main(): 
    coll.drop()
    load()
    starttime = time.time()
    drive()
    endtime = time.time()
    print "start time: " + str(starttime)
    print "end time: " + str(endtime)
    print "time elapsed: " + str(endtime - starttime)


if __name__ == "__main__":
    main()
