class intro():
    def title(self):
        topic="BUS TICKET BOOKING"
        design="*=*=*=*=*=*=*=*=*"
        print(topic.center(100))
        print(design.center(100))
        
    def details(self):
        print("Easy Booking: \n\tBooking your preferred Bus ticket is just few taps away !!! ")
        print("\nManage Trip: \n\tAll Your trip in one place. Regular remainder about your upcoming Trips !!! ")
        print("\nTrack Bus:  \n\tTrack real time location of your bus and share with your friends and family !!!\n")

top=intro()
top.title()
top.details()

class connect():
    def __init__(self,sign):
        self.sign=sign
        
    def log(self):
        if(self.sign=="1"):
            print("\nSignUp")
            ph=input("1.Phonenumber \n2.Gmail \nEnter Your Option: ")
            if(ph=="1"):
                for i in range(50):
                    phone=input("Enter Phone Number: ")
                    if(len(phone)==10):
                        import random
                        otp=random.randrange(1000,10000)
                        print("Generate OTP: ",otp)
                        generate=int(input("Enter OTP:"))
                        if(generate==otp):
                            print("Access Granted")
                            break
                        else:   print("Access denied")
                    else:   print("Please Enter Phone Number Correctly !")
            elif(ph=="2"):
                    mail=input("\nEnter Emailid: ")
                    password=input("Enter Password: ")
                    for i in range(50):
                        password2=input("Re-Enter Password: ")
                        if(password==password2):
                            print("Signup Succesfully")
                            break
                        else:   print("Please Re-Enter Password Correctly !\n")
        elif(self.sign=="2"):
            print("\nLogin")
            ph=input("1.Phonenumber \n2.Gmail \nEnter Your Option: ")
            if(ph=="1"):
                for i in range(50):
                    phone=input("Enter Phone Number: ")
                    if(len(phone)==10):
                        import random
                        otp=random.randrange(1000,10000)
                        print("Generate OTP: ",otp)
                        generate=int(input("Enter OTP:"))
                        if(generate==otp):
                            print("Access Granted")
                            break
                        else:   print("Access denied")
                    else:   print("Please Enter Phone Number Correctly !")
            elif(ph=="2"):
                    mail=input("\nEnter Emailid: ")
                    password=input("Enter Password: ")
                    print("Login Successfully !")
        elif(self.sign=="3"):
            pass
        
signin=input("1.Signup \n2.Login \n3.Skip \nEnter Your Choice: ")
loc=connect(signin)
loc.log()

class profile():
    def __init__(self,alter):
        self.alter=alter
        
    def prof(self):
        if(self.alter=="Yes" or self.alter=="yes"):
            print("\nPersonal Information")
            name=input("Name: ")
            birth=input("DOB: ")
            gender=input("Gender: ")
            print("\nContact Details: ")
            state=input("State:")
            for i in range(50):
                number=input("Phone Number: ")
                if(len(number)==10):
                    break
                else:   print("Enter Phone Number Correctly !")
            email=input("Email ID: ")
        elif(self.alter=="Later" or self.alter=="later"):
            pass
            
edit=input("\nEdit Profile Yes/Later: ")
info=profile(edit)
info.prof()

