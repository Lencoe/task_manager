import os



# the program will first ask for password and username

pass_word= input("Enter your password : ")
user_name= input("Enter your username : ")


#then take the password and username intered and check if they are available
#the program will display the invail text if they are not correct until user enters correct cridentials

reads =  open("user.txt","r+") 
read_lines = reads.readlines()
index =0

for line in read_lines :
  
 
  index+=1     
  
  if line :

    # if the password is correct it will display the task of the login user esle it will ask you to enter correct details
    
    if user_name in line :
      break

    else :
      if index == len(read_lines) : # helps in to check each line in the file
        print("invaild username or password!!! || try again\n")
        pass_word= input("Enter your password : ")
        user_name= input("Enter your username : ")
        read_lines = reads.readlines()

        for line in read_lines :
          if pass_word in line :
    
           break
      

#if the user login is the admin the program will display the admin menu else if its not the admin the program displays the user menu

#below is the admin menu
    
if user_name == "admin" :
  print("\nPlease select one of the following options :")
  print("r - register user")
  print("a - add task")
  print("va - view all tasks")
  print("vm - view my tasks")
  print("s  - to view statisticts")
  print("exit")
  print("\n")
    
#the else code below displays the user maenu
  
else  :
   
    print("\nPlease select one of the following options :")
    print("a - add task")
    print("vm - view my tasks")
    print("exit")
    print("\n")
    
reads.close()     

charactor = input()
charactor = charactor.lower()
  



write_in = open("user.txt",'a')

#if the user enters *r* the  program will allow them to register a new user

if charactor == "r" :

  if pass_word != "admin" :
    print("you are not urthurised in this section")
    
  else :
    username = input("enter new username : ")
    password = input("enter new password  : ")
    confirm  = input("please confirm your password : ")

    if password == confirm :
      write_in.write(str(username)+" , "+str(password))

      print("user successfuly registered !!!")
    
write_in.close()    
  

# if the user enters *a* the program will allow them to add a task    

if charactor == "a" :

  username = input("\nEnter the username of the person the task is assigned to : ")
  tittle =   input("\nEnter title of the task : ")
  description = input("\nDescription of a task : ")
  date = input("\nEnter the date today :")
  task_complete= input("\nIs the task completed? :")
  write_in = open("tasks.txt","a")
  write_in.write("\n"+str(username)+", "+str(tittle)+", "+str(description)+", "+str(date)+",  No ")
  write_in.close()
  print("Task sucessfuly added!!!")

# if the user enters va then the program will print out all the task in the file

if charactor == "va" :

  task_file = open("tasks.txt","r")
  
  for line in task_file :

    if line : 
      username,tittle,description,date,task_complete =  line.split(",")
   
      print("""
      Assigned to       :      {}
      Task tittle       :      {}
      Task description  :      {}
      Date Assigned     :      {}
      Task completed?    :     {}
        """.format(username,tittle,description,date,task_complete))
  task_file.close()
  

# if the user enters vm then the program will print out only  the task of the loggedin user

if charactor == "vm" :

  task_file = open("tasks.txt","r")

  for line in task_file :
    username,tittle,description,date,task_complete =  line.split(",")
   
    
    if user_name == username :
      print(f"""
Assigned to       :     {username}.
Task tittle       :     {tittle}.
Task description  :     {description}.
Date Assigned     :     {date}
Task completed?   :     {task_complete}
""")

      
task_file.close()

#if they enters *s* the program will display a statistics
  
if charactor == "s" :
  task_file = open("tasks.txt","r")
  counter = 0
  for i in task_file :
    if i :
      counter +=1
  print("Number Of Tasks")
  print(counter)

  task_file = open("user.txt","r")
  lenth = 0
  for i in task_file :
    if i :
      lenth +=1
  print("\nNumber Of Users")
  print(lenth)

  

if charactor == "exit" :
  print("u have exited your program Bye !!! Bye!!!")
  quit()
  
os.system("pause")

    
   
