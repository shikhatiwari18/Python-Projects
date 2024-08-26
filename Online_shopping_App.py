print("Script is starting...")

# Main code
import mysql.connector
import uuid
#Function to connect mysqldb
def connect_to_mysql():
    return mysql.connector.connect(
    host = "localhost",  
    user = "root",
    password = "MOMdad@86",
    database = "marketplace"
    )
# Function to generate unique session id    
def generate_session_id():
    return str(uuid.uuid4())
# Function to check credentials and return session id
def check_credentials(table,cursor,username,password):
    query = f"select id from {table} WHERE username = %s and password = %s"
    cursor.execute(query,(username,password))
    result = cursor.fetchone()
    if result:
        session_id = generate_session_id()
        update_query = f'UPDATE {table} SET session_id = %s where id = %s'
        cursor.execute(query,(session_id,result[0]))
        return session_id
    return None

#user_credentials = {"user1": "Password1", "user2": "Password2"}  # Example users
#admin_credentials = {
   # "admin1": "Password3",
    #"admin2": "Password4",
    #"shikha.tiwari18@gmail.com": "MOMdad@86" 
    #}
# Your credentials
def login():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    
    print("Welcome to shikha's Marketplace")
    print("please enter your details to login")

    role = input("Are you logging in as user or admin?").strip().lower()
    
    if role == "user":
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        
        session_id = check_credentials(cursor, "users",username,password)
        if session_id:
        #if userlogin in user_credentials and user_credentials[userlogin] == userpassword:
            print(f"Welcome {username} to shikha's Marketplace")
            print(f"session_ID: {session_id}")
        else:
            print("Invalid username or password")
            
    elif role == "admin":
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        #if adminlogin in admin_credentials and admin_credentials[adminlogin] == adminpassword:
        session_id = check_credentials(cursor,"admins",username,password)
        if session_id:
            print(f"Welcome {username} to shikha's Marketplace")
            print(f"Session_ID: {session_id}")
        else:
            print("Invalid username or password")
    else:
        print("Invalid role selected, please enter as a 'user' or 'admin'.")
  # close the cursor and connection
    cursor.close()
    connection.close()      
#calling function
login()
