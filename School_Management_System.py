# Import All Modules.

# import Sqlite for connect database into program.
import sqlite3

#import os for some operating system functionalites.
import os

# import datetime for current time and date.
import datetime

# import time for sleep function.
import time

# import Random for registration No
import random

#Create a function for clear the console.
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#Create a connection with Database.
MyDB=sqlite3.connect("login.db" , check_same_thread=False)
          
# Create a Cursor for Execute all query into database.
MyCur=MyDB.cursor() 

# Create aTable for Password
MyCur.execute(''' Create Table if not Exists password( user varchar(20) , pass varchar(20) , pass_key varchar(30));''')

# Create a Table for Fee
MyCur.execute(''' Create Table If Not Exists fee_table( roll_no int primary key , submitted_fee int(13) default 1000 ,class varchar(10)); ''')

# Create a Table for Registration.
MyCur.execute(''' Create Table If Not Exists stu_registration( name varchar(30) , father_name varchar(30) , class varchar(10) , reg_no varchar(15) primary key , phone_no varchar(13) , address varchar(40) , registration_date date);''')
# Function for Student Registration.
     
#Create a Table for storing Student Data.
MyCur.execute('''  Create Table If Not Exists stu_details( name varchar(30) , father_name varchar(30) , class varchar(10) , roll_no int primary key , phone_no varchar(13) , gender varchar(10) , religion varchar(15) , address varchar(40) , email varchar(30) , addmission_date date); ''')

#Create a table for Storing Teachers Data.
MyCur.execute('''  Create Table If Not Exists Teacher_details( name varchar(30) ,  subject varchar(20) , id int primary key , phone_no varchar(13) , gender varchar(10) , religion varchar(15) , address varchar(40) , email varchar(30) , joining_date date); ''')

# Function for System Setting.
def sys_setting( ):
      time.sleep(0.7)
      clear()
      print('''                                  iCoder School Management System Setting                     
           \n\t\t******************************************************************************************* 
                  1 . Reset System                                     2 . Change Font / Color  
                  3 . About software                                   4 .Change Password
                  5 . Help Center
                ******************************************************************************************* ''')                                  
      task = input("\n      Enter task No : ")
      if task == '1':
            reset( )
      elif task == '2':
            change_font_color( )
      elif task == '3':
            about_software( )
      elif task=='4':
            change_pass( )
      elif task == '5':
            help( ) 
      else :
            print("\n    Please Enter Valid No. ")

# Function for showing Details about software
def about_software( ):
      print(''' \n\tSoftware Name : iCoder school Management System.\n\tSoftware Type : Console Application. \n\tDevelope By : Team iCoder. \n\tVersion : 0.0.01 Global.\n\n\n\n\t\t\t\t******* Thank You From shezziii  to use Our software. ********* ''' )                          
# Function for Help.
def help( ):
      print('''\n Hello ,\n\n\t You are using a School Management Syatem Develope By iCoder Team.\n\t if you are not Understand working of System Please contact with  iCoder Team.\n\t I hope you are having good experience with it.\n\t Contect no : 0000000XYZ  \n\t For feedback Visit - www.iCoder.in \n\n\n\t\t\t\t********* Thank You *************''') 
                            
#  Function for change color.
def change_font_color( ):
      print('\n This feature is in Testing .\n it will appear in next version.')

# Function for loging.
def user_pass( ):
      print('''\n\n\n\n\n\n\n\n\n\t\t\t\t***** WELCOME TO iCoder International School *****                                                       ''')
      time.sleep(2)
      clear()
      MyCur.execute(" select pass from password ;")
      key=MyCur.fetchone( )
      if key == None :
            user=input("\n Enter User Name For Sign-Up : ")
            pass_=input("\n Create a '8' digits Password ( please , Create a strong Password ) : ")
            pass_key=input(" \n Enter your Faviorate person Name : ")
            MyCur.execute(f" Insert into password values ( '{user}' , '{pass_}' , '{pass_key}');")     
            MyDB.commit()
            print(" \n\n\n\t\t\t\t  SIGN-UP SECCUSSEFULL............")
            input("\n\n Press enter key - ")
            clear()
      else :
           user_ , pass_ = input("\n Enter User name and password  ( for loging ): ").split()     
           MyCur.execute(f" Select * from password where  user= '{user_}' and pass='{pass_}';")
           result=MyCur.fetchone()
           if( result==None):
                 print("\n Invalid Username and Password . ")
                 f_pass=input(" \n Forget Password ( Y / N ) : ")
                 if f_pass=='Y':
                       user=input("\n Enter User Name : ")
                       pass_key=input(" \n Enter your Faviorate person Name : ")
                       MyCur.execute(f" Select pass from password where user='{user}' and pass_key='{pass_key}';")
                       pass_=MyCur.fetchone( )
                       if pass_==None:
                             print("/n Invalid user and password key . ")
                             user_pass( )
                 else : 
                       clear()
           else :
                 print('\n\n\n\n\n\t\t\t\t  Loging successful .........')
                 input("\n\n Press enter key - ")
                 clear()
                 
