import os

def writeDataToFile(path, name, address, phone):
  userFileName = input("Enter filename: ")
  with open(userFileName, 'a') as f:
    f.write("{},{},{}".format(name, address, phone))
  f.close()
  print("Data stored successfully!")
      

def main():
  while (True):

    while (True):
      user_name = input("Please enter your name: ")
      user_address = input("Please enter your address: ")
      user_phone = input("Please enter your phone number: ")

      print("You have entered {}, {}, {}.".format(user_name, user_address, user_phone))

      qEntryVerify = input("Is the information you entered accurate? y or n")

      if qEntryVerify == "y":
        break;

    qStore = input("Store data? y or n")

    if qStore == "y":
      print("Where would you like to store this data?")
      print("Current directory: {}".format(os.getcwd()))

      qDirVerify = input("Save in current directory? y or n")

      if qDirVerify == "y":
        path = os.getcwd()
        writeDataToFile(path, user_name, user_address, user_phone)
      else:
        userPath = input("Enter path to the directory you want to save the file to: ")
        
      


if __name__ == "__main__":
  main()