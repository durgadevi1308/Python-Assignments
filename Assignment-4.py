import datetime
class IndividualReservation:
    def __init__(self,train_name,start,dest,passenger_name,age,clazz,date):
        self.train_name=train_name
        self.start=start
        self.dest=dest
        self.passenger_name=passenger_name
        self.age=age
        self.clazz=clazz
        self.date=date

    """
    Getting Passenger's travel details
    """  

    def travel_details(self):
        print("TRAVEL DETAILS")
        return f"Your starting point: {self.start}\nYour ending point: {self.dest}\nYour travel date:{date}"    
        
    def train_details(self,train_code,tstart,tdest,**kwargs):
        print("\nTRAIN DETAILS")
        print("Train available: ",self.train_name)
        print("Train code: ",train_code)
        stations = []
        for key,value in kwargs.items():
            stations.append("{} is at {}".format(key,value))
            
        return f"Train's Starting station: {tstart}\nTrain's Destination station: {tdest}\nStaions in between: {stations}"
    
    """
    Have used datetime function to get the date in YYYY-MM-DD form. Then isoweekday function is usedto get the day number of the date. Eg:number 7 is returned for Sunday
    """    
    
    def availability(self):
        print("\nAVAILABILITY TIMINGS IN A WEEK")
        dt=self.date
        day=dt.isoweekday()
        match day:
            case 1:
                return f"{self.date} is Monday \nTrain is available at {self.start} station at 14.50pm"
            case 2:
               return f"{self.date} is Tuesday \nTtrain is unavailable at {self.start} station"
            case 3:
               return f"{self.date} is Wednesday\n Train is available at {self.start} station at 14.20pm"
            case 4:
                return f"{self.date} is Thursday \nTrain is available at {self.start} station at 14.50pm"
            case 5:
                return f"{self.date} is Friday \nTrain is available at {self.start} station at 09.15am"
            case 6:
                return f"{self.date} is Saturday \nTrain is unavailable at {self.start} station"
            case 7:
                return f"{self.date} is Sunday  \nTrain is available at {self.start} station at 14.50pm"
            case _:
                return f"Incorrect date!!!"    
        
    def passenger_details(self,gender,pno):
        print("\nPASSENGER DETAILS")
        return f"Passenger Name:{self.passenger_name}\nAge:{self.age}\nGender:{gender}\nPhone Number:{pno}"
        
    """
    Have used if elif else clause to determine the ticket price on the basis age criteria
    """    

    def ticket_details(self,sleeper_price,fclass_price,sclass_price):
        print("\nTICKET DETAILS")
        print("Passenger Name:",self.passenger_name)
        print("Your boarding station:",self.start,"\nYour landing station:",self.dest)
        if self.clazz=="Sleeper":
            print("Class booked: SLEEPER CLASS")
            if self.age>60:
                return f"Age:{self.age} - Senior Citizen \nTicket price:{sleeper_price*0.75}"
            elif self.age<10:
                return f"Age:{self.age} - Child \nTicket price:{sleeper_price*0.80}"
            else:
                return f"Age:{self.age} - Adult \nTicket price: {sleeper_price}"
                
        elif self.clazz=="First Class": 
            print("Class booked: FIRST CLASS")
            if self.age>60:
                return f"Age:{self.age} - Senior Citizen \nTicket price:{fclass_price*0.75}"
            elif self.age<10:
                return f"Age:{self.age} - Child \nTicket price:{fclass_price*0.80}"
            else:
                return f"Age:{self.age} - Adult \nTicket price: {fclass_price}"
            
                
        elif self.clazz=="Second Class":
            print("Class booked: SECOND CLASS")
            if self.age>60:
                return f"Age:{self.age} - Senior Citizen \nTicket price:{sclass_price*0.75}"
            elif self.age<10:
                return f"Age:{self.age} - Child \nTicket price:{sclass_price*0.80}"
            else:
                return f"Age:{self.age} - Adult \nTicket price: {sclass_price}"
                
        else:
            return f"Unreserved!!!"
        
    def additional_bill(self,platform_bill):
            print("\nADDITIONAL BILL DETAILS")
            meal_bill=360
            try:
                ab=meal_bill+platform_bill
                return f"Additionally you have to pay:{ab}"
            except Exception as e:
                return f"Error!!, Please enter valid amount"
            
print("AN INDIVIDUAL RAILWAY RESERVATION SYSTEM\n")        
date=datetime.date(2024,3,17)
s=IndividualReservation("Karaikal Express","Katpadi","Mayiladuthurai","Pranav",24,"Sleeper",date)
print(s.travel_details())
print(s.train_details("KVM-431","Chennai","Mayiladuthurai",station1="Chengalpet",station2="Arrakonam",station3="Katpadi",station4="Villupuram",station5="Chidambaram"))
print(s.availability())
print(s.passenger_details("Male","9894755943"))
print(s.ticket_details(2500,2000,1700))
print(s.additional_bill(15))

   
        