def ReplitLoginSystem():
  while True:
    userName = input("What is your Username?: ")
    passWord = input("Please enter Password: ")

    if userName == "David" and passWord == "Replit4ever":
      print("Welcome David")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
      
print("Replit Login System")
ReplitLoginSystem()