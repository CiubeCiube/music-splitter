from helpers import populateConfig
from helpers import printInputData
from files import checkSource
from audio import splitAudio

def main():
  try:
    initCheck = checkSource()
    if initCheck["code"] != 0:
      return initCheck["code"]
  except Exception as err:
    print(err)
    return -2

  userChoice = -1
  while userChoice != "0":
    userChoice = input("Please choose an action\n1 - Enter tracks data\n2 - Split file\n0 - Exit\n")

    if userChoice == "1":
      print("To insert the tracks please follow this scheme for each song: Starting Time[mm.ss] Track name\nExample: 18:45 Afterthought \nThe entire tracklist must be a string\n\n")
      populateConfig()

    elif userChoice == "2":
      userConfirm = None
      printInputData()
      userConfirm = input("\n\nDo you want to proceed? y/N\n")

      if userConfirm == "y":
        splitAudio(initCheck["data"])

    elif userChoice == "0":
      print("Exiting...")
      return 0

    else:
      print("\nPlease choose a valid option\n")

if __name__ == "__main__":
  exit_code = main()
  import sys
  sys.exit(exit_code)