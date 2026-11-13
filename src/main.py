from flask import Flask
from flask import request
from matrix import Matrix
from matrix import Product

web = Flask(__name__)

A = Matrix(0, 0)
B = Matrix(0, 0)
C = Matrix(0, 0)

@web.route('/')
def set_size() -> str:
    text: str = ''

    with open('pages/index.html') as file:
        for line in file.readlines():
            text += line
   
    return text

@web.route('/matrix-input')
def matrix_input() -> str:
    text: str = ''

    with open('pages/matrix-input.html') as file:
        for line in file.readlines():
            text += line

    return text        

@web.route('/result')
def result() -> str:
    text: str = ''

    with open('pages/result.html') as file:
        for line in file.readlines():
            text += line

    return text