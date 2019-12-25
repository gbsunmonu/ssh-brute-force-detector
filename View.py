import os
import webbrowser

from PyQt5.QtGui import QPixmap, QMouseEvent, QImage
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

import sys

from PyQt5.uic.properties import QtCore

from my_ui import *
import ParsingPcapUtil


class Ui_MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonOpenPcap.setText("open pcap")
        self.pushButtonDetail.setText("detail")

        self.pushButtonOpenPcap.clicked.connect(self.openfile)
        self.pushButtonDetail.clicked.connect(self.showDetial)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "brute-force-detector"))


    def openfile(self):
        openfile_names = QFileDialog.getOpenFileNames(self,'choose file','','Pcap files(*.pcap)')
        pcap_count_content = ""
        for file_path in openfile_names[0]:
            pcap_count_content += file_path + "\n"
        ParsingPcapUtil.make_table(openfile_names[0])

        pixmap = QPixmap('avgPacketSizePerProcess.png')
        self.packetNumberDprocessNumber.setText("Total Packet Count / Process count")
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.packetNumberDprocessNumber_frame.setScene(scene)

        pixmap2 = QPixmap('avgPacketSize.png')
        self.packetSizeDpacketCount.setText("Total Packet Size / Packet Count")
        scene2 = QGraphicsScene()
        scene2.addPixmap(pixmap2)
        self.packetSizeDpacketCount_frame.setScene(scene2)
        self.pcapSelected.setText(pcap_count_content)

    def showDetial(self):
        self.imgshow = PaintPicture()


class PaintPicture(QDialog):
    def __init__(self, parent=None):
        super(PaintPicture, self).__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.show()
        self.showImage()

    def showImage(self):
        filename = 'high_dpi_avgPacketSize.png'
        image = QImage(filename)

        filename2 = "high_dpi_avgPacketSizePerProcess.png"
        image2 = QImage(filename2)

        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

        self.imageLabel2 = QLabel()
        self.imageLabel2.setPixmap(QPixmap.fromImage(image2))

        layout = self.layout()
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.imageLabel2)
        webbrowser.open('file://' + os.path.realpath("avgPacketSizePerProcess.html"))
        webbrowser.open('file://' + os.path.realpath("avgPacketSize.html"))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Ui_MainWindow()
    main_win.show()
    sys.exit(app.exec_())