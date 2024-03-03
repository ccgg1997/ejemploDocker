import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Amin",
        "lastname": "Espinoza",
        "socialMedia":
        [
            {"facebookUser": "aminespinoza10"},
            {"instagramUser": "aminespinoza10"},
            {"xUser": "aminespinoza"},
            {"linkedin": "amin-espinoza"},
            {"githubUser": "aminespinoza10"}
        ],
        "blog": "https://aminespinoza.com",
        "author": "Miranda Espinoza"
    }
    return json.dumps(value)

#el puerto es el 5000 por default por eso cuando se de el docker run se debe de exponer el puerto 5000 ejemplo  docker run -it --rm -d -p 5000:5000 imagen-creada-antes

#para cambiar el puerto se debe de hacer lo siguiente, descomenta el siguiente codigo y cambia el puerto deseado
#if __name__ == '__main__':
#    app.run(port=puerto-deseado)