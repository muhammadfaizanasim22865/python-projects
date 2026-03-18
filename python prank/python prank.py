import tkinter as tk
from tkinter import simpledialog, messagebox
import time

def prank():
   
    root = tk.Tk()
    root.withdraw() 
    
 
    user_input = simpledialog.askinteger("Number Guess", "Think of a number: ")
    
    if user_input is not None:  
        
        init_window = tk.Toplevel()
        init_window.title("Initializing")
        tk.Label(init_window, text="Initializing...", font=("Arial", 16)).pack(padx=20, pady=20)
        init_window.update()
        
      
        time.sleep(2)  
        
        init_window.destroy()  
        
        messagebox.showinfo("Guess", f"You are thinking of number {user_input}!")
    else:
        messagebox.showwarning("Warning", "You didn't enter a number!")


prank()
