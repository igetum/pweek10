"""
Antone Cabral
5/11/2020

Assignment Week 10

Filename: main.py

Purpose:
This program takes in user name, phone, and addresses as stores the information in the directory and file of their choosing.
"""

import os


def main():

  print("Contact Data Store")
  print("------------------------------------")

  #Application Loop
  while (True):

    #Information Input Loop
    while (True):
      user_name = input("\nPlease enter your name: ")
      user_address = input("Please enter your address: ")
      user_phone = input("Please enter your phone number: ")

      print("\nYou have entered {}, {}, {}.".format(user_name, user_address, user_phone))

      #Asks users if information is correct, breaks out otherwise
      qEntryVerify = input("\nIs the information you entered accurate? y or n: ")
    
      if qEntryVerify == "y":
        break;

    #Asks users if they want to store that data
    qStore = input("\nStore data? y or n: ")

    if qStore == "y":

      #Path input Loop
      while (True):
        path = os.getcwd()
        print("\nWhere would you like to store this data?")
        print("Current directory: {}".format(path))

        qDirVerify = input("\nSave in current directory? y or n: ")

        if qDirVerify == "y":
          break

        else:
          userPath = input("\nEnter path to the directory you want to save the file to: ")
    
          try: #tries and change directory to path, if it does not exist then it I ask to create the directory.
            os.chdir(userPath)
          except:
            print("Path does not exists.")
            qCreateDir = input("Do you want to create the new directory? y or no: ")

            if qCreateDir == "y":

              #Makes directory and changes path of console to that path
              os.mkdir(userPath)
              os.chdir(userPath)
              break

      #Write content to file passing in path and user information.
      writeDataToFile(path, user_name, user_address, user_phone)


    runApp = input("\nEnter more data? y or n: ")
    if runApp == "n":
      break
    
    continue


    
  print("\nExisting Program...")
        
  
#writeDataToFile takes the path and user information and writes to file.
def writeDataToFile(path, name, address, phone):

  userFileName = input("\nEnter filename: ")

  with open(userFileName, 'a') as f:
    f.write("{},{},{}\n".format(name, address, phone))
  f.close()

  print("\nData stored successfully!")
      

if __name__ == "__main__":
  main()