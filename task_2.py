import os,hashlib,csv,sys,shutil #refer readme file for passwords
try:  #try except blocks used beacuse you dont have to worry when u run this code multiple times
    os.mkdir('DBMS')
except FileExistsError:
    os.chdir('DBMS')
else:
    os.chdir('DBMS')
try:   #try except blocks used beacuse you dont have to worry when u run this code multiple times
    os.mkdir('profile_pictures')
except FileExistsError:
    pass
def login():
    os.system('cls')
    print('lets login')
    email=input('Enter Your email: ')
    with open('users.csv','r') as f:
        read=csv.DictReader(f)
        for line in read:
            if (str(line['Email']))==email:
                password =make_hashed_pwd(input('Please enter password:').strip())
                if password== line['Hashed_pwd']:
                    f.close()
                    os.system('cls')
                    print('Logged in!!')
                    display_user_details(email) 
                    break             #stps iterating for reducing execution time
                       
                else:
                    print('wrong password')
                    f.close()
                    welcome_page()
                    break             #stps iterating for reducing execution time        
            else:
                continue   
def register():
    os.system('cls')
    print('let\'s register')
    email=input('Enter Your email: ')
    with open('users.csv','a') as f:
        write=csv.writer(f)
        if os.stat('users.csv').st_size==0 :
            write.writerow(['Name','Email','Phone_no','Sex','Address','Hashed_pwd'])
            f.close()
            save_user_data(email)
        else:
            f.close()
            with open('users.csv','r') as f:
                read=csv.DictReader(f)
                for line in read :
                    if str(line['Email'])==email :
                        print('user alredy exists with the same email!! login or register with anathor email')
                        f.close()
                        welcome_page()   
                        break
                    else:    
                        continue
                save_user_data(email)
                f.close()
def make_hashed_pwd(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def display_user_details(email):
    with open('users.csv','r') as f:
        read=csv.DictReader(f)
        for line in read:
            if (str(line['Email']))==email:
                for details_of_user in ['Name','Email','Phone_no','Sex','Address']:
                    print('Your '+details_of_user+' is '+line[details_of_user])      
            else:
                continue
    f.close()
    search_names()
    
def search_names():

    user_name=input("pls enter the name of the user to search :")
    os.system('cls')
    with open('users.csv','r') as f:
            read=csv.DictReader(f)
            for line in read:
                if line['Name']==user_name:
                    for details_of_user in ['Name','Phone_no','Address']:
                        print(details_of_user+' is '+line[details_of_user]) 
                    break
                print()                   
    to_check_if_user_want_to_make_anathor_search=input("if_user_want_to_make_anathor_search,type 'yes'\n")
    if to_check_if_user_want_to_make_anathor_search=='yes':
        search_names()
    else:
        f.close()
        pass
def welcome_page():
    print('WELCOME!!')
    response=input("Are you a new user? \t (type 'yes' or 'no' )\n")
    register() if response=='yes' else login() 

def save_user_data(email):
    with open('users.csv','a+') as f:
            write=csv.writer(f)
            Name=input('Enter Your Name: ')
            Phone_no=input('Enter Your phone_number: ')
            Sex=input('Enter Your sex: ')                    
            Address=input('Enter Your Address : ')
            password =input('Please enter password:')
            password2=input('Please re- enter password:')
            if password==password2:
                print('account created\t Lets login')
                Hashed_pwd=make_hashed_pwd(password)
                write.writerow([Name,email,Phone_no,Sex,Address,Hashed_pwd])
                
            else:
                print('passwords didnt match')
                register()
            print("Let's add a profile pic!!")
            confirmation=input("dear User please type 'yes' to add a profile pic\n or a default image will be set:")
            os.chdir('profile_pictures')
            if confirmation=='yes':
                path_of_img=input('please provide path of the image')
                destination_folder=os.getcwd()
                shutil.copy(path_of_img,destination_folder)
            else:
                try:  #here default path gives error in others system so try,except used,just rectify path it works well
                    path_of_img='C\:\\Users\\admin\\Pictures\\hjkfsdh.jpg'
                    destination_folder=os.getcwd()
                    shutil.copy(path_of_img,destination_folder) 
                except OSError:
                    pass
            os.system('cls')   
            os.chdir('..')  
            print('account created!!, lets login!') 
            f.close()          
            welcome_page()
welcome_page()



























