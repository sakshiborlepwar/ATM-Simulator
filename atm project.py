import tkinter as tk
from tkinter import messagebox

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("400x400")
        self.balance = 1000.0
        self.pin = "1234"
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="ATM Login", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text="Enter PIN:").pack()
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=10)
        tk.Button(self.root, text="Login", command=self.check_pin).pack(pady=10)

    def check_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Incorrect PIN!")

    def create_main_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="ATM Menu", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Check Balance", command=self.check_balance, width=20).pack(pady=5)
        tk.Button(self.root, text="Deposit", command=self.deposit_money, width=20).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_money, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=20)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is ₹{self.balance:.2f}")

    def deposit_money(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter amount to deposit:").pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        tk.Button(self.root, text="Deposit", command=self.do_deposit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def do_deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Success", f"₹{amount:.2f} deposited successfully.")
                self.create_main_menu()
            else:
                messagebox.showerror("Error", "Enter a valid amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    def withdraw_money(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter amount to withdraw:").pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        tk.Button(self.root, text="Withdraw", command=self.do_withdraw).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def do_withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if 0 < amount <= self.balance:
                self.balance -= amount
                messagebox.showinfo("Success", f"₹{amount:.2f} withdrawn successfully.")
                self.create_main_menu()
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
root = tk.Tk()
app = ATMApp(root)
root.mainloop()
