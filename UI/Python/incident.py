import random


properties = ['oorzaakcode', 'hersteltijd', 'prioriteit', 'melddatum', 'geocode', 'beschrijving', 'hersteltijd_dt', 'hersteltijd_lr', 'hersteltijd_knn']


class Incident:
    def __init__(self, df, i):
        for prop in properties:
            value = getattr(df.iloc[i], prop)
            setattr(self, prop, value)

    def __str__(self):
        return f'Prioriteit: {self.prioriteit}\nMelddatum: {self.melddatum}\nHersteltijd: {self.hersteltijd}\n'
