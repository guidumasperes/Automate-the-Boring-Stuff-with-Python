#This script finds the twitter users in your homepage. You aren't necessarily following the users.
#After hitting ctrl+A and ctrl+C just run the script and it prints out the users in console.

import pyperclip, re

#Write regex
userRegex = re.compile(r'@[^-\s]*')

#Copy from clipboard
text = str(pyperclip.paste())

#Find users
users = userRegex.findall(text)

#Print users
print("This users are in your feed: ")
for user in users:
    print(user)

