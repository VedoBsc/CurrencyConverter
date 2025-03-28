import tkinter as tk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Meine Tkinter GUI")

        # Label
        self.label = tk.Label(root, text="Gib deinen Namen ein:")
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(root, text="Anzeigen", command=self.anzeigen)
        self.button.pack(pady=10)

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def anzeigen(self):
        name = self.entry.get()
        self.output_label.config(text=f"Hallo, {name}!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()

