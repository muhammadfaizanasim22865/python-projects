
class SmartDevice:

    def __init__(self,name):

        self.name=name
        self._status="OFF"

    def status(self):
        return self._status
    
    def turn_on(self):
       
       self._status="ON"
       return self._status
    
    def turn_off(self):
        self._status = "OFF"
        return self._status


    def __str__(self):
        return f"device name : {self.name} \n  status : {self._status} "
    
class SmartLight(SmartDevice):

    def status(self):
       return f"SmartLight is currently : {self._status} "

    def turn_on(self):

        self._status="ON"
        return f"{self.name} is : {self._status}"
    
    def turn_off(self):

        self._status="OFF"
        return f"{self.name} is : {self._status}"
    
    def __str__(self):
        return f"SmartLight name : {self.name} \n  status : {self._status} "
    
class SmartFan(SmartDevice):

    def status(self):
       return f"SmartFan is currently : {self._status} "

    def turn_on(self):

        self._status="ON"
        return f"{self.name} is : {self._status}"
    
    
    def turn_off(self):

        self._status="OFF"
        return f" {self.name} is : {self._status}"
    
    def __str__(self):
        return f"SmartFan name : {self.name} \n  status : {self._status} "
    
class SmartAC(SmartDevice):

    def status(self):
       return f"SmartAC is currently : {self._status} "

    def turn_on(self):

        self._status="ON"
        return f"{self.name} is : {self._status}"
    
    def turn_off(self):

        self._status="OFF"
        return f"{self.name} is : {self._status}"
    
    def __str__(self):
        return f"SmartAC name : {self.name} \n  status : {self._status} "
    
class SmartHub:

    def __init__(self):
        self.devices=[]

    def __add__(self,device):

        if device in self.devices:
            print("Device already exists!")
        else:
            self.devices.append(device)
        return self
    
    def __str__(self):
        abc=[]
        for dvc in self.devices:
            abc.append(str(dvc))
        
        return "\n".join(abc)
    
    def __iter__(self):
        return self.devices           # self.devices is iterable so the whole class becomes iterable
    
    def __getitem__(self,index):
        return self.devices[index]
    
    def __call__(self,name,action):

        for i in self.devices:
            if i.name.lower()==name.lower():
                if action.lower()=="on":
                    return(i.turn_on())
                elif action.lower()=="off":
                    return(i.turn_off())
                else:
                    return("invalid!")
                
        
        return "No such device!"
            
    def __len__(self):
        return len(self.devices)
    
hub = SmartHub()

while True:

    print("\n🔹 SMART HOME CONTROL MENU 🔹\n")
    print("1. Add SmartLight")
    print("2. Add SmartFan")
    print("3. Add SmartAC")
    print("4. Show all devices")
    print("5. Control a device (ON/OFF)")
    print("6. Show device count")
    print("7. Show device by index")
    print("8. Exit")

    choice = (int(input("Enter your choice (1-8): ")))

    if choice==1:
        name=input("enter name of your smartlight : ").strip().lower()
        light=SmartLight(name)
        hub+light
        print(name, "added!")
    
    elif choice==2:
        name=input("enter name of your smartfan : ").strip().lower()
        fan=SmartFan(name)
        hub+fan
        print(name, "added!")

    elif choice==3:
        name=input("enter name of your smartAC : ").strip().lower()
        AC=SmartAC(name)
        hub+AC
        print(name, "added!")

    elif choice==4:
            print("\n devices details \n")
            print(hub)

    elif choice==5:
        print("\n controllling device \n ")
        name=input("enter name of the device : ")
        action=input("enter the action u wanna perform : ")
        print(hub(name,action))

    elif choice==6:
        print("\n devices count \n")
        print(len(hub))

    elif choice==7:
        print("\n checking device at the index \n ")
        try: 
            index=int(input("enter index : "))
            print(hub[index])
        except IndexError:
            print("no device found at this index!")

    elif choice==8:
        print("exiting...")
        print("Good Bye!")
        break

    else:
        print("invalid choice!")

    