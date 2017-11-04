import sys
import main
import printhelp

#------------ variable ------------
cmd_check="help"
#----------------------------------

class CheckShell:
    def __init__(self,getcmd):
        try:
            self.Get_Cmd=getcmd
            if cmd_check==self.Get_Cmd:
                printhelp.showall()
            else:
                print "Bad Cmd"
                main.main()
            pass
        except IOError as identifier:
            print "No Value Found {}"+format(self.Get_Cmd)
            pass
        finally:
            pass
      
  