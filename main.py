import os


def main():

  print("Contact Data Store")
  print("------------------------------------")

  while (True):

    while (True):
      user_name = input("\nPlease enter your name: ")
      user_address = input("Please enter your address: ")
      user_phone = input("Please enter your phone number: ")

      print("\nYou have entered {}, {}, {}.".format(user_name, user_address, user_phone))

      qEntryVerify = input("\nIs the information you entered accurate? y or n: ")

      if qEntryVerify == "y":
        break;

    qStore = input("\nStore data? y or n: ")

    
    if qStore == "y":

      while (True):
        path = os.getcwd()
        print("\nWhere would you like to store this data?")
        print("Current directory: {}".format(path))

        qDirVerify = input("\nSave in current directory? y or n: ")

        if qDirVerify == "y":
          break

        else:
          userPath = input("\nEnter path to the directory you want to save the file to: ")
    
          try:
            os.chdir(userPath)
          except:
            print("Path does not exists.")
            qCreateDir = input("Do you want to create the new directory? y or no: ")

            if qCreateDir == "y":
              os.mkdir(userPath)
              os.chdir(userPath)
              break

      writeDataToFile(path, user_name, user_address, user_phone)
      break

    elif (qStore == "n"):
      break

    
  print("\nExisting Program...")
        
  
def writeDataToFile(path, name, address, phone):

  userFileName = input("\nEnter filename: ")

  with open(userFileName, 'a') as f:
    f.write("{},{},{}\n".format(name, address, phone))
  f.close()

  print("\nData stored successfully!")
      

if __name__ == "__main__":
  main()