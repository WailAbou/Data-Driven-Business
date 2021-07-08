from incident import Incident, properties
from helper import get_province, get_cause, load_data
from pandas import concat
from ui import *


incidents = []

    
def bind():
    ui.minusButton.clicked.connect(delete_incident)
    ui.plusButton.clicked.connect(add_incident)
    ui.saveButton.clicked.connect(save_incident)
    ui.overviewList.itemPressed.connect(select_incident)


def refresh():
    global incidents
    incidents = [Incident(df, i) for i in range(len(df))]
    ui.overviewList.clear()
    [ui.overviewList.addItem(str(incident)) for incident in incidents]



def insert_row(row_number, dff, row_value):
    df1 = dff[0:row_number]
    df2 = dff[row_number:]
    df1.loc[row_number]=row_value
    df_result = concat([df1, df2])
    df_result.index = [*range(df_result.shape[0])]
    return df_result


def delete_incident():
    global df
    row = ui.overviewList.currentRow()
    index = len(df) - 1 if row == -1 else row
    df = df.drop(index=index)
    refresh()



def add_incident():
    global df
    row = ui.overviewList.currentRow()
    index = len(df) - 1 if row == -1 else row
    df = concat([df.iloc[:index], df.iloc[[index]], df.iloc[index:]]).reset_index(drop=True)
    df.iloc[index, df.columns.get_loc('meldnummer')] += 1
    refresh()


def save_incident():
    index = ui.overviewList.currentRow()
    for prop in properties:
        ui_text = getattr(ui, prop)
        try: df.iloc[index, df.columns.get_loc(prop)] = ui_text.toPlainText()
        except AttributeError: pass
    df.to_csv('../../Data/CSV/subset.csv', sep=';', index=False)
    refresh()


def select_incident(clicked_incident):
    row = ui.overviewList.currentRow()
    selected_incident = incidents[row]

    for prop in properties:
        ui_text = getattr(ui, prop)
        incident_text = str(getattr(selected_incident, prop))
        ui_text.setText(incident_text)
    
    province = get_province(selected_incident.geocode)
    ui.mapLabel.setPixmap(QtGui.QPixmap(f"../../Data/Images/{province}.jpg"))

    cause = get_cause(selected_incident.oorzaakcode)
    ui.oorzaakcode.setText(cause)


if __name__ == "__main__":
    # making application
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # binding data
    df = load_data('../../Data/CSV/subset.csv')
    refresh()
    bind()

    # displaying window and setting exit state
    MainWindow.show()
    sys.exit(app.exec_())
