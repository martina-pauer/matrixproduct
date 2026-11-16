from flask import Flask
from flask import request
from matrix import Matrix
from matrix import Product

web = Flask(__name__)

A = Matrix(0, 0)
B = Matrix(0, 0)
C = Matrix(0, 0)

@web.route('/', methods = ['GET', 'POST'])
def set_size() -> str:
    text: str = ''

    with open('pages/index.html') as file:
        for line in file.readlines():
            text += line
            
    if request.method == 'POST':
        A = Matrix(int(request.form['first-rows']), int(request.form['first-columns']))
        B = Matrix(int(request.form['second-rows']), int(request.form['second-columns']))
        C = Matrix(A.matrix.__len__(), B.matrix[0].__len__())
        text.replace('"POST"', '"POST" action = "matrix-input"')

    return text

@web.route('/matrix-input')
def matrix_input() -> str:
    text: str = ''
    
    with open('pages/matrix-input.html') as file:
        for line in file.readlines():
            text += line
            
    A_components = ''
    
    for rows in range(0, A.matrix.__len__()):
        for columns in range(0, A.matrix[0].__len__):
            A_components += f'<input type = "text" id = "a{rows}{columns}" />'
            if request.method == 'POST':
                A.add_component(int(request.form[f'a{rows}{columns}']))
                
    B_components = ''
    
    for rows in range(0, B.matrix.__len__()):
        for columns in range(0, B.matrix[0].__len__):
            B_components += f'<input type = "text" id = "b{rows}{columns}" />'
            if request.method == 'POST':
                B.add_component(int(request.form[f'b{rows}{columns}']))
                
    text = text.replace('[A Components]', A_components)
    text = text.replace('[B Components]', B_components)

    if request.method == 'POST':
        text.replace('"POST"', '"POST" action = "result"')
        
    return text        

@web.route('/result')
def result() -> str:
    text: str = ''

    with open('pages/result.html') as file:
        for line in file.readlines():
            text += line

    return text
