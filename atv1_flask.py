from flask import Flask

app = Flask(__name__) # inicio o flask

@app.route('/decorator') 
def explicacaoFlask():
    return 'O Flask é um framework leve para aplicações web WSGI. Ele foi projetado para facilitar e agilizar o início do desenvolvimento, com a capacidade de escalar para aplicações complexas.'

if __name__ == '__main__':
    app.run(debug=True)