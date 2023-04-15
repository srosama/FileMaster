import time
import pyfiglet
from operator import itemgetter
import time
#Make It Better
ascii_banner = pyfiglet.figlet_format("FileMaster !!")
print(ascii_banner)
time.sleep(0.1)

class main():
#The User Inputs And Validation
    try:
        user_Input_FileCHose = input("Enter File Name: ")
        while not user_Input_FileCHose.endswith('.txt'):
            user_Input_FileCHose = input("Enter File Name: ")
        while len(user_Input_FileCHose) < 5:
            user_Input_FileCHose = input("Enter File Name: ")

    except FileExistsError:
        print("\nFile NoT Found!!!")
        
        
    except FileNotFoundError:
        print("\nFile NoT Found!!!") 
    try:
        filetoPro = open(user_Input_FileCHose)
    except NameError:
        print("File NOt Existed")
        exit()
    except FileExistsError:
        print("File NOt Existed")
        exit()
    except FileNotFoundError:
        print("File NOt Existed")
        exit()

    time.sleep(0.3)

    print('\n')
    print("\
            [1]FindCLW\n\
            [2]SortByInpute\n \
           [3]Print THe File ")   
    try:
        userChoise = int(input(f"\n({filetoPro.name}) What is the Path?: "))
    except:
        print("\n(ErroR iNPUTE NonVilad Path Chose Ethir)(1,2,3)".upper())
        exit()
#The Tools
    def findCW():
        dic_data = dict()
        conter = 0
        larg = -1
        theword = None
        for findCW in main.filetoPro:
            convered_list = findCW.split()
            conter +=1 
            for dic_list in convered_list:
                dic_data[dic_list] = dic_data.get(dic_list,0) + 1
        #The Common
        for k,v in dic_data.items():
            if v > larg:
                larg = v
                theword = k
        print('\n')
        print(f'\t The Most Common Word is ---> ("{theword}") --> {larg}')

            
        #least
        least = min(dic_data.items())
        leastword = None
        for k,v in dic_data.items():
                least = v
                leastword = k
                
        print(f'\t The less Common Word is ---> ("{leastword}") --> {least} ')
        print(f'\t Total Lines In The FIle ---> ({conter})\n')
    def sortByInput():
        Whattosort = input(f"({main.filetoPro.name}) What to Find: ")
        dic_data_sort = dict()
        for sort in main.filetoPro:
            lsort = sort.split()
            for sdic in lsort:
                dic_data_sort[sdic] = dic_data_sort.get(sdic,0) + 1
            
        for fidn in dic_data_sort:
                try:
                    co = dic_data_sort[Whattosort] = dic_data_sort.get(Whattosort) +1
                    co+=-1
                except:
                    pass
                if Whattosort in dic_data_sort:
                    print(f"\nWord Found --> ({Whattosort}) in file ({main.filetoPro.name}) and repated ({co}) TImes".upper())
                    break
                else:
                    ms = (f"\nNo any desired data in file: {main.filetoPro.name}").upper()
                    
                    print(ms)
                    break
    def printAll():
        print('\n',95*"*")
        for easyTest in main.filetoPro:
            print(easyTest)
        print(95*"*")
 
#The Constructor 
def mainfile():
    if main.userChoise == 1: 
        time.sleep(0.8)
        main.findCW()
    elif main.userChoise == 2:
        time.sleep(0.8)
        main.sortByInput()
    elif main.userChoise == 3:
        time.sleep(0.8)
        main.printAll()

#Add this later
import re

file = open('sum.txt')
lst = list()
total = 0

for line in file:
    number_string = re.findall("[0-9]+", line)
    if len(number_string) == 0:
        continue
    else:
        for value in number_string:
             total += int(value)
print(total)

mainfile()
