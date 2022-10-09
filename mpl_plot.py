import imp
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import QtWidgets
from matplotlib.lines import Line2D
from matplotlib.figure import Figure


class Mplplot(FigureCanvas):
    def __init__(self,parent = None,width = 5,height = 3,dpi = 100,):
         # normalized for 中文显示和负号
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig = Figure(figsize=(width,height),dpi=dpi)
        super(Mplplot,self).__init__(self.fig)
        self.setParent(parent)
        self.axes = self.fig.add_subfigure(111)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def add_line(self,x_data,y_data):
        self.line = Line2D(x_data,y_data)

        self.axes.set_xlim(np.min(x_data), np.max(x_data))
        self.axes.set_ylim(np.min(y_data), np.max(y_data) + 5)  # y 轴稍微多一点，会好看一点
        self.axes.set_xlabel('x 坐标 ')  # 设置坐标名称
        self.axes.set_ylabel('y 坐标 ')
        # 在曲线下方填充颜色
        # self.ax.fill_between(x_data, y_data, color='g', alpha=0.1)
        # self.ax.legend([self.line], ['sinx'])  # 添加图例
        # ------------------------------------------------------#
        self.axes.add_line(self.line)

    