import tkinter as tk
from tkinter import messagebox

class LoanCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Loan Calculator")

        # Create input fields
        self.label_principal = tk.Label(root, text="Principal Amount:")
        self.label_principal.grid(row=0, column=0, padx=10, pady=10)
        self.entry_principal = tk.Entry(root)
        self.entry_principal.grid(row=0, column=1, padx=10, pady=10)

        self.label_rate = tk.Label(root, text="Annual Interest Rate (%):")
        self.label_rate.grid(row=1, column=0, padx=10, pady=10)
        self.entry_rate = tk.Entry(root)
        self.entry_rate.grid(row=1, column=1, padx=10, pady=10)

        self.label_years = tk.Label(root, text="Loan Term (years):")
        self.label_years.grid(row=2, column=0, padx=10, pady=10)
        self.entry_years = tk.Entry(root)
        self.entry_years.grid(row=2, column=1, padx=10, pady=10)

        # Create calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_payment)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate_payment(self):
        try:
            principal = float(self.entry_principal.get())
            annual_rate = float(self.entry_rate.get())
            years = int(self.entry_years.get())

            # Calculate monthly payment
            monthly_rate = annual_rate / 100 / 12
            months = years * 12
            if monthly_rate != 0:
                monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
            else:
                monthly_payment = principal / months

            # Display the monthly payment
            messagebox.showinfo("Monthly Payment", f"Your Monthly Payment will be: ${monthly_payment:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanCalculatorApp(root)
    root.mainloop()
