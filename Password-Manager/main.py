from cryptography.fernet import Fernet

# Key for encryption
'''
def write_key():
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
      key_file.write(key)

write_key()
'''

# Encryption/Decryption Settings
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

# View all passwords
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

# Add a password
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    # This way it automatically closes the file
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Deal with user input to view, add or quit
while True:
    mode = input(
        "Would you like to add a new password or view existing ones or quit (a/v/q)? ")

    if mode == "q":
        break
    elif mode == "a":
        add()
    elif mode == "v":
        view()
    else:
        print("Invalid mode.")
        continue
