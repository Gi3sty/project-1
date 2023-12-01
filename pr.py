import tkinter as tk

# Definizione di una classe Fornitore per rappresentare i fornitori
class Fornitore:
    def __init__(self, nome):
        self.nome = nome
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

# Definizione di una classe Prodotto per rappresentare i prodotti
class Prodotto:
    def __init__(self, nome, prezzo, iva):
        self.nome = nome
        self.prezzo = prezzo
        self.iva = iva

# Simulazione di alcuni dati di fornitori e prodotti
fornitore1 = Fornitore("Fornitore A")
fornitore1.aggiungi_prodotto(Prodotto("Prodotto 1", 10.0, 22))  # IVA espressa in percentuale (22%)
fornitore1.aggiungi_prodotto(Prodotto("Prodotto 2", 15.0, 18))  # IVA espressa in percentuale (18%)

fornitore2 = Fornitore("Fornitore B")
fornitore2.aggiungi_prodotto(Prodotto("Prodotto 3", 20.0, 25))  # IVA espressa in percentuale (25%)
fornitore2.aggiungi_prodotto(Prodotto("Prodotto 4", 12.0, 15))  # IVA espressa in percentuale (15%)


# Definizione di una classe Fornitore per rappresentare i fornitori
class Fornitore:
    def __init__(self, nome):
        self.nome = nome
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

# Definizione di una classe Prodotto per rappresentare i prodotti
class Prodotto:
    def __init__(self, nome, prezzo, iva):
        self.nome = nome
        self.prezzo = prezzo
        self.iva = iva

# Simulazione di alcuni dati di fornitori e prodotti
fornitore1 = Fornitore("Fornitore A")
fornitore1.aggiungi_prodotto(Prodotto("Prodotto 1", 10.0, 22))  # IVA espressa in percentuale (22%)
fornitore1.aggiungi_prodotto(Prodotto("Prodotto 2", 15.0, 18))  # IVA espressa in percentuale (18%)

fornitore2 = Fornitore("Fornitore B")
fornitore2.aggiungi_prodotto(Prodotto("Prodotto 3", 20.0, 25))  # IVA espressa in percentuale (25%)
fornitore2.aggiungi_prodotto(Prodotto("Prodotto 4", 12.0, 15))  # IVA espressa in percentuale (15%)

# Funzione per cercare i prodotti di un fornitore
def cerca_prodotti_per_fornitore(nome_fornitore):
    for fornitore in [fornitore1, fornitore2]:
        if fornitore.nome == nome_fornitore:
            return fornitore.prodotti
    return None

# Codice Kivy per l'applicazione mobile
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10)

        label_nome_fornitore = Label(text="Nome Fornitore:")
        layout.add_widget(label_nome_fornitore)

        self.entry_nome_fornitore = TextInput(multiline=False)
        layout.add_widget(self.entry_nome_fornitore)

        button_cerca = Button(text="Cerca Prodotti")
        button_cerca.bind(on_press=self.cerca_prodotti)
        layout.add_widget(button_cerca)

        self.area_testo = TextInput(multiline=True)
        layout.add_widget(self.area_testo)

        return layout

    def cerca_prodotti(self, instance):
        nome_fornitore = self.entry_nome_fornitore.text
        prodotti_fornitore = cerca_prodotti_per_fornitore(nome_fornitore)
        if prodotti_fornitore:
            self.area_testo.text = f"Prodotti forniti da {nome_fornitore}:\n"
            for prodotto in prodotti_fornitore:
                self.area_testo.text += f"Nome: {prodotto.nome}, Prezzo: {prodotto.prezzo}€, IVA: {prodotto.iva}%\n"
        else:
            self.area_testo.text = "Fornitore non trovato."

# Esecuzione dell'applicazione Kivy
if __name__ == '__main__':
    MyApp().run()
