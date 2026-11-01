import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantApp:
    def __init__(self,root):
        self.root  = root
        root.title("Restaurant Management App")
        root.geometry("800x600")
        root.configure(bg = "lightblue")

        self.setup_menu()
        self.setup_currency()

    def setup_menu(self):
            self.menu={
                "Fries": 2,
                "Spring rolls": 2,
                "Burger": 3,
                "Pizza": 4,
                "Amala and Stew": 5,
                "Soda": 2
            }
            self.frame = ttk.Frame(self.root)
            self.frame.place(relx= 0.5, rely= 0.5, anchor= "center")
            ttk.Label(
                self.frame,
                text = "Restaurand Order Mnagement",
                font = ("Arial", 12, "bold"),
            ).grid(row=0, columnspan=2)

            self.entries = {}

            for i, (item, price) in enumerate(self.menu.items(), 1):
                ttk.Label(
                    self.frame,
                    text=f"{item} (${price})"
                ).grid(row = i, column = 0, padx=10,pady=5)

                entry = ttk.Entry(self.frame,width=5)
                entry.grid(row=i, column = 1)
                self.entries[item] = entry

    def setup_currency(self):
         self.currency = tk.StringVar(value="USD")
         ttk.Label(self.frame, text = "Currency:").grid(
              row = 7, column =0
         )
         ttk.Combobox(
            self.frame,
            textvariable = self.currency,
            values = ("USD", "NGN"),
            state = "readonly"
         ).grid(row = 7, column = 1)

         ttk.Button(
              self.frame,
                text = "Place Order",
                command = self.place_order
         ).grid(row = 8, columnspan = 2, pady = 10)

    def place_order(self):
         total = 0
         rate = 1345 if self. currency.get() == "NGN" else 1
         symbol="₦" if rate == 1345 else "$"

         for item, entry in self.entries.items():
              try:
                   quantity = int(entry.get())
                   if quantity > 0:
                        total += quantity * self.menu[item] * rate
              except ValueError:
                   pass
         if total:
             messagebox.showinfo(
                   "order info",
                   f"Total: {symbol}{total}"
              )
         else:
              messagebox.showerror(
                   "Error",
                   "Please order at least one item"
              )



if __name__== "__main__":
    root= tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()