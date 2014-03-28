var NUM_DOCS = 100000;
var NUM_FIELDS = 100;
var NUM_UPDATES = 100000;
var NUM_FIELDS_UPDATED = 10;

var coll = db.update_perf_test;
coll.drop();
//first we load up test data

var tmp = {};
for(var i=0;i<NUM_DOCS;i++) {
    tmp = {_id: i};
    for(var j=0; j<NUM_FIELDS; j++) {
        tmp[j.toString()] = Math.random();
    }
    coll.insert(tmp);
}

//now we roughly test performance of updates
var query = {};
var update = {};
var randField = 0;
var startt = Date.now();
for(i=0; i<NUM_UPDATES; i++) {
    query = {_id: (i % NUM_DOCS)}
    update = {}
    for(j=0; j<NUM_FIELDS_UPDATED; j++) {
        randField = Math.random() * NUM_FIELDS;
        update[randField.toString()] = Math.random();
    }
    update = {$set: update};
    coll.update(query, update);
    //db.getLastErrorObj();
}
var endt = Date.now();
print("start: " + startt);
print("end: " + endt);
var totalTime = endt - startt;
print("time elapsed: " + totalTime);
