#!/bin/bash

# --- imports ------
import os
import shell
import colors
import time
import sys
import checkshell
#-------------------
#------variables --------
get_uname=""
store_shellname=""
show_shellname=""
get_input_from_user=""
shell_checker=""
#-------------------

def main():
    
    try:
       get_uname=raw_input("{}Enter the Shell user Name :".format(colors.red))
       store_shellname=shell.Shell(get_uname)
       show_shellname=store_shellname.GetName()
       get_input_from_user=raw_input(show_shellname)
       shell_checker=checkshell.CheckShell(get_input_from_user)
       pass
    except IOError as identifier:
       print ("{}shell faild{}".format(colors.red,colors.reset))
       pass
    else:
       pass
    finally:
       pass
    time.sleep(30)

if __name__ =='__main__':
    main()
