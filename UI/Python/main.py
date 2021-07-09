from incident import Incident
from helper import columns, get_province, get_cause, load_data, load_model
from pandas import concat
from ui import *


incidents = []

    
def bind():
    ui.minusButton.clicked.connect(remove_incident)
    ui.plusButton.clicked.connect(add_incident)
    ui.saveButton.clicked.connect(save_incident)
    ui.overviewList.itemPressed.connect(select_incident)


def init():
    global incidents
    incidents = [Incident(df, row) for row in range(len(df))]
    [ui.overviewList.addItem(str(incident)) for incident in incidents]


def predict():
    features = get_incident().features
    ui.hersteltijd_dt.setText(str(dt_model.predict(features)[0]))
    ui.hersteltijd_lr.setText(str(lr_model.predict(features)[0]))
    ui.hersteltijd_knn.setText(str(knn_model.predict(features)[0]))


def get_incident():
    row = ui.overviewList.currentRow()
    return incidents[row]


def update_map():
    province = get_province(int(get_incident().geocode))
    ui.mapLabel.setPixmap(QtGui.QPixmap(f"../../Data/Images/{province}.jpg"))
    ui.mapLabel.update()


def update_cause():
    cause = get_cause(get_incident().oorzaakcode)
    ui.oorzaakcode.setText(cause)
    ui.oorzaakcode.update()


def remove_incident():
    incidents.remove(get_incident())
    ui.overviewList.clear()
    [ui.overviewList.addItem(str(incident)) for incident in incidents]


def add_incident():
    new_incident = Incident(get_incident().df, 0)
    new_incident.meldnummer += 1
    incidents.insert(ui.overviewList.currentRow(), new_incident)
    ui.overviewList.clear()
    [ui.overviewList.addItem(str(incident)) for incident in incidents]


def save_incident():
    get_incident().update_values(ui)
    update_map()
    predict()
    df = concat([incident.df for incident in incidents])
    df.to_csv('../../Data/CSV/subset.csv', sep=';', index=False)


def select_incident(selected_item):
    get_incident().update_ui(ui)
    update_map()
    update_cause()


if __name__ == "__main__":
    # making application
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # binding data
    df = load_data('../../Data/CSV/subset.csv')
    dt_model, lr_model, knn_model = load_model('dt'), load_model('lr'), load_model('knn')
    init()
    bind()

    # displaying window and setting exit state
    MainWindow.show()
    sys.exit(app.exec_())
