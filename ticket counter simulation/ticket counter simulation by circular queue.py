
class Ticket:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front==-1
    
    def is_full(self):
        return (self.rear+1)%self.size == self.front

    def add_customer(self,customer):
        if self.is_full():
            print("Counter full, customer waits outside")
            return None

        elif self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear+1)%self.size
        
        self.queue[self.rear] = customer

    def serve_customer(self):

        if self.is_empty():
            print("counter is empty")
            return None
        temp = self.queue[self.front]

        if self.rear==self.front:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1)%self.size
        return f"customer <{temp}> served"
        
    def next_customer(self):
        if self.is_empty():
            print("counter is empty")
            return None
        return f"next customer : {self.queue[self.front]}"
    
    def display_counter(self):
        if self.is_empty():
            print("counter is empty")
            return None
        elif self.rear >= self.front:
            print("counter : ",self.queue[self.front : self.rear+1])
        else:
            print("counter : ",self.queue[self.front :]+self.queue[ :self.rear+1 ])




t = Ticket(3)

t.add_customer("A")
t.add_customer("B")
t.add_customer("C")      
t.add_customer("D")      

print(t.serve_customer())  
t.add_customer("D")      

print(t.next_customer())
t.display_counter()

print(t.serve_customer())
print(t.serve_customer())
t.display_counter()
t.serve_customer()
t.display_counter()

