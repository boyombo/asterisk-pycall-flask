from pycall import CallFile, Call, Application
from flask import Flask, request
import logging

app = Flask(__name__)


@app.route("/")
def test():
    return "hello world"


@app.route("/call")
def localcall():
    call_from = request.args.get('from', '')
    call_to = request.args.get('to', '')
    if call_from and call_to:
        cfrom = 'SIP/{}'.format(call_from)
        logging.debug(cfrom)
        cto = 'SIP/{}'.format(call_to)
        logging.debug(cto)
        c = Call(cfrom)
        a = Application('Dial', cto)
        cf = CallFile(c, a)
        cf.spool()
    else:
        return "no call made"
    return "call made"


@app.route("/dialout")
def dialout():
    call_from = request.args.get('from', '')
    call_to = request.args.get('to', '')
    cfrom = 'SIP/{}@hotvoip'.format(call_from)
    cto = 'SIP/{}@hotvoip'.format(call_to)
    c = Call(cfrom)
    a = Application('Dial', cto)
    cf = CallFile(c, a)
    cf.spool()
    return 'dialed'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
