from .. import mongo

class User:

    def register_user(client_data): 
       return  mongo.db.user.insert_one(client_data)
   
    def register_admin(admin_data): 
       return  mongo.db.user.insert_one(admin_data)
    
    def user_exist(email):
        return mongo.db.user.find_one({'$or':[{'email': email}]})
 
    def login_user(email, password): 
        return mongo.db.user.find_one({"email": email, "password": password})
    
    
    def query_filter_by ( email,password):
         return mongo.db.user.check_password_hash({"email": email, "password": password})
        
        
        
  
  
    
    
    
    
    