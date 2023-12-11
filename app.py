from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        palabra_clave = request.form['palabra_clave']
        imagenes = obtener_imagenes_giphy(palabra_clave)
        return render_template('resultado.html', imagenes=imagenes)
    
    return render_template('resultado.html')

def obtener_imagenes_giphy(palabra_clave, api_key='hEm5eEcEkKlQPpJzcV4ZFW1XxpeR9T9M', cantidad=10):
    endpoint = 'https://api.giphy.com/v1/gifs/search'
    parametros = {
        'q': palabra_clave,
        'api_key': api_key,
        'limit': cantidad
    }

    try:
        respuesta = requests.get(endpoint, params=parametros)
        respuesta.raise_for_status()
        datos = respuesta.json()

        imagenes = []
        for gif in datos['data']:
            url_imagen = gif['images']['fixed_height']['url']
            imagenes.append(url_imagen)

        return imagenes

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return []

if __name__ == '__main__':
    app.run(debug=True)