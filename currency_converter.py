import tkinter as tk

exchange_rates = {
    "USD": 1.08,  # 1 EUR = 1.08 USD
    "CHF": 0.98,  # 1 EUR = 0.98 CHF
    "GBP": 0.85,  # 1 EUR = 0.85 GBP
}

class Currency:
    def __init__(self, root): #Konstruktor von GUI
        self.root = root
        self.root.geometry("400x200")  #Die Größe des Fensters
        self.root.title("Currency Converter")
        

        # Entry-Feld
        self.curr1 = tk.Entry(root)
        self.curr1.grid(row=0, column=0)

        # Auswahl
        self.t_curr = tk.StringVar(value="USD")
        self.drop = tk.OptionMenu(root, self.t_curr, *exchange_rates.keys())
        self.drop.grid(row=0, column=1)
        
        # Button
        self.convert_button = tk.Button(root, command=self.convert)
        self.convert_button.grid(row=1, column=0, columnspan=3)
        self.convert_button.config(text= "Convert")
        

        # Label für Ausgabe
        self.curr2 = tk.Entry(root, state="disabled")
        self.curr2.grid(row=2, column=0, columnspan=3)

    def convert(self):
        try:
            amount = float(self.curr1.get())
            rate = exchange_rates[self.t_curr.get()]
            result = round(amount * rate, 2)
        except ValueError:
            result = "Falsche Eingabe"
        
        self.curr2.config(state="normal")
        self.curr2.delete(0, "end")
        self.curr2.insert(0, str(result))
        self.curr2.config(state="disabled")
if __name__ == "__main__": #Gibt die GUI aus
    root = tk.Tk()
    app = Currency(root)
    root.mainloop()

