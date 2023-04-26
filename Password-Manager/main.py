pwd = input("What is the master password? ")
master_password = "123"

if pwd != master_password:
    print("Incorrect master password")
    quit()

def view():
  with open('password.txt', 'r') as f:
    for line in f.readlines():
       data = line.rstrip()
       user, passw = data.split("|")
       print("User:", user + ",", "Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # This way it automatically closes the file
    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
        

while True:
  mode = input("Would you like to add a new password or view existing ones or quit (a/v/q)? ")

  if mode == "q":
      break
  elif mode == "a":
      add()
  elif mode == "v":
      view()
  else:
      print("Invalid mode.")
      continue