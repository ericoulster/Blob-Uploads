from github import Github
from string import ascii_lowercase
import random
from datetime import datetime
import os

#put your credentials here
g = Github("github-username", "github-password")


def randomString(stringLength=20):
    letters = ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# put your repo here
repo = g.get_repo("ericoulster/Blob-Uploads")

def fileload():
    x = randomString(4)
    y = randomString(30)
    dt = datetime.now()
    with open(str(x)+'.txt', 'w+') as f:
        f.write(str(dt) + '\n' + y)
    f.close()
    repo.create_file(str(dt) + str(x) + '.txt', 'blob', str(dt) + '.txt')
    os.remove(str(x) + '.txt')


if datetime.today().weekday() < 5:
    for i in range(random.randint(3,6)):
        fileload()
else:
    for i in range(random.randint(0,1)):
        fileload()

