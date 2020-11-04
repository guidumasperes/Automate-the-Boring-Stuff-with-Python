#open_links: open a set of links copied by user

import threading, re, pyperclip, webbrowser

def openLinks(stop): #Function to open links
    links = []
    while not stop(): #Run until receives a stop signal
        text = pyperclip.paste() #Copy link from clipboard
        if text not in links:
            linkRegex = re.compile(r'(www\..*)|(http://.*)|(.*\.com.*)') #Regex to detect if it's a link
            link = linkRegex.search(text)
            if link: #If it's a link append to links list
                link = link.group()
                print(text)
                links.append(text)
    for link in links: #Open links before exit
        webbrowser.open(link)

def main():
    print("Press ENTER to open your links!")
    stop_threads = False #To interrupt the openLinks thread
    p = threading.Thread(target=openLinks, args=(lambda : stop_threads,)) #Create thread
    p.start() #Start thread
    if input(): #If user types ENTER...
        pass
    stop_threads = True
    p.join() #...Stop thread

if __name__ == "__main__":
    main()