
from abc import ABC,abstractmethod

import random

class Assistant(ABC):
    
    @abstractmethod
    def respond(self,command):
        pass

    def intro(self):
        return "Jarvis AI assistant created by fizzy "

class Jarvis(Assistant):

    def __init__(self):
        
        self.jokes = [     "I'm reading a book on anti-gravity… it's impossible to put down.",
    "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "I told my computer I needed a break… and it said 'No problem, I’ll crash.'",
    "Why don’t scientists trust atoms? Because they make up everything.",
    "I asked my dog what’s two minus two. He said nothing.",
    "Why did the scarecrow win an award? He was outstanding in his field.",
    "My WiFi went down for five minutes, so I had to talk to my family… they seem nice.",
    "What do you call fake spaghetti? An impasta.",
    "Why did the bicycle fall over? It was two-tired.",
    "I told my friend she drew her eyebrows too high. She looked surprised."   ]
    
    def respond(self, command):
        if command.cmd_type.lower()=="greeting":
            return " hey I am Jarvis a text based assistant by fizzy for your help"
        
        elif command.cmd_type.lower()=="joke":
            return random.choice(self.jokes)
        
        elif command.cmd_type.lower()=="intro":
            return self.intro()
        
        elif command.cmd_type.lower()=="exit":
            return "GoodBye!"

        else:
            return "Sorry, I don't understand that command."
        
    def __call__(self,command):
        return self.respond(command)
    
    def __str__(self):
        return "Jarvis AI assistant created by fizzy "
    
    def __secret_protocol(self,passcode):
        if passcode == "khul ja sim sim":
            return "Access Granted 🔓"
        else:
            return "Access Denied 🚫"

    def __dir__(self):
        return [x for x in super().__dir__() if x!='__secret_protocol']

class Command:
    
    def __init__(self,text):

        if text:
            self.input=text.lower()
        else:
            self.input=input("enter your message : ").strip().lower()
        
        self.cmd_type="unknown"
    
    def type_check(self):

        if "hello" in self.input or "hi" in self.input:
            self.cmd_type="greeting"
        
        elif "joke" in self.input:
            self.cmd_type="joke"

        elif "intro" in self.input:
            self.cmd_type = "intro"

        elif "exit" in self.input or "bye" in self.input:
            self.cmd_type = "exit"
        
        else:
            self.cmd_type = "unknown"



if __name__ == "__main__":
    jarvis = Jarvis()

    while True:
        print("\n===== Jarvis Assistant Menu =====\n")
        print("1. Give Jarvis a command ")
        print("2. View Jarvis intro (__str__)")
        print("3. Try secret protocol")
        print("4. View available methods (dir(jarvis))")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            user_input = input("Enter your command: ")
            cmd = Command(user_input)
            cmd.type_check()
            print(jarvis(cmd))

        elif choice == '2':
            print(str(jarvis))

        elif choice == '3':
            passcode = input("Enter the secret passcode: ")
            try:
                print(jarvis._Jarvis__secret_protocol(passcode))
            except AttributeError:
                print("Access method not found.")

        elif choice == '4':
            print(dir(jarvis))

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
