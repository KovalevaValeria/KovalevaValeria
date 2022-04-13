import eulid
import flask
import math
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.context_processor
def inject_globals():
    return {
        "isclever": [
            "маленький",
            "глупый",
        ]
    }

@app.route('/hello/<string:text>')
@app.route('/hello')
def hello_world(text=None):
    return 'Just a plain text: "Hello from Flask!"' + (' With path .../' + text if text else '')


arg1=10
arg2 = 22
@app.route('/', methods = ['GET'])
def root():
    a, b = request.args.get('arg1'), request.args.get('arg2')
    if not a is None:
        global arg1
        arg1 = int(a)

    if not b is None:
        global arg2
        arg2 = int(b)
    islcm = ""
    if request.args.get('func')=="gcd":
        myvalue = "НОД равен" + str(eulid.gcd(arg1, arg2))
    else:
        myvalue = "НОК равен" + str(math.lcm(arg1, arg2))
        islcm = "selected"

    return flask.render_template(
        'index.html',
        myvalue = myvalue,
        myarg1 = arg1,
        myarg2 = arg2,
        islcm = islcm)




if __name__ == '__main__':
   app.run(debug = True)