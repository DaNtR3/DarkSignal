from flask import session
from models.user_model import get_user_by_username


def AuthService(username, password):
    # If username or password is empty, terminate the process
    if not username or not password:
        return False
    # Find username
    user = get_user_by_username(username)
    
    # If user is not found
    if not user:
        return False
    
    #if user is found
    if (
        user["username"] == username
        and user["password"] == password
        and user["active"] == 1
        and user["locked"] == 0
    ):
        #Set session variables
        session["user"] = username
        SessionRoles(user)
        print(session)
        return True
    else:
        return False

def SessionRoles(user):
    valid_roles = {"SUPER_ORG_ADMIN", "ADMIN", "SIMULATOR", "END_USER"}
    role = user["role_name"]
    session["role"] = role if role in valid_roles else "END_USER"
    session["is_admin"] = role in {"ADMIN", "SUPER_ORG_ADMIN"}

def ActiveSession():
    return "user" in session



