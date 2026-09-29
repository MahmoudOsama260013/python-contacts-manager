import difflib
list_Num = []
list_Name = []
list_Type = []
def add ():
  # global list_Num
  name = input("Contact name: ").strip().lower()
  number = input("contact number: ")
  if number:
    
    while number in list_Num :
      print("Reserved Number")
      number = int(input("contact number: "))
    type = input("contact type: (Family, Personal, Work,Other)")
    if type not in ['Family' , 'family', 'Personal' , 'personal', 'Work' , 'work' ] :
      type = 'Other' 
      print ("The contact type is Other")
    list_Name.append(name) 
    if number not in list_Num:
      list_Num.append(number)
    else:
      print("Reserved number")
      number= int (input('Enter the number: '))
    list_Type.append(type)
    while True:
      more = input("Add another number (Y/N)")
      if more in ["y","Y"]:
        number_2= int (input('Enter another number: '))
        list_Name.append(name)  
        list_Type.append(type)
        if number_2 not in list_Num:
          list_Num.append(number_2)
        else:
          print("Reserved number")
          number_2= int (input('Enter another number: '))
      else:
        break
    print("DONE!\n")
  else:
    print("Invalid Input")
    print()
    add()

def s_Name ():
  #global name
  name = input("Enter the name: ").strip().lower()
  matches = difflib.get_close_matches(name,list_Name,n=3,cutoff=0.6) 
  if len(matches)==0:
    print("The name", name ,"does not reserved")
  else:
      x=0
      for i in list_Name:
        if i in matches:
          print("Name: ",list_Name[x])
          print("Number: ",list_Num[x])
          print("Type: ",list_Type[x],"\n")
        x+=1

def s_number ():
  #global name
  number = input("Enter the number: ")
  if number not in list_Num :
    print("The number", number ,"does not reserved")
  else:
    x=0
    for i in list_Num: # 100 200 300 400
      if i == number :
        print("Name: ",list_Name[x])
        print("Number: ",number)
        print("Type: ",list_Type[x],"\n")
      x+=1
      

def d_Name ():
  #global name
  name = input("Enter the name: ")
  if name not in list_Name :
    print("The name", name ,"Not found")
  else:
    while name in list_Name:
      x = list_Name.index(name)
      print("Name: ",name)
      print("Number: ",list_Num[x])
      print("Type: ",list_Type[x])
      del(list_Name[x])
      del(list_Num[x])
      del(list_Type[x])
    print("DONE!\n")


def d_Number ():
  #global name
  number = input("Enter the number: ")
  if number not in list_Num :
    print("The number", number ,"Not found")
  else:
    
    for i in list_Num: # 100 200 300 400
      if i == number :
        x = list_Num.index(number)
        print("Name: ",list_Name[x])
        print("Number: ",number)
        print("Type: ",list_Type[x])
        del(list_Name[x])
        list_Num.remove(number)
        del(list_Type[x])
    print("DONE!\n")
      

def show_All ():
  if len(list_Name)==0:
    print("NO contacts. \n")
  else:
    for i in range(len(list_Num)):
      print("Name: ",list_Name[i],"\t" , end="")
      print("Number: ",list_Num[i],"\t" , end="")
      print("Type: ",list_Type[i],"\t")
      print("")

while True :
  print("Welcome to our Address book, please to find what you want\n\t1. Add new contact.\n\t\
2. Search by name.\n\t3. Search by number.\n\t4. Delete contact by name.\n\t5. Delete contact by number.\n\t\
6. Show all contacts.\n\t7. Exit")
  choice = (input("Please to enter your choice: ")).strip()
  if choice in ["1","2","3","4","5","6","7"]:
    choice=int(choice)
  if choice in  [1]:
    add()
  elif choice in[2] :
    s_Name ()
  elif choice in [3]:
    s_number ()
  elif choice in [4]:
    d_Name ()
  elif choice in  [5]:
    d_Number ()
  elif choice in [6]:
    show_All ()
  elif choice in [7]:
    break
  else :
    print("Invalid Input")
