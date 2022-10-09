import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow,QVBoxLayout,QGridLayout
from Ui_MultimeterWindow import Ui_MultimeterMainWindow #导入QtTest文件
from PyQt6.QtCore import QThread,pyqtSignal,QMutex,QTimer
import matplotlib
matplotlib.use("Qt5Agg")

from MultimeterFigure import MultimeterFigure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import time
import random
class MultimeterUI(QMainWindow, Ui_MultimeterMainWindow):
    def __init__(self,parent = None):
        # super(Ui_MultimeterMainWindow,self).__init__(parent)
        super( MultimeterUI, self).__init__(parent)
        self.setupUi(self)
        self.initAPP()
        
    
    def initAPP(self):
        # app 初始化
        # 设置名称
        self.setWindowTitle("34470A")
        self.measure_timer = QTimer(self)
        self.measure = MeasureModule(self.measure_timer)
        self.measure._signal_update.connect(self.update_data_thread_slot)
        # 信号槽连接
        self.vertival_scale_dial.valueChanged.connect(self.dialtest)
        self.close_button.clicked.connect(self.close)
        self.start_button.clicked.connect(self.startbuttontest)
        self.setupFigure()


    def setupFigure(self):
        self.phase_fig = MultimeterFigure(width=5, height=3, dpi=72)
        self.fig_ntb = NavigationToolbar(self.phase_fig, self)
        self.gridlayout = QGridLayout(self.figure_box)
        self.gridlayout.addWidget(self.phase_fig)
        self.gridlayout.addWidget(self.fig_ntb)
        self.x_data = np.arange(-10, 10, 0.1)
        y_data = np.sin(self.x_data)
        self.phase_fig.add_line(self.x_data, y_data)

    def startbuttontest(self):
        print("start")
        # self.update_thread.start()
        self.measure.start_measure()

    def dialtest(self):
        print(self.vertival_scale_dial.value())

    def update_data_thread_slot(self,data = None):
        # print("update data")
        # print(data)
        # pass
        self.phase_fig.line.set_data(data,data)
        # set_ydata(data)  #(data['sin_data'])  # 更新数据
        self.phase_fig.draw()  # 重新画图



class MeasureModule(QThread):
    _signal_update = pyqtSignal(list)
    def __init__(self,measure_timer) -> None:
        super(MeasureModule, self).__init__(None)
        self.measure_timer = measure_timer
        self.measure_timer.timeout.connect(self.measure)
        self.lasttime = time.time()
        self.data = []

    def start_measure(self,dt = 100):
        # 多少ms的采样间隔
        self.measure_timer.start(dt)
        print("measure start")

    def measure(self):
        # 获取测量数据
        self.data.append(random.randint(0,500))
        print("get measured data")
        self._signal_update.emit(self.data) 

if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MultimeterWindow = MultimeterUI()
    MultimeterWindow.show()
    sys.exit(app.exec())