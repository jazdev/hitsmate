#!/usr/bin/python

"""
   Copyright 2014 Jasdev Singh

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import uuid

# Tkinter
try:
    import Tkinter as tk     ## Python 2.x
except ImportError:
    import tkinter as tk     ## Python 3.x 

import ttk
import tkMessageBox
from ttk import Frame, Style

# pillow
from PIL import Image, ImageTk

# Tkintertable
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

import scipy as sp
from scipy.stats import gamma
import matplotlib.pyplot as plt



__author__ = "Jasdev Singh"
__copyright__ = "Copyright (C) 2014 Jasdev Singh"
__credits__ = ["Jasdev Singh"]
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "Jasdev Singh"
__email__ = "jasdev@singh.am"
__status__ = "Development"



class HitsMateFrame(tk.Frame):
    """
        This is the base class for the program.
    """
    # window count
    count = 0
    randomWebLogsWindowOpenedFlag = False
    graphsWindowOpenedFlag = False



    def __init__(self, parent):
        """
            Initialize the parent Frame
        """
        
        tk.Frame.__init__(self, parent)            
        self.parent = parent
        self.initUI()



    def initUI(self):
        """
            Method for initializing the root window elements. 

            All root level buttons and labels are initialized here.
        """

        self.parent.title("Hitsmate: A simple web traffic estimator")
        self.pack(fill=tk.BOTH, expand=1)

        # canvas for logo
        TweetimentCanvas = tk.Canvas(self.parent, height=130, width=600)
        TweetimentCanvas.create_text(300, 50, font=("Purisa", 40), text = "HITSMATE")
        TweetimentCanvas.create_text(300, 100, font=("Purisa", 20), text = "Web traffic predictor")
        TweetimentCanvas.place(x = 100, y = 40, width = 600, height = 130)

        # button for random data
        global GenRandomLogsButton
        GenRandomLogsButton = tk.Button(self.parent, text = "Generate Random Web Logs", command = self.genRandomWebLogs, bg="blue", fg="white")
        GenRandomLogsButton.place(x = 160, y = 220, width = 200, height = 30)
       
        # button for model generation
        global GenPredictionModelButton
        GenPredictionModelButton = tk.Button(self.parent, text = "Generate Prediction Model", command = self.genPredictionModel, bg="blue", fg="white")
        GenPredictionModelButton.place(x = 420, y = 220, width = 200, height = 30)

        # button for showing graphs
        global ShowGraphsButton
        ShowGraphsButton = tk.Button(self.parent, text = "Show Graphs", command = self.showGraphs, bg="blue", fg="white")
        ShowGraphsButton.place(x = 160, y = 280, width = 200, height = 30)
       
        # button for future traffic prediction
        global PredictFutureButton
        PredictFutureButton = tk.Button(self.parent, text = "Predict Future Traffic", command = self.predictFutureTraffic, bg="blue", fg="white")
        PredictFutureButton.place(x = 420, y = 280, width = 200, height = 30)

        

    def genRandomWebLogs(self):
        """
            Method for generating random web log data.
        """

        self.count += 1
        if self.randomWebLogsWindowOpenedFlag == False:

            self.randomWebLogsWindowOpenedFlag = True # set window opened
            global RandomWebLogsWindow

            def toggleFlag():
                self.randomWebLogsWindowOpenedFlag = False # set window closed
                RandomWebLogsWindow.destroy()

            RandomWebLogsWindow = tk.Toplevel(self)
            RandomWebLogsWindow.minsize(300, 500)
            RandomWebLogsWindow.geometry("300x500+100+100")
            RandomWebLogsWindow.title("Random web log data")
            RandomWebLogsWindow.config(bd=5)
            RandomWebLogsWindow.protocol("WM_DELETE_WINDOW", toggleFlag)

            x = sp.arange(1, 31 * 24) # 1 month of traffic data
            y = sp.array(200 * (sp.sin(2 * sp.pi * x / (7 * 24))), dtype=int)
            y += gamma.rvs(15, loc=0, scale=100, size=len(x))
            y += 2 * sp.exp(x / 100.0)
            y = sp.ma.array(y, mask=[y < 0])
            sp.savetxt(os.path.join("sample_data", "sample_web_traffic.tsv"), list(zip(x, y)), delimiter="\t", fmt="%s")
            model = TableModel() # create a new TableModel for table data
            table = TableCanvas(RandomWebLogsWindow, model=model, editable=False) # create a new TableCanvas for showing the table
            table.createTableFrame()
            tableData = {} # dictionary for storing table data
            for k, v in list(zip(x,y)):
                tableData[uuid.uuid4()] = {'Hour': str(k), 'Hits': str(v)}
            model.importDict(tableData)
            table.resizeColumn(0, 100)
            table.resizeColumn(1, 100)
            table.sortTable(columnName='Hour')
            table.redrawTable()

        else:
            RandomWebLogsWindow.deiconify()  



    def genPredictionModel(self):
        """
            Method for model generation.
        """
        colors = ['g', 'r']
        linestyles = ['-', '--']

        def plot_models(x, y, models, fname):
            plt.clf()
            plt.scatter(x, y, s=10)
            plt.title("Last month's web traffic")
            plt.xlabel("Time")
            plt.ylabel("Hits / Hour")
            plt.xticks([week * 7 * 24 for week in range(10)], ['Week %i' % week for week in range(10)])
            mx = sp.linspace(0, x[-1], 1000)
            for model, style, color in zip(models, linestyles, colors):
                plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

            plt.legend(["Degree=%i" % m.order for m in models], loc="upper left")
            plt.autoscale(tight=True)
            plt.ylim(ymin=0)
            plt.grid(True, linestyle='-', color='0.75')
            plt.savefig(fname)
            return

        data = sp.genfromtxt("sample_data/sample_web_traffic.tsv", delimiter="\t")
        x = data[:, 0]
        y = data[:, 1]
        print("Number of invalid entries:", sp.sum(sp.isnan(y)))
        x = x[~sp.isnan(y)]
        y = y[~sp.isnan(y)]
        fp2, residuals2, rank2, sv2, rcond2 = sp.polyfit(x, y, 2, full=True)
        fp3, residuals3, rank3, sv3, rcond3 = sp.polyfit(x, y, 3, full=True)
        print "Error 2: ", str(residuals2)
        print "Error 3: ", str(residuals3)
        if residuals2 < residuals3:
            print "Using 2nd degree model"
            f2 = sp.poly1d(fp2)
            print f2
            plot_models(x, y, [f2], os.path.join("graphs", "Curve_fit.png"))
        else:
            print "Using 3rd degree model"
            f3 = sp.poly1d(fp3)
            print f3
            plot_models(x, y, [f3], os.path.join("graphs", "Curve_fit.png"))
        
        tkMessageBox.showinfo("Done", "Models successfully trained. Click 'Show Graphs' to see them.", parent = self.parent)
        return



    def showGraphs(self):
        """
            Method for showing graphs.
        """

        self.count += 1
        if self.graphsWindowOpenedFlag == False:

            self.graphsWindowOpenedFlag = True # set window opened
            global GraphsWindow

            def toggleFlag():
                self.graphsWindowOpenedFlag = False # set window closed
                GraphsWindow.destroy()

            GraphsWindow = tk.Toplevel(self)
            GraphsWindow.minsize(300, 500)
            GraphsWindow.geometry("810x610+50+50")
            GraphsWindow.title("Graph showing curve fitted to the data")
            GraphsWindow.config(bd=5)
            GraphsWindow.protocol("WM_DELETE_WINDOW", toggleFlag)

            graph = Image.open("graphs/Curve_fit.png")
            graphPhoto = ImageTk.PhotoImage(graph)
            graphLabel = tk.Label(GraphsWindow, image=graphPhoto)
            graphLabel.image = graphPhoto 
            graphLabel.place(x = 0, y = 0, width = 800, height = 600)



    def predictFutureTraffic(self):
        """
            Method for future traffic prediction.
        """
        pass
        


def main():
    """
        The main function. 
        This function sets up the root Tkinter window.
    """
    # initialize root frame and run the app
    global root
    root = tk.Tk()
    root.geometry("800x400+100+100")
    app = HitsMateFrame(root)
    root.mainloop()  



if __name__ == '__main__':
    main() 
