
class Priority:
    def __init__(self):
        self.queue = []
    
    def admit_patient(self,name,priority):
        
        def get_priority(queue):
            return queue[1]
        
        self.queue.append((name,priority))
        self.queue.sort(key=get_priority,reverse=True)

    def is_empty(self):
        return len(self.queue)==0
    
    def treat_patient(self):
        if self.is_empty():
            print("no patient left")
            return
        else:
            print("treated patient : ",(self.queue.pop(0))[0])
    
    def next_patient(self):
        if self.is_empty():
            return
        return self.queue[0][0]
    
    def display_info(self):
        print("remaining patients : ",[f"{i[0]}({i[1]})" for i in self.queue])
        print("next patient : ",self.next_patient())

hospital = Priority()

hospital.admit_patient("ali",2)
hospital.admit_patient("sana",5)
hospital.admit_patient("bilal",1)
hospital.admit_patient("zoya",4)
hospital.admit_patient("hamza",3)

hospital.display_info()

while not hospital.is_empty():
    hospital.treat_patient()
    hospital.display_info()

