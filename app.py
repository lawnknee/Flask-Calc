from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

OPERATIONS = {
    "add" : add,
    "sub" : sub,
    "div" : div,
    "mult" : mult
}

@app.route('/math/<operation>')
def big_math(operation):
    """Takes in numbers a, b, and operation from URL query
    performs operation on a and b"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(OPERATIONS[operation](a,b))

@app.route('/add')
def add_nums():
    """Add numbers a and b given from URL query"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/sub')
def sub_nums():
    """Subtract number b from a given from URL query"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/div')
def div_nums():
    """Divide number a by b given from URL query"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))


@app.route('/mult')
def mult_nums():
    """Multiply numbers a and b given from URL query"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))