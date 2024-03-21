import tkinter as tk
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.configure(background="#f0f0f0")

        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'INR': 73.94,
            # Add more currencies and exchange rates as needed
        }

        self.amount_var = tk.StringVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Amount:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="From Currency:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text="To Currency:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Converted Amount:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10)

        tk.Entry(self.root, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.from_currency_var).grid(row=1, column=1, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.to_currency_var).grid(row=2, column=1, padx=10, pady=10)
        tk.Entry(self.root, state='readonly', disabledforeground='black').grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Convert", command=self.convert_currency).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Clear All", command=self.clear_fields).grid(row=5, column=0, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
                messagebox.showerror("Error", "Invalid currencies selected!")
                return

            converted_amount = amount * (self.exchange_rates[to_currency] / self.exchange_rates[from_currency])
            self.to_currency_var.set(round(converted_amount, 2))

        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered!")

    def clear_fields(self):
        self.amount_var.set("")
        self.from_currency_var.set("")
        self.to_currency_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    currency_converter = CurrencyConverter(root)
    root.mainloop()
