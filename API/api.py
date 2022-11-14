from flask import Flask, request
from liked_pets import top3_liked_pets_by_user



'''
/dog-race : ruta de la api para reconocimiento de raza de un perro
/recommendation : ruta de la api para recomendacion de razas de perros
'''



if __name__ == '__main__':


    
    app = Flask(__name__)



    @app.route("/recommendation") #ruta de la api para recomendacion de mascota
    def get_recommendation():
        user_id = request.args.get('user_id', default =1, type = str)
        response = top3_liked_pets_by_user(user_id, "credentials.json")
        return response
    


    app.run(host = '10.128.0.5',port = 80, debug = True) 
