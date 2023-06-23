# main.py

import PySimpleGUI as sg
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        greeting = f"Hello, {name}!"
        return render_template('index.html', greeting=greeting)
    return render_template('index.html')

def run_gui():
    layout = [
        [sg.T('Go')],
        [sg.Text('Enter your name:'), sg.Input(key='name')],
        [sg.Button('Submit')]
    ]

    window = sg.Window('Greeting App', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Submit':
            name = values['name']
            response = app.test_client().post('/', data={'name': name})
            greeting = response.get_data(as_text=True)
            sg.popup(greeting)

    window.close()

if __name__ == '__main__':
    app.run(debug=True)