class travel(profile):
    def __init__(self,start,end,date,time,number,clas):
        self.start=start
        self.end=end
        self.date=date
        self.time=time
        self.number=number
        self.clas=clas

    def showbus(self):
        bus=input("\n1.Red Express Travels - $530 \n2.Praveen Travels - $460 \n3.National Travel - $600 \n4.RKT Tours and Travels - $720 \n5.SVT TRANZ - $900 \nSelect Your Bus: ")
        if(bus=="1"):
            prize=530*self.number
            if(self.clas=="1"):
                total=prize*3
                print("\nRed Express Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="2"):
                total=prize*2
                print("\nRed Express Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="3"):
                total=prize*1
                print("\nRed Express Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            else:   print("Only above Class are Available !")
        elif(bus=="2"):
            prize=460*self.number
            if(self.clas=="1"):
                total=prize*3
                print("\nPraveen Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="2"):
                total=prize*2
                print("\nPraveen Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="3"):
                total=prize*1
                print("\nPraveen Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            else:   print("Only above Class are Available !")
        elif(bus=="3"):
            prize=600*self.number
            if(self.clas=="1"):
                total=prize*3
                print("\nNational Travel","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="2"):
                total=prize*2
                print("\nNational Travel","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="3"):
                total=prize*1
                print("\nNational Travel","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            else:   print("Only above Class are Available !")
        elif(bus=="4"):
            prize=720*self.number
            if(self.clas=="1"):
                total=prize*3
                print("\nRKT Tours and Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="2"):
                total=prize*2
                print("\nRKT Tours and Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="3"):
                total=prize*1
                print("\nRKT Tours and Travels","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            else:   print("Only above Class are Available !")
        elif(bus=="5"):
            prize=900*self.number
            if(self.clas=="1"):
                total=prize*3
                print("\nSVT TRANZ","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="2"):
                total=prize*2
                print("\nSVT TRANZ","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            elif(self.clas=="3"):
                total=prize*1
                print("\nSVT TRANZ","\nFrom:",self.start,"\nEnd:",self.end,"\nDate:",self.date,"\nTiming:",self.time,"\nNumber of Passenger:",self.number,"\nClass Type:",self.clas)
                print("Total Prize:₹",total)
            else:    print("Only above Class are Available !")
        else:   print("Now ! Above Bus Only Available...")
            
print("\nPlace and Time: ")
start=input("From: ")
end=input("End: ")
date=input("Date(eg.10/08/2024):")
time=input("Time(eg.22:30): ")
number=int(input("Number of Passenger: "))
clas=input("Class Type: \n1.First Class(AC with Sleeper) \n2.Second Class(Sleeper) \n3.Third Class(Normal Seat) \nEnter Your Prefernce: ")
trav=travel(start,end,date,time,number,clas)
trav.showbus()

class payment(travel):
    def __init__(self,process):
        self.process=process
    def transfer(self):
        if(self.process=="Yes" or self.process=="yes"):
            method=input("\nGpay / Phonepe / Paytm / Cancel \nEnter Your Payment method: ")
            if(method=="gpay" or method=="Gpay"):
                trans=input("Enter UPI id:")
                import random
                upi=random.randrange(1000000,10000000)
                print("Transaction ID:",upi)
                id=int(input("Enter Transaction Id: "))
                if(id==upi): print("\nPayment received succesfully ! \nContact Number: 7852369941 \nCall Above Number Collect Driver Name and Phone Number \nAll Passenger are must bring ID proof \nThank You ! ")
                else:       print("Sorry ! Payment Cancelled")
            elif(method=="Phonepe" or method=="phonepe"):
                trans=input("Enter UPI id:")
                import random
                upi=random.randrange(1000000,10000000)
                print("Transaction ID:",upi)
                id=int(input("Enter Transaction Id: "))
                if(id==upi): print("\nPayment received succesfully ! \nContact Number: 7852369941 \nCall Above Number Collect Driver Name and Phone Number \nAll Passenger are must bring ID proof \nThank You ! ")
                else:       print("Sorry ! Payment Cancelled")
            elif(method=="paytm" or method=="Paytm"):
                trans=input("Enter UPI id:")
                import random
                upi=random.randrange(1000000,10000000)
                print("Transaction ID:",upi)
                id=int(input("Enter Transaction Id: "))
                if(id==upi): print("\nPayment received succesfully ! \nContact Number: 7852369941 \nCall Above Number Collect Driver Name and Phone Number \nAll Passenger are must bring ID proof \nThank You ! ")
                else:       print("Sorry ! Payment Cancelled")
            elif(method=="cancel" or method=="Cancel"):
                pass
        elif(self.process=="No" or self.process=="no"):
            print("Re-Enter Details Correctly ! ")                

process=input("\nAbove Details are Correct Yes/No:")
paid=payment(process)
paid.transfer()
