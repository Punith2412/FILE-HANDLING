import os
import sys
print('start')
def f():
    print("choose your option\n 1.creat file\n 2.read file\n 3.edit file\n 4.list file\n 5.delete file\n")
    d=int(input(""))
    a=d
    
    match a:
          case 1:
              print("----------------------------------------------------------")
              print("CREATING FILE\n")
              print("enter your file name\n:")
              f=input("")
              h=f+".txt"
              with open(h,'x')as file:
                 print(f,"FILE CREATED SUCCESSFULLY\n")
              print("-----------------------------------------------------------")
              f()
          

          case 2:
              print("----------------------------------------------------------")
              print("READING FILE\n")
              print("enter the file name that you want to read\n")
              f=input("")
              with open (f+".txt",'r')as file:
                 print(file.read())
              print("THE FILE READ SUCCESSFULLY\n")
              print("----------------------------------------------------------")
              f()

          case 3:
              print("----------------------------------------------------------")
              print("EDITING FILE\n")
              print("enter the file name that you want to edit\n")
              f=input("")
              with open(f+".txt",'a')as file:
                  print(file.write())
              print("FILE EDITED SUCCESSFULLY\n")
              print("-----------------------------------------------------------")
              f()

          case 4:
              print("------------------------------------------------------------")
              print("LIST ALL FILES\n")
              path='C:/Users'
              file=os.listdir(path)
              for file in file:
                  print (file)
              print("THESE ARE THE LIST OF FILES\n")
              print("----------------------------------------------------------")
              f()

          case 5:
              print("----------------------------------------------------------")
              print("DELETE FILE\n")
              f=input("")
              file=os.remove+'.txt'(path)
              print("DELETE FILE SUCCESSFULLY\n")
              print("----------------------------------------------------------")
              f()

          case 6:
              print("----------------------------------------------------------")
              print("STOP THE PROGRAM\n")
              sys.exit(0)
              print("----------------------------------------------------------")
              

while 1:
     f()
              
