import wmi
import subprocess
import time
import ctypes, sys

def is_admin():
        try:
                return ctypes.windll.shell32.IsUserAnAdmin()
        except:
                return False

if is_admin(): 
        c = wmi.WMI()
        processes = c.Win32_Process()
        LeagueClient_cml = '\LeagueClient/LeagueClient.exe" --locale=th_TH --landing-token='
        for process in processes:
                if LeagueClient_cml in str(process.Commandline):
                        commandline = str(process.Commandline).replace('--locale=th_TH' , '--locale=en_US')
                        commandline = "@echo off\n" + commandline
                        #save bat
                        f = open("(English) League of Legends.bat", "w")
                        f.write(commandline)
                        f.close()
                        #terminate LoL
                        c.Win32_Process(ProcessId=process.ProcessId)[0].Terminate()
                        # time.sleep(1)
                        subprocess.call(['League of Legends(English).bat'])

else:  # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
