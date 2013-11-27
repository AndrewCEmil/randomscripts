import sys
import logging

from optparse import OptionParser
try:
    from pymongo import MongoClient as Connection
except ImportException:
    from pymongo import Connection
logging.basicConfig(filename='ffgen.log', level=logging.DEBUG)
logger = logging.getLogger(__file__)

#args is a dict of the args
def main(options, args):
    jsonobj = None
    if args['json'] is not None:
        jsonobj = json_from_file(args['json'])   
    else:
        connstr = 'localhost'
        if args['mongoconnection']:
            connstr = args['mongoconnection']
        connstr += ':'
        if args['port'] is not None:
            connstr += ':' + args['port']
        else: 
            connstr += ':27017'
        conn = Connection(connstr)
        db = conn['test']
        if args['database'] is not None:
            db = conn[args['database']]
        coll = db['test']
        if args['collection'] is not None:
            coll = db[args['collection']]
        query = {}
        if args['query'] is not None:
            query = json.loads(args['query'])
        cursor = coll.find(query)
        if cursor.count() == 0:
            logger.error("count for query was 0")
            return
        jsonobj = cursor[0]
        if cursor.count() > 1:
            logger.warning("count for query was greater than 1, taking first")
    #at this point we have the json object, now we need to turn it into a file


def json_from_file(json_file_str):
    jsonstr = None
    if json_file_str == "-":
        #stdin case
        jsonstr = sys.stdin.read()
    else:
        jsonf = open(json_file_str)
        jsonstr = jsonf.read()
    if jsonstr is not None:
        json = json.loads(jsonstr)
        return json
    return None

if __name__ == "__main__":
    parser = OptionParser(usage="A program to convert json documents into flat\
files, json can be taken in from a file, \
stdin, or monobdb\n%prog [options]")
    parser.add_option("-c", "--collection", dest="collection", metavar="COLL",
                      help="collection to query, default is test")
    parser.add_option("-d", "--database", dest="database", metavar="DB",
                      help="database to query, default is test")
    parser.add_option("-j", "--json", dest="json", metavar="JSON", 
                      help="take input from json file, for stdin pass -, \
                      overrides any database options")
    parser.add_option("-m", "--mongoconn", dest="mongoconnection", 
                      metavar="URL", help="url for mongodb connection")
    parser.add_option("-o", "--outfile", dest="outfile", metavar="OUT",
                      help="file to write out out to, default to stdout")
    parser.add_option("-p", "--port", dest="port", metavar="PORT",
                      help="port for mongodb connection")
    parser.add_option("-q", "--query", dest="query", metavar="QUERY", 
                      help="query to find the document to be transformed into a \
                      flat file")
    (options, args) = parser.parse_args()
    main(options, args)
