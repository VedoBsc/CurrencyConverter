import tkinter as tk

languages = {
    "en": {"title": "Currency Converter", "button": "Convert"},
    "de": {"title": "Währungsrechner", "button": "Umrechnen"},
    "fr": {"title": "Convertisseur de devises", "button": "Convertir"},
    "es": {"title": "Conversor de monedas", "button": "Convertir"},
    "it": {"title": "Convertitore di valute", "button": "Convertire"},
    "pt": {"title": "Conversor de moedas", "button": "Converter"},
    "ru": {"title": "Конвертер валют", "button": "Преобразовать"},
}




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
        self.curr1.grid(row=1, column=0)

        # Auswahl
        self.t_curr = tk.StringVar(value="USD") #Main Currency ist USD
        self.drop = tk.OptionMenu(root, self.t_curr, *exchange_rates.keys()) #fügt ein option menu hinzu mit den Werten aus der exchange_rates dictionary
        self.drop.grid(row=0, column=2)
        #Auswahl der Sprache
        self.t_lang = tk.StringVar(value="en") #Main Language ist Englisch
        self.drop = tk.OptionMenu(root, self.t_lang, *languages.keys()) #fügt ein option menu hinzu mit den Sprachen aus der languages dictionary
        self.drop.grid(row=0, column=0) #ist die erste Reihe und die zweite Spalte
        self.t_lang.trace_add("write", self.update_language) #aktualisiert die Sprache zu aktualisieren

        # Button
        self.convert_button = tk.Button(root, command=self.convert) #Button um die Werte umzurechnen
        self.convert_button.grid(row=5, column=1, columnspan=3)
        self.convert_button.config(text= "Convert")

    
        

        # Label für Ausgabe
        self.curr2 = tk.Entry(root, state="disabled")
        self.curr2.grid(row=1, column=4, columnspan=3)
    
    def update_language(self, *args): #Methode um die Sprache zu aktualisieren
        lang = self.t_lang.get()
        self.root.title(languages[lang]["title"])
        self.convert_button.config(text=languages[lang]["button"])
    
    def convert(self):
        try:
            amount = float(self.curr1.get())
            rate = exchange_rates[self.t_curr.get()]
            result = round(amount * rate, 2) #rundet die ausgabe auf 2 nachkomma stellen
        except ValueError:
            result = "Wrong input" 
        
        self.curr2.config(state="normal")
        self.curr2.delete(0, "end")
        self.curr2.insert(0, str(result))
        self.curr2.config(state="disabled")
if __name__ == "__main__": #Gibt die GUI aus
    root = tk.Tk()
    app = Currency(root)
    root.mainloop()

