def password():
 
  count = 0
  while count < 5:
    remaining_attempts = 5 - count
    print(f"You have {remaining_attempts} attempts left!")  
    password = input("Enter the password: ")  

    if password == "toiyeubk":
      print("You are logged in to the system!")
      break
    else:
      print("Wrong password!")
      count += 1

  if count == 5:
    print("You are kicked off the system!!!")

if __name__ == "__main__":
  password()
