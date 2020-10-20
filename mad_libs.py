#MadLibs: given a base file with a crazy statement, modify this file

import time, sys, threading, re, subprocess

def runMad(stop, temp, grams, words, choosen): #Function to print options for user
    print(grams)
    i = -1
    while not stop(): #Run until user types ENTER 
        i += 1
        if i == 3:
            i = 0
        temp.append(words[i])
        sys.stdout.write('\r'+str(words[i])) #Write to terminal overwriting the previous word
        sys.stdout.flush()
        time.sleep(0.5) #Give a short time to user sees the word
    choosen.append(words[i]) #Append the users word in a list

def main():
    i = -1 #Index to control grams and words flow
    choosen = [] #Ihe words choosed by the user
    grams = ["Enter an adjective:", "Enter a noun:", "Enter a verb:", "Enter a noun:"] #The sentences indicating what to choose
    words = [["silly", "dumb ", "crazy"],
             ["chandelier", "village   ", "moon   "],
             ["screamed    ", "regurgitated", "danced      "],
             ["pickup truck", "guy         ", "dinosaur    "]] #The groups of adjectives, nouns and verbs
    f = open(".\\text_files\\MadLibBase.txt", "r")
    print("You are going to mess out the following sentence: ")
    print()
    text = f.read()
    print(text)
    print()
    print("Ready? Hit ENTER on your keyboard to choose your word for every case")
    print()
    while i != 3: #Run until user chooses all words
        temp = [] #Auxiliary list, helps to choose the correct word
        i += 1
        stop_threads = False #To interrupt the runMad thread for a certain group
        p = threading.Thread(target=runMad, args=(lambda : stop_threads, temp, grams[i], words[i], choosen)) #Create thread
        p.start() #Start thread
        if input(): #If user types ENTER...
            pass
        stop_threads = True
        p.join() #...Stop thread
        print()
    for i in range(len(choosen)): #Remove white spaces
        choosen[i] = choosen[i].strip()
    adjRegex = re.compile(r'ADJECTIVE') #Define regexes
    text = adjRegex.sub(choosen[0],text) #Change the base words by the user words
    nounRegex = re.compile(r'NOUN')
    text = nounRegex.sub(choosen[1],text)
    verbRegex = re.compile(r'VERB')
    text = verbRegex.sub(choosen[2],text)
    othernoRegex = re.compile(r'OTHERNO')
    text = othernoRegex.sub(choosen[3],text)
    f1 = open(".\\text_files\\MadLibBaseMod.txt", "w")
    f1.write(text) #Write to a file
    f.close()      #Close all open files
    f1.close()

if __name__ == "__main__":
    main()
