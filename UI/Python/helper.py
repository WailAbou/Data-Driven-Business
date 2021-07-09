from pandas import read_csv, Series
from pickle import load as pickle_load

cause_df = read_csv('../../Data/CSV/oorzaakcodes.csv', sep=';')
causes = Series(cause_df.Oorzaak.values, index=cause_df.Code).to_dict()

columns = ['meldnummer', 'oorzaakcode', 'prioriteit', 'melddatum', 'geocode', 'beschrijving', 'hersteltijd', 'hersteltijd_15', 'hersteltijd_dt', 'hersteltijd_lr', 'hersteltijd_knn']

provinces = {
    'drenthe': [],
    'flevoland': [],
    'friesland': [],
    'gelderland': [210, 508, 666],
    'groningen': [3],
    'limburg': [],
    'noordbrabant': [],
    'noordholland': [76, 586, 589],
    'overijsel': [],
    'utrecht': [531],
    'zeeland': [],
    'zuidholland': [112, 114, 165, 539, 542, 555, 564]
}


def load_data(file_name):
    loaded_df = read_csv(file_name, sep=';')
    sorted_df = loaded_df.sort_values(by=['prioriteit', 'melddatum'], ascending=False)
    return sorted_df


def load_model(file_name):
    with open(f'../../Data/Model/{file_name}.pkl', 'rb') as file:
        return pickle_load(file)


def get_province(geocode: int) -> str:
    province = list(provinces)[0]
    for i, geocodes in enumerate(provinces.values()):
        if geocode in geocodes:
            province = list(provinces)[i]
    return province


def get_cause(causecode: int) -> str:
    cause = causes.get(causecode) 
    return 'Onbekende Oorzaak' if cause is None else cause 
