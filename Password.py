def is_strong_password(password):
    # Conditions
    if (len(password) >= 8 and
        (c.isupper() for c in password) and
        (c.islower() for c in password) and
        (c.isdigit() for c in password) and
        (c in "@#$%&!" for c in password)):
        return True
    return False


# User input
pwd = input("Enter your password: ")

# Check password
if is_strong_password(pwd):
    print(" Strong password")
else:
    print(" Weak password - Please create a strong password")