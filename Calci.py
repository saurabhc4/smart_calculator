import sys #inbuilt module
sys.path.append('/mymodules/') #path is ref var(obj) append is funtion
import mymodules
from mymodules.Mathy import *
print(responses[0])
print(responses[1])

while True:
    print() #line space
    text=input("enter some text")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("something went wrong please retry.")  
            finally:
                break #out from loop
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
        else:
            sorry()          
