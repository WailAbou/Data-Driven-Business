from pandas import DataFrame 
from helper import columns


class Incident:
    def __init__(self, df, row):
        for column in columns:
            value = getattr(df.iloc[row], column)
            setattr(self, column, value)

    def update_ui(self, ui):
        for column in columns:
            try:
                ui_text = getattr(ui, column)
                incident_text = str(getattr(self, column))
                ui_text.setText(incident_text)
            except AttributeError:
                pass

    def update_values(self, ui):
        for column in columns:
            try: 
                ui_text = getattr(ui, column)
                setattr(self, column, ui_text.toPlainText())
            except AttributeError:
                if column in ['hersteltijd_dt', 'hersteltijd_lr', 'hersteltijd_knn']:
                    ui_text = getattr(ui, column)
                    setattr(self, column, ui_text.text())

    @property
    def df(self):
        values = [[getattr(self, column) for column in columns]]
        df = DataFrame(values, columns=columns)
        return df

    @property
    def features(self):
        return [[int(self.geocode), int(self.prioriteit), int(self.oorzaakcode)]]

    def __str__(self):
        return f'Prioriteit: {self.prioriteit}\nMelddatum: {self.melddatum}\nHersteltijd: {self.hersteltijd}\n'
