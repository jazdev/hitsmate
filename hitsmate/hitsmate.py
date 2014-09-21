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