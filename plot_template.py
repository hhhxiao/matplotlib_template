import matplotlib.pyplot as plt
import numpy as np
from typing import List
import matplotlib as mpl

class LineData:
    x : list
    y : list
    label : str

    def __init__(self, x, y,label : str = '') -> None:
        self.x = x
        self.y = y
        self.label = label
        pass
 
       
class SubPlotData():
    data : List[LineData]
    label_x :str
    label_y: str
    sub_title : str



    def __init__(self,data: List[LineData], label_x: str = '',label_y : str= '', title: str = '') -> None:
        self.data = data
        self.label_x = label_x
        self.label_y = label_y
        self.sub_title = title


class MultPlot():
    sub_plot_data: List[SubPlotData]
    title: str
    row : int
    col : int
    line_width : float = 2.5
    font_size: int = 18
    scala_x : int = 8
    scala_y : int = 6

    def __init__(self, sub_plot_data: List[SubPlotData], title : str = '',  row : int = 1,col : int = 1) -> None:
        self.sub_plot_data = sub_plot_data
        self.title = title
        self.row =row
        self.col = col
        if len(self.sub_plot_data) > row * col:
            raise Exception("Error len in sub plot data")

    def set_figure_scala(self, x,y):
        self.scala_x = x
        self.scala_y = y 


    def plot(self):
        mpl.rcParams['axes.linewidth'] = self.line_width
        plt.figure(figsize = (self.col * self.scala_x,self.row * self.scala_y))
        plt.subplots_adjust(wspace=0.4,hspace=0.4,top=0.80,bottom=0.20)
        plt.suptitle(self.title,fontsize=self.font_size + 2)

        for sub in range(len(self.sub_plot_data)):
            d = self.sub_plot_data[sub]
            ax = plt.subplot(self.row,self.col,sub + 1)
            ax.set_title(d.sub_title,fontsize = self.font_size)
            ax.set_xlabel(d.label_x,fontsize = self.font_size)
            ax.set_ylabel(d.label_y, fontsize = self.font_size)
            ax.xaxis.set_tick_params(width=self.line_width)
            ax.yaxis.set_tick_params(width=self.line_width)

            plt.xticks(fontsize=18)
            plt.yticks(fontsize=18)

            for line in d.data:
                plt.plot(line.x,line.y,label=line.label,linewidth=self.line_width)
                plt.legend(frameon=False)


    def show(self):
        plt.show()


if __name__ == '__main__':
    x = np.linspace(0, 2 * np.pi, 400)
    y1 = np.sin(x ** 2)
    y2 = np.sin(x)
    y3 = np.sin(x/ np.pi)
    l1 = LineData(x,y1)
    l2 = LineData(x,y2)
    l3 = LineData(x,y3)

    s1 = SubPlotData([l1],label_x="test label x",label_y="test label y",title='sub titles')
    s2 = SubPlotData([l2],label_x="test label x",label_y="test label y",title='sub titles')
    s3 = SubPlotData([l3],label_x="test label x",label_y="test label y",title='sub titles')


    plot = MultPlot([s1,s2,s3],row=2,col=2,title="this is the total title")
    plot.set_figure_scala(5,5)
    plot.plot()

    plot.show()


