import pymongo

from optparse import OptionParser

def main(options, args):
    print dir(options)
    print dir(args)
    print options
    print args

if __name__ == "__main__":
    parser = OptionParser(usage="A program to convert json documents into flat\
files, json can be taken in from a file, \
stdin, or monobdb\n%prog [options]")
    parser.add_option("-m", "--mongoconn", dest="mongoconnection", 
                      metavar="URL", help="url for mongodb connection")
    parser.add_option("-p", "--port", dest="port", metavar="PORT",
                      help="port for mongodb connection")
    parser.add_option("-d", "--database", dest="database", metavar="DB",
                      help="database to query")
    parser.add_option("-c", "--collection", dest="collection", metavar="COLL",
                      help="collection to query")
    parser.add_option("-q", "--query", dest="query", metavar="QUERY", 
                      help="query to find the document to be transformed into a \
                      flat file")
    parser.add_option("-j", "--json", dest="json", metavar="JSON", 
                      help="take input from json file, for stdin pass -, \
                      overrides any database options")
    (options, args) = parser.parse_args()
    main(options, args)
