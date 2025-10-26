
import requests
from src.handlers.hashing_handler import hash_password

BASE_URL = "https://api.pwnedpasswords.com/range/"

def HaveIbeenPwned(password):
    
    password_found = False
    
    print("The password lenght is: " + str(len(password)))

    hashed_password = hash_password(password)

    prefix = Get_preffix(hashed_password)

    suffix = Get_suffix(hashed_password)

    url = f"{BASE_URL}{prefix}"
        
    response = requests.get(url)
        
    partial_hashes = response.text.splitlines()
    for partial_hash in partial_hashes:
        response_suffix, response_count = partial_hash.split(':')
        if response_suffix == suffix:
            password_found = True
            break
    return password_found

def Get_preffix(hashed_password):
    loop_count = 0
    prefix = ""
    for letter in hashed_password:
        if loop_count >= 5:
            break
        prefix += letter
        loop_count += 1
    return prefix

def Get_suffix(hashed_password):
    start_from = 5
    suffix = ""
    for letter in range(start_from, len(hashed_password)):
        suffix += hashed_password[letter]
    return suffix

#HaveIbeenPwned("test")
#HaveIbeenPwned("&KxHv[4Dt'88meU")
