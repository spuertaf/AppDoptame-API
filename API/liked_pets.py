import types
import firebase_admin
from firebase_admin import firestore, credentials



def get_likes_dict(likes_dict:dict, breed:str) -> dict:
    try:
        likes_dict[breed] += 1
    except KeyError as error:
        likes_dict[breed] = 1
    return likes_dict



def liked_pets_by_user(liked_posts:types.GeneratorType) -> dict or bool:
    assert isinstance(liked_posts, types.GeneratorType), f"liked_post must be type generator, not type {type(liked_posts)}"
    try:
        likes_dict = {}
        for post in liked_posts:
            post_values = post.to_dict()
            likes_dict = get_likes_dict(likes_dict, post_values['PET']['BREED'])
        return likes_dict
    except AssertionError as error:
        print(error)
        return False



def get_liked_posts_by_user(user_id:str, credentials_path:str)-> types.GeneratorType:
    try:
        db_credentials = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(db_credentials) #inicializo la conexion con la base de datos
        db_access = firestore.client()
        liked_posts = db_access.collection(u"post").where(u"LIKES",u"array_contains_any",[user_id]).stream()
        return liked_posts
    except ValueError as error:
        return False



def top3_liked_pets_by_user(user_id:str, credentials_path:str="credentials.json") -> dict:
    liked_posts = get_liked_posts_by_user(user_id, credentials_path)
    if liked_posts is False:
        return {"breed":"error getting liked posts by user"}
    liked_pets = liked_pets_by_user(liked_posts)
    if liked_pets is False:
        return {"breed":"error getting liked pets by user"}
    return liked_pets