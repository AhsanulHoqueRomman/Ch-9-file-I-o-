#1. A program to read the text from a file "poem.txt" and find out whether it contains the word "Twinkle".
'''f= open("poem.txt")

content= f.readline()

if("twinkle in content"):
    print("The word twinkle is present in the content.")

else:    
    print("The word twinkle is not present in the content.")

f.close()'''


#2.The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.


'''
import random

def game():
    print("You are playing the game.")
    score = random.randint(1, 99)

    #Fetching the hi-score:

    with open("hi-score.txt") as f:
        hiscore= f.read()
        if(hiscore != ""):
            hiscore= int(hiscore)
        
        else:
            hiscore=0
    
    print(f"Your score is: {score}")

    if(score>hiscore):
        #Writing the highscore in the "hi-score" file.

        with open("hi-score.txt", "w") as f:
            f.write(str(score) )
        

    return score

    
game()

'''

#3. a program to generate multiplication tables from 2 to 20 and write it to the different files.
#  Place these files in a folder for a 13 – year old.

'''

def generateTables(n):
    table= ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    with open(f"Tables/table_of_{n}.txt" , "w") as f:
        f.write(table)



for i in range(2, 21):
    generateTables(i)


'''

#4. A file contains a word “Donkey” multiple times.Write a program which replace this word with ##### by updating the same file.

'''

with open("file.txt") as f:
    content= f.read()

contentNew= content.replace("Donkey","#####")

with open("file.txt", "w") as f:
    content= f.write(contentNew)

'''


#5. Repeat problem 4 for a list of such words to be censored.

'''
words= ["Donkey", "Monkey", "Konkey"]

with open("file.txt") as f:
    content = f.read()

for i in words:
    content = content.replace(i, "#"*len(i))

with open("file.txt", "w") as f:
    content = f.write(content)

'''

#6. A program to mine a log file and find out whether it contains ‘python’.

'''
with open("log.txt") as f:
    content = f.read()
    
if ("Python" in content):
    print("Yes,Python is present!")
else:
    print("No,Python is not present!")

'''


#7.A program to find out the line number where python is present from problem 6.

'''

with open("log.txt") as f:
    content = f.readlines()

lineno=1
for line in content:
    if ("Python" in line):
        print(f"Yes,Python is present! Line no:{lineno}")
        break
    lineno += 1

else:
    print("No,Python is not present!")

'''


#8.A program to make a copy of a text file “this. txt”

'''

with open("this.txt") as f:
    content= f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)

'''

#9.A program to find out whether a file is identical & matches the content of another file.

'''

with open("this.txt") as f:
    content1= f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if (content1==content2):
    print("Yes,these files are identical!")

else:
    print("No,these files are not identical!")

'''

#10.A program to wipe out the content of a file using python.

'''

with open("this_copy.txt", "w") as f:
    f.write("")

'''

#11.A python program to rename a file to “renamed_by_ python.txt.

'''

with open("old.txt") as f:
    content= f.read()

with open("renamed_by_ python.txt", "w") as f:
    f.write(content)

'''