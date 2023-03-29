import json
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
  


def delete():
    print("Enter the word you wanna delete: \n")
    wordToDelete = input()  # getting inpur from user
    myDictionary = open("./dictionary.txt", "r")
    allWords = myDictionary.readlines()
    flag = True
    for x in allWords:
        if f"{wordToDelete}:" in x:
            allWords.remove(x)
            dataFile = open('./dictionary.txt',"w")  #  writing into file.
            dataFile.writelines(allWords)
            dataFile.close()
            print(f"{bcolors.WARNING}Your given word deleted successfully.")
            flag = False
            myDictionary.close()
    if flag:
        myDictionary.close()
        print("The word you wanna delete is not found in the dictionary.")
        

def addWord():
    print("please enter the Word: ")
    word = input()
    word = word.lstrip().rsplit()[0]
    print("Please enter the Meaning of the Word you enterer: ")
    Meaning = input()
    dataFile = open('./dictionary.txt','a') 
    line = f"{word}:{Meaning}\n"
    dataFile.writelines(line)
    print(f"{bcolors.OKGREEN}Your word has been added successfully...{bcolors.ENDC}")

 



def operate(num):
    if num == 'c':
        searchWord()
    elif num == "a":
        addWord()
    else:
        print("You again entered the wrong code. please enter again press a or c.")
        num = input()
        operate(num)

