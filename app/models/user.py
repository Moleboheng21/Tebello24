from .. import mongo

class User:

    def register_user(client_data): 
       return  mongo.db.user.insert_one(client_data)
    
    def user_exist(email):
        return mongo.db.user.find_one({'$or':[{'email': email}]})
 
    def login_user(email, password): 
        return mongo.db.user.find_one({"email": email, "password": password})
    
    
    
    
    