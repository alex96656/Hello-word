# Simple Password Checker Simulation for Practice

PREDEFINED_PASSWORD = "Practice123!"

def main():
    print("=== Password Checker Simulation ===")
    password = input("Enter the password: ")

    if password == PREDEFINED_PASSWORD:
        print("Access granted! Password is correct.")
    else:
        print("Access denied! Incorrect password.")

if __name__ == "__main__":
    main()