# Function for change Password.
def change_pass( ):
      user_=input("\n Enter Username :  ")
      pass_=input("\n Enter password : ")
      MyCur.execute(f" Select * from password where  user= '{user_}' and pass='{pass_}';")
      result=MyCur.fetchone()
      if( result==None):
            print("\n Invalid Username and Password . ")
            return
      pass_=input("\n Create New '8' Digits Password : ")
      MyCur.execute(f" Update into password set pass = '{pass_}' where user= '{user_}'; ")
      MyDB.commit( )
      print("\n\t Password Change Successfully.....")
            
      
# Function for Reset System
def reset( ):
      confirm=input("\n Do you Want to Reset Your School Management system (Y / N) : ")
      if confirm=='Y' or confirm=='y':
            confirm=input("\n Are You Confirm (Y / N) : ")
            if confirm=='Y'  or confirm=='y':
                  MyCur.execute("Drop Table stu_details;")
                  MyCur.execute("Drop Table Teacher_details;")
                  MyCur. execute(" Drop Table fee_table;")
                  MyCur.execute('Drop Table password;')
                  MyDB.commit()   
                  clear()
                  print('''\n\n\n\n\n\n                                              System Successfully  Reset ''' )   
            else :
                  return
      else:
            return            
            
# ************************* Function for Teacher **********************

# Function for add Teachers.
def Add_Teacher( ):
      name=input("\nEnter Name of Teacher : ")         
      subject=input("Enter Subject of Teacher : ")
      id=input("Enter ID no of Teacher : ")           
      phone_no=input("Enter Phone No  of Teacher : ")           
      gender=input("Enter Gender of Teacher : ")           
      religion=input("Enter Religion of Teacher : ")
      address=input("Enter address of Teacher : ")     
      email=input("Enter Email of Teacher : ")
      joining_date=(datetime.datetime.now()).split( )[0]  
      sql_statement='''insert into Teacher_details values (%s , %s , %s , %s , %s , %s ,%s ,%s , %s ); '''    
      Data = (name,subject,id , phone_no ,gender , religion ,address , email , joining_date)
      MyCur.execute(sql_statement, Data)     
      MyDB.commit() 
      print("\n************************* Entered Teacher Details ************************** ")
      Teacher_Print(Data)

# Function for Searching Details of Teacher.
def search_Teacher( ):
      key = int(input("\n Enter Id No of Teacher for Searching : "))
      sql_statement = f''' select * from Teacher_details where id = {key} ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None:
            print(f"\n Id No {key} is not Present in School .")
            return
      print(f"\n********************** Id No {key} Teacher Details ********************")
      Teacher_Print(Data)

# Function for Update Teacher details.
def update_Teacher( ):
      key=int(input("\n Enter ld No of Teacher for Updating : "))
      sql_statement = f''' select * from Teacher_details where id = {key} ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None:
            print(f"\n Id No {key} is not Present in School .")
            return
      print("\n********************** Id No {key} Teacher Old Details *********************** ")
      Teacher_Print(Data)
      sql_statement = f''' Delete from Teacher_details where id = {key} ; '''
      MyCur.execute(sql_statement)
      MyDB.commit()
      print("\n************************* Enter New Record ****************************")
      Add_Teacher( )                    

