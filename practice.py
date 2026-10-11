print("------------------------")
print("PASSWORD CHECKER PROGRAM")

username = input("Enter a username")
password = input("Enter a password")

print()
choice = input("Your infos were saved do you want to login now (yes/no)").lower()
if choice == "yes":
      uncheck = input("Re-enter your usename ")
      pswdcheck = input("Re-enter your password ")

      if uncheck == username and pswdcheck == password:
            print("Acces garanted")
      elif uncheck == username and not pswdcheck == password:
            print("The password is incorrect")
      elif not uncheck == username and  pswdcheck == password:
                  print("The username is incorrect")
      else:
              print("Acces denied")
else :
        print("Thanks for trying this program")
        
