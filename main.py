from helpers import populateConfig
from helpers import printInputData
from files import checkSource
from files import downloadYTAudio
from audio import splitAudio

def main():
  try:
    initCheck = checkSource()
    if initCheck["code"] != 0:
      print("initCheck error")
      return initCheck["code"]
  except Exception as err:
    print(err)
    return -2

  userChoice = -1
  while userChoice != "0":
    userChoice = input("Please choose an action\n1 - Split File\n2 - Enter tracks data\n3 - Download Youtube audio\n\n0 - Exit\n\n")

    if userChoice == "2":
      print("To insert the tracks please follow this scheme for each song: Starting Time[mm.ss] Track name\nExample: 18:45 Afterthought \nThe entire tracklist must be a string\n\n")
      populateConfig()

    elif userChoice == "1":
      userConfirm = None
      printInputData()
      userConfirm = input("\nDo you want to proceed? Y/n\n")

      if userConfirm == "" or userConfirm == "y" or userConfirm == "Y":
        splitAudio(initCheck["data"])

    elif userChoice == "3":
      ytURL = input("\nInsert the Youtube URL:\n")
      downloadYTAudio(ytURL)

    elif userChoice == "0":
      print("Exiting...")
      return 0

    else:
      print("\nPlease choose a valid option\n")

if __name__ == "__main__":
  exit_code = main()
  import sys
  sys.exit(exit_code)