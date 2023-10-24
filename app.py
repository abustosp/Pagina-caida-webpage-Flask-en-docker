from flask import Flask, render_template, redirect, flash, request
# import sqlite3
# import webview
# import webbrowser
# from datetime import datetime

# Fila comentada para utilizar luego con webview
# app = Flask(__name__, template_folder='./templates', static_folder='./static')

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route("/")
def index():
    return render_template('index.html')



# EJECUCIÓN DEL PROGRAMA
if __name__ == '__main__':
    # webbrowser.open_new('http://127.0.0.1:5000/')
    # app.run(debug=True, host='contadoresonline.com.ar' , port='80')
    # app.run(debug=True, host='www.contadoresonline.com.ar' , port='80')
    app.run(debug=True, host='0.0.0.0')
    #app.run(debug=True, host='localhost' , port='80')
