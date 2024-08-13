import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='root',database='cancer')
if con.is_connected():
    cor=con.cursor()
from funtions import *
with open ('TEXT.txt', 'r') as file:
    read_file=file.read()
    print(read_file)
while True:
    print('                                                        ')
    print('                                                        ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    ch=int(input('1.Admin login 2.Patient login'))
    if ch==1:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('                                                                         ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME TO ADMIN MODE ~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('                                                                         ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('                                                                         ')
        print('                        1.User Sign In (Login)                                                  ')
        print('                        2.User Sign Up (Registration)                                           ')
        print('                                                                         ')
        ch1=int(input("Please Enter Your Choice:"))
        if ch1==1:
            i=0
            j=1
            while i<3:
                    Username=input('Enter username')
                    Password=input('Enter Passowrd')
                    sql = "select * from admin_login where A_username = %s and A_password = %s"
                    cor.execute(sql,[(Username),(Password)])
                    results = cor.fetchall()
                    if results:
                       for i in results:
                          print('                                                      ')
                          print('~~~~~~~~~~~~~~~~~~~ Login sucessful ~~~~~~~~~~~~~~~~~~')
                          print('                                                      ')
                          j=j+1
                          break

                    else:
                       print('~~~~~~~~~~~ Login Unsucessful. Incorrect Password/Username ~~~~~~~~~~~')
                       print('~~~~~~~~~~~~~~~~~~~~~~  Please Try again ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                       i=i+1
                    while j>1:
                        A_menu()
                        print('                                                      ')
                        print('                                                      ')
                        A_opp=int(input("Please Enter Your Choice:"))
                        if A_opp==1:
                            layout()
                        elif A_opp==2:
                            add_patient()
                        elif A_opp==3:
                            disp_patient()
                        elif A_opp==4:
                            disp_allrecords()
                        elif A_opp==5:
                            upd_record()
                        elif A_opp==6:
                            remove()
                        elif A_opp==7:
                            summary()
                        elif A_opp==8:
                            A_login()
                        else:
                           print('Invalid Input')

        elif ch1==2:
            Username=input("Please enter your Username")
            while True:
             Password=input("Please enter you Password (Must be atleast 6 words )")
             re=input("Please retype your password")
             if Password !=re:
                print("Please recheck your password")
                break
             else:
                sql = "insert into admin_login values(%s,%s)"
                cor.execute(sql,(Username,Password))
                con.commit()
                results = cor.fetchall()
                print('                                                      ')
                print('~~~~~~~~~~~~~~~ Admin account created ~~~~~~~~~~~~~~~')
                print('                                                      ')

                A_menu()
                print('                                                      ')
                print('                                                      ')
                A_opp=int(input("Please Enter Your Choice:"))
                if A_opp==1:
                    layout()
                elif A_opp==2:
                    add_patient()
                elif A_opp==3:
                    disp_patient()
                elif A_opp==4:
                    disp_allrecords()
                elif A_opp==5:
                    upd_record()
                elif A_opp==6:
                    remove()
                elif A_opp==7:
                    summary()
                elif A_opp==8:
                    A_login()
                else:
                    print('Invalid Input')

        else:
            print('Invalid Input')
    elif ch==2:
         print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
         print('                                                                         ')
         print('~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME TO USER MODE ~~~~~~~~~~~~~~~~~~~~~~~~~')
         print('                                                                         ')
         print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
         print('                                                                         ')
         print('                        1.User Sign In (Login)                                                  ')
         print('                        2.User Sign Up (Registration)                                           ')
         print('                                                                         ')
         ch2=int(input("Please Enter Your Choice:"))
         if ch2==1:
              i1=0
              k=1
              while i1<3:
                    Username=input('Enter Username')
                    Password=input('Enter Passowrd')
                    sql = "select * from patient_login where P_username = %s and P_password = %s"
                    cor.execute(sql,[(Username),(Password)])
                    results = cor.fetchall()
                    if results:
                        for i in results:
                             print('                                                      ')
                             print('~~~~~~~~~~~~~~~~~~~ Login sucessful ~~~~~~~~~~~~~~~~~~')
                             print('                                                      ')
                             k=k+1
                             break

                    else:
                           print('~~~~~~~~~~~ Login Unsucessful. Incorrect Password/Username ~~~~~~~~~~~')
                           print('~~~~~~~~~~~~~~~~~~~~~~  Please Try again ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                           i1=i1+1
                    while k>1:
                       P_menu()
                       print('                                                      ')
                       print('                                                      ')
                       P_opp=int(input("Please Enter Your Choice:"))
                       if P_opp==1:
                          view_app()
                       elif P_opp==2:
                          add_app()
                       elif P_opp==3:
                          cancel_app()
                       elif P_opp==4:
                           view_m()
                       elif P_opp==5:
                           add_m()
                       elif P_opp==6:
                           upd_m()
                       elif P_opp==7:
                           P_login()
                       else:
                           print('Invalid Input')
                
         elif ch2==2:
             Username=input("Please enter your Username")
             while True:
               Password=input("Please enter you Password (Must be atleast 6 words )")
               re=input("Please retype your password")
               if Password !=re:
                 print("Please recheck your password")
                 break
               else:
                 sql = "insert into patient_login values(%s,%s)"
                 cor.execute(sql,(Username,Password))
                 con.commit()
                 results = cor.fetchall()
                 print('                                                      ')
                 print('~~~~~~~~~~~~~~~ Patient account created ~~~~~~~~~~~~~~~')
                 print('                                                      ')
                 P_menu()
                 print('                                                      ')
                 print('                                                      ')
                 P_opp=int(input("Please Enter Your Choice:"))
                 if P_opp==1:
                    view_app()
                 elif P_opp==2:
                    add_app()
                 elif P_opp==3:
                    cancel_app()
                 elif P_opp==4:
                    view_m()
                 elif P_opp==5:
                    add_m()
                 elif P_opp==6:
                    upd_m()
                 elif P_opp==7:
                     P_login()
                 else:
                    print('Invalid Input')
    else:
      print('Invalid Input')