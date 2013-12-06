from bottle import route, static_file, run

@route('/<filename:path>', method='GET')
def allroutes(filename):
    return static_file(filename, root='/mnt/workspace/mongo/testout')

run(host='0.0.0.0', port=8080)
