from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Fichas médicas'))
layout.addWidget(QPushButton('Estadísticas'))
layout.addWidget(QPushButton('Sincronizar'))
window.setLayout(layout)
window.show()
app.exec_()