# Function for Remove Teacher.
def remove_Teacher( ):
      key = int(input("\n Enter ld No of Teacher for Deletion : "))
      sql_statement = f''' select * from Teacher_details where id = {key} ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None:
            print(f"\n Id No {key} is not Present in School .")
            return
      print("\n*********************** Deleted Teacher Details *************************** ")
      Teacher_Print(Data)
      sql_statement = f''' Delete from Teacher_details where id = {key} ; '''
      MyCur.execute(sql_statement)
      MyDB.commit()

# Function for View All Teacher of Specific subject.
def view_Teacher( ):
      key = input("\n Enter Subject Name for View All Teacher : ")
      sql_statement=f'''select count(*) from Teacher_details where subject = '{key} ' ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None or Data == 0 :
            print("\nNoOne Teacher Present for this Subject .")
            return
      print(f"\n Total Teacher of {key} Subject : {Data[0]}" )
      sql_statement = f''' select * from Teacher_details where subject = '{key}' ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      print(f"\n***************************** All Teacher of {key} ************************")
      for data in Data :
            Teacher_Print(data)
            
# Function for print details of Teacher.                                                                                    
def Teacher_Print( details):
      print(f''' Name : {details[0]} \n Subject :  {details[1]} \n id :  {details[2]} \n Phone No :  {details[3]} \n Gender :  {details[4]} \n Religion : {details[5]} \n Address : {details[6]} \n Email : {details[7]} \n Date of Joining : {details[8]} ''')

# **************************Function for students.*************************

def registration(  ):
      print("\n***************** Welcom to iCoder International school *********************")
      print("\n Filling the correct Details for registration : ")
      name=input("\nEnter Name of student : ")         
      fname=input("Enter Father Name of student : ")
      class_name=input("Enter Class of student : ")
      reg_no=random.randint(100,500)
      phone_no=input("Enter Phone No  of student : ")           
      address=input("Enter address of student : ")     
      registration_date=str(datetime.datetime.now()).split( )[0]  
      sql_statement='''insert into stu_registration values (%s , %s , %s , %s , %s , %s ,%s ); '''    
      print(f"\n Student Successfully registered.\n Please must remember registration No : {reg_no}.\n (Registration No is Used When you come for addmission.)")
      Data = (name,fname,class_name,reg_no , phone_no ,address,registration_date)
      MyCur.execute(sql_statement, Data)     
      MyDB.commit() 

# Function for Add Student.
def Add_Student( ):
      key=int(input("\n Enter Registration No : "))
      MyCur.execute(f"select * from stu_registration where reg_no = {key};")
      Data=MyCur.fetchone()
      if Data==None:
            print("\n Invalid registration id.\n please do registration first.")
            return
      print("\n Student is registered. \n Enter correct details for addmission.")
      name=input("\nEnter Name of student : ")         
      fname=input("Enter Father Name of student : ")
      class_name=input("Enter Class of student : ")
      roll_no=input("Enter Roll no of student : ")           
      phone_no=input("Enter Phone No  of student : ")           
      gender=input("Enter Gender of student : ")           
      religion=input("Enter Religion of student : ")
      address=input("Enter address of student : ")     
      email=input("Enter Email of student : ")
      addmission_date=str(datetime.datetime.now()).split( )[0]  
      sql_statement='''insert into stu_details values (%s , %s , %s , %s , %s , %s ,%s ,%s , %s , %s); '''    
      Data = (name,fname,class_name,roll_no , phone_no ,gender , religion ,address , email , addmission_date)
      MyCur.execute(sql_statement, Data)     
      MyCur.execute(f"insert into fee_table values ({ roll_no } , 0 , '{class_name}' );")
      MyDB.commit() 
      print("\n************************* Entered Student Details ************************** ")
      Print(Data)

# Function For Print Details of student.            
def Print( details):
      print(f''' Name : {details[0]} \n Father Name :  {details[1]} \n Class : {details[2]} \n Roll No :  {details[3]} \n Phone No :  {details[4]} \n Gender :  {details[5]} \n Religion : {details[6]} \n Address : {details[7]} \n Email : {details[8]} \n Date of Addmission : {details[9]} ''')

# Function for Searching for student.
def search_student( ):
      key = int(input("\n Enter Roll No of Student for Searching : "))
      sql_statement = f''' select * from stu_details where roll_no = {key} ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None:
            print(f"\n Roll No {key} is not Present in School .")
            return
      print(f"\n********************** Roll No {key} Student Details ********************")
      Print(Data)

