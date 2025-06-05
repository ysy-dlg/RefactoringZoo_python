def register_user(name, email):
    if not name or not email:
        print("Invalid input")
        return

    if "@" not in email:
        print("Invalid email")
        return

    print(f"Registering user: {name}")
    # Simulate DB insert
    print(f"Inserting into DB: {name}, {email}")
