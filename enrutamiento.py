from flask import Flask, render_template 
app = Flask(__name__)

@app.route ('/')
def hola_mundo():
    return ('Hola Mundo!')

    
@app.route('/dojo')
def dojo():
    return "¡Dojo!"

@app.route('/say/<name>')
def Hola_flask(name):
    print(name)
    return "Hola, " + name 

@app.route('/repeat/<int:count>/<message>')
def repeat_message(count, message):
    repeated_message = message * count
    return repeated_message


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)