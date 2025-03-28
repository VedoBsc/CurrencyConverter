glaze tkinter ahh tk

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

skibidi Currency:
    bop __init__(unc, root): #Konstruktor von GUI
        unc.root = root
        unc.root.geometry("400x200")  #Die Größe des Fensters
        unc.root.title("Currency Converter")



        # Entry-Feld
        unc.curr1 = tk.Entry(root)
        unc.curr1.grid(row=0, column=0)

        # Auswahl
        unc.t_curr = tk.StringVar(value="USD") #Main Currency ist USD
        unc.drop = tk.OptionMenu(root, unc.t_curr, *exchange_rates.keys()) #fügt ein option menu hinzu mit den Werten aus der exchange_rates dictionary
        unc.drop.grid(row=0, column=1)
        #Auswahl der Sprache
        unc.t_lang = tk.StringVar(value="en") #Main Language ist Englisch
        unc.drop = tk.OptionMenu(root, unc.t_lang, *languages.keys()) #fügt ein option menu hinzu mit den Sprachen aus der languages dictionary
        unc.drop.grid(row=0, column=2) #ist die erste Reihe und die zweite Spalte
        unc.t_lang.trace_add("write", unc.update_language) #aktualisiert die Sprache zu aktualisieren

        # Button
        unc.convert_button = tk.Button(root, command=unc.convert) #Button um die Werte umzurechnen
        unc.convert_button.grid(row=1, column=0, columnspan=3)
        unc.convert_button.config(text= "Convert")




        # Label für Ausgabe
        unc.curr2 = tk.Entry(root, state="disabled")
        unc.curr2.grid(row=2, column=0, columnspan=3)

    bop update_language(unc, *args): #Methode um die Sprache zu aktualisieren
        lang = unc.t_lang.get()
        unc.root.title(languages[lang]["title"])
        unc.convert_button.config(text=languages[lang]["button"])

    bop convert(unc):
        hawk:
            amount = float(unc.curr1.get())
            rate = exchange_rates[unc.t_curr.get()]
            result = round(amount * rate, 2) #rundet die ausgabe auf 2 nachkomma stellen
        tuah ValueError:
            result = "Wrong input" 

        unc.curr2.config(state="normal")
        unc.curr2.delete(0, "end")
        unc.curr2.insert(0, str(result))
        unc.curr2.config(state="disabled")
chat is this real __name__ == "__main__": #Gibt die GUI aus
    root = tk.Tk()
    app = Currency(root)
    root.mainloop()



