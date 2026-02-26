from flask import request
import mysql.connector
import re #Regular expressions also called Regex

##############################
def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",  
            password = "password",
            database = "2026_1_backend"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Database under maintenance", 500)

##############################
# USER_FIRST_NAME_MIN = 2         #Det er med stort da det er en const in python
# USER_FIRST_NAME_MAX = 20

# def validate_user_first_name():
#     user_first_name = request.form.get("user_first_name", "").strip()
#     if len(user_first_name) < USER_FIRST_NAME_MIN:
#         raise Exception(f"User first name ninimun {USER_FIRST_NAME_MIN} characters", 400)
#     if len(user_first_name) > USER_FIRST_NAME_MAX:
#         raise Exception(f"User first name ninimun {USER_FIRST_NAME_MAX} characters", 400)
#     return user_first_name

# #one action for one function - that is what Santiago likes - make it simpel

##############################
USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20
# ^.{2,20}$ <- venstre side er som at skrive det på højre side -> f"^.{{{USER_FIRST_NAME_MIN},{USER_FIRST_NAME_MAX}}}$"
USER_FIRST_NAME_MAX_REGEX = f"^.{{{USER_FIRST_NAME_MIN},{USER_FIRST_NAME_MAX}}}$"
def validate_user_first_name():
    user_first_name = request.form.get("user_first_name", "").strip()  
    if not re.match(USER_FIRST_NAME_REGEX, user_first_name): 
        raise Exception(f"--error-- user_first_name")  

    return user_first_name

##############################
USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20
def validate_user_last_name():
    user_last_name = request.form.get("user_last_name", "").strip()
    if len(user_last_name) < USER_LAST_NAME_MIN:
        raise Exception(f"User last name minimum {USER_LAST_NAME_MIN } characters", 400)
    if len(user_last_name) > USER_LAST_NAME_MAX:
        raise Exception(f"User last name maximum {USER_LAST_NAME_MAX } characters", 400)    
    return user_last_name


##############################
USER_USERNAME_MIN = 2
USER_USERNAME_MAX = 20
USER_USERNAME_REGEX = f"^.{{{USER_USERNAME_MIN},{USER_USERNAME_MAX}}}$"
def validate_user_username():
    user_username = request.form.get("user_username", "").strip()
    if not re.match(USER_USERNAME_REGEX, user_username):    #if the rule does not match then
        raise Exception("--error-- user_username")          #there is a error in the first name and app.py fix it - line 88 in app.py
    return user_username