# Function for Updating of Student Details.
def update_student( ):
      key=int(input("\n Enter Roll No of Student for Updating : "))
      sql_statement = f''' select * from stu_details where roll_no = {key} ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None:
            print(f"\n Roll No {key} is not Present in School .")
            return
      print("\n********************** Roll No {key} Student Old Details *********************** ")
      Print(Data)
      sql_statement = f''' Delete from stu_details where roll_no = {key} ; '''
      MyCur.execute(sql_statement)
      MyDB.commit()
      print("\n************************* Enter New Record ****************************")
      Add_Student( )                    
      
# Function for Delete Student.                                                                                      
def remove_student( ):
      key = int(input("\n Enter Roll No of Student for Deletion : "))
      sql_statement = f''' select * from stu_details where roll_no = {key} ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None:
            print(f"\n Roll No {key} is not Present in School .")
            return
      print("\n*********************** Deleted Student Details *************************** ")
      Print(Data)
      sql_statement = f''' Delete from stu_details where roll_no = {key} ; '''
      MyCur.execute(sql_statement)
      MyDB.commit()

# Function for View All Student of Same Class.
def view_student( ):
      key = input("\n Enter class for View All Student : ")
      sql_statement=f'''select count(*) from stu_details where class ='{key}' ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None or Data == 0 :
            print("\nNoOne Teacher Present for this Subject .")
            return
      print(f"\n Total No of Student Present in Class {key} : {Data[0]}" )
      sql_statement = f''' select * from stu_details where class = '{key}' ; '''
      MyCur.execute(sql_statement)
      Data = MyCur.fetchone( )
      if Data == None:
            print("\nNoOne Student Present in this Class.")
            return
      print(f"\n***************************** All Student of Class {key} ************************")
      for data in Data :
            Print(data)

# Function for Fees
def student_fee( ):
      fee_struct={1 : 5000 , 2 : 7000 , 3 : 9000 , 4 : 11000 , 5 : 13000 , 6 : 16000 , 7 : 19000 , 8 : 22000 , 9 : 25000 , 10 : 28000 , 11 : 33000 , 12 : 38000}
      class_n=int(input("\n Enter class of  Student ( Enter Only Digits ) : "))
      roll_No=int(input("\n Enter roll No of Student : "))
      MyCur.execute(f"select submitted_fee from fee_table where roll_no ={roll_No} and class= '{class_n}' ;")
      T_fee=MyCur.fetchone()
      T_fee=T_fee[0]
      if T_fee==None:
            print(f"\n Roll No {roll_No} is not present in {class_n} class of this school .")
            return
      print(f"\n Total fee = {fee_struct[class_n]} ")
      print(f"\n Submitted fee = {T_fee}")
      X=fee_struct[class_n]-T_fee
      print(f"\n Remaining fee = {X}")
      if T_fee> fee_struct[class_n]:
            print("\n Student Already Submitted Total fee.")
            return
      choice=input("\n Do you want to submit your fee ( Y / N ): ")
      if choice=='Y':
            return 
      money=int(input("Enter amount to submit : "))
      if (T_fee+money)>fee_struct[class_n]:
           print("\n please Submit amount ( Greater than equal to remain fee ) : ")      
      money=int(input())
      value=T_fee+money     
      MyCur.execute(f"Update fee_table set submitted_fee = {value} where roll_no={roll_No};")
      MyDB.commit()
      print("\n Fee Sumbitted Successfully. ")
 
# Main Function of Program.                              
def Main( ):
      print('''                    ********************* iCoder School Management System **********************                     
                     1 . Student Registration                                      2 . New addmission
                     3 . Remove Student                                            4 . Update Student Details                           5 . Search Student                                            6 . View All Student                                 7 . Add Teacher                                               8 . Remove Teacher                                   9 . Update Teacher Details                                    10. Search Teacher                                   11. View All Teacher                                          12. Fee Details                                      13. System Setting                                            14. Exit
                  \n                    **********************************************************************************''')
                  
      task = input("\n      Enter task No : ")
      if task=='1':
            registration( )
      elif task=='2':
          Add_Student( )
      elif task == '3':
          remove_student( ) 
      elif task=='4':
            update_student( )
      elif task== '5':
            search_student( )   
      elif task=='6':
            view_student( )                                  
      elif task=='7':
            Add_Teacher( )
      elif task == '8':
            remove_Teacher( ) 
      elif task=='9':
            update_Teacher( )
      elif task== '10':
            search_Teacher( )   
      elif task=='11':
            view_Teacher( )
      elif task=='12':
            student_fee()                                        
      elif task=='13':
            sys_setting( )
      elif task=='14':
            print("\n Thanks for using. ")
            exit()
      else :
            print("\n    Please Enter Valid No. ")
                                 
    
# Main Program Start from here. 
user_pass( )                       
while True:
      Main() 
      input("\n Press enter key : ")
      clear()       