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

# Tkinter
try:
    import Tkinter as tk     ## Python 2.x
except ImportError:
    import tkinter as tk     ## Python 3.x 

import ttk
import tkMessageBox
from ttk import Frame, Style

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
       
        
    def genRandomWebLogs(self):
        """
            Method for generating random web log data.
        """
        pass

    def genPredictionModel(self):
        """
            Method for model generation.
        """
        pass

    def showGraphs(self):
        """
            Method for showing graphs.
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