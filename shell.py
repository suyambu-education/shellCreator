#!/bin/bash

# --- imports ------
import os
from colors import *
from colorama import *
import printhelp

#-------------------
#------variables --------

#-------------------
class Shell:
    
    def __init__(self,name):
        self.name=name
       

    def SetName(self,name):
        self.name=name

    def GetName(self):
        
        print "----------------------------- Tool And Function ---------------------------- "
        printhelp.showall()
        return ("{}Shell(".format(Fore.WHITE)+Fore.RED+'{}'.format(self.name)+"${}".format(Fore.YELLOW)+Fore.WHITE+")>")

   
