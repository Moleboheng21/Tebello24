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
    
    def __init__(self, email, name, surname, password, role):
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.role = role

    def save(self):
        mongo.db.users.insert_one({
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            "password": self.password,
            "role": self.role
        })
    
    
    def find_by_email(email):
        user_data = mongo.db.users.find_one({"email": email})
        if user_data:
            return User(
                email=user_data['email'],
                name=user_data['name'],
                surname=user_data['surname'],
                password=user_data['password'],
                role=user_data['role']
            )
        return None
    
    # def query_filter_by ( email,password):
    #      return mongo.db.user.check_password_hash({"email": email, "password": password})
        
        
        
  
  
    
    
    
    
    