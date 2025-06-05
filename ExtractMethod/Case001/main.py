def register_user(name, email):
    if not is_valid_input(name, email):
        print("Invalid input")
        return

    print(f"Registering user: {name}")
    insert_to_db(name, email)

def is_valid_input(name, email):
    if not name or not email:
        return False
    if "@" not in email:
        return False
    return True

def insert_to_db(name, email):
    print(f"Inserting into DB: {name}, {email}")
