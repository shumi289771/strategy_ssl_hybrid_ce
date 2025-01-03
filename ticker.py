import yfinance as yf
import pandas as pd
import numpy as np



class Ticker:
    def __init__(self, name):
        self.name = name            # nom de la valeur boursiere, de la crypto, ...
        self.data = None                # les données récupérer de yfinance, avec les indicateurs tehcnique
        self.extension = ".csv"
        self.filename = self.name + "_ticker" + self.extension
        self.interval = None
        self.period = None


    def fetch_data(self, interval="", period = ""):
        if period != "":
            self.period = period
            self.interval = interval
        elif self.period == None:
           raise "period undefined"
        elif self.interval == None:
            raise "interval undefined"
    
        self.data = yf.Ticker(self.name).history(self.period , self.interval)
        if self.data.empty:
            raise ValueError(f"Aucune donnée disponible pour le ticker '{self.name}'")
        print("Données récupérées avec succès")
       

    def save_data(self):
        self.data.to_csv(self.filename)
        print(f"Données enregistrées dans {self.filename}")

    def load_data(self):
        self.data = pd.read_csv(self.filename)
        print("données chargées à partir de " + self.filename)

 
      
    
