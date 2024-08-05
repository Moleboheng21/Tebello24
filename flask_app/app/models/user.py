from .. import mongo



class User:

    def register_user(cust_data): 
        mongo.db.user.insert_one(cust_data)
        return str("cust_user")
    
    def user_exist(email):
        return mongo.db.user.find_one({'$or':[{'email': email}]})
 
    def login_user(email, password): 
        return mongo.db.user.find_one({"email": email, "password": password})