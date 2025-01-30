from flask import Flask, render_template, request

app = Flask(__name__)

# Datos simulados de centros comerciales en varias ciudades
SHOPPING_DATA = {
    "madrid": [
        "Centro Comercial La Vaguada",
        "Gran Plaza 2",
        "Plenilunio",
        "Príncipe Pío",
        "Centro Comercial Madrid Sur"
    ],
    "barcelona": [
        "Diagonal Mar",
        "Maremagnum",
        "L'illa Diagonal",
        "La Maquinista",
        "Glòries"
    ],
    "valencia": [
        "Bonaire",
        "Aqua Multiespacio",
        "Nuevo Centro",
        "El Saler"
    ],
    "sevilla": [
        "Nervión Plaza",
        "Los Arcos",
        "Lagoh",
        "Torre Sevilla"
    ]
}

@app.route('/')
def home():
    """ Página inicial: formulario para ingresar ciudad """
    return render_template('home.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    """ Procesa la búsqueda de centros comerciales en una ciudad """
    ciudad = request.form.get('ciudad', '').strip().lower()

    if not ciudad:
        return render_template('malls.html',
                               error="Por favor ingresa una ciudad.",
                               malls=[])

    # Buscamos en nuestro diccionario
    if ciudad in SHOPPING_DATA:
        malls = SHOPPING_DATA[ciudad]
        return render_template('malls.html',
                               error=None,
                               city=ciudad.title(),
                               malls=malls)
    else:
        # Ciudad no encontrada
        return render_template('malls.html',
                               error=f"No hay datos de centros comerciales para '{ciudad}'.",
                               malls=[])

# No ejecutamos app.run() aquí porque Gunicorn lo manejará
