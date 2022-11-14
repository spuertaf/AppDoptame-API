from flask import Flask
from usable_model import prediction
from flask import request
from liked_pets import top3_liked_pets_by_user



'''
/dog-race : ruta de la api para reconocimiento de raza de un perro
/recommendation : ruta de la api para recomendacion de razas de perros
'''



if __name__ == '__main__':


    
    app = Flask(__name__)



    @app.route("/dograce") #ruta de la api para deteccion de raza de un perro
    #una vez se acceda a la ruta se va a ejecutar esto
    def model_prediction():
        try:
            print("Prediciendo la raza de la foto...")
            img_path = request.args.get('url', default = 1, type = str)
            predict = prediction(img_path)
            print(f"La raza es {predict}")
        except Exception as error:
            print(error)
            predict = f"STATUS CODE: 400 \nError en la prediccion"
        return {"race":predict}
    
    
    
    @app.route("/recommendation") #ruta de la api para recomendacion de mascota
    def get_recommendation():
        user_id = request.args.get('user_id', default =1, type = str)
        response = top3_liked_pets_by_user(user_id, "")
        return response
    


    app.run(host = '0.0.0.0',port = 80, debug = True) 
