import wmi
import subprocess
import time

c = wmi.WMI()
processes = c.Win32_Process()
LeagueClient_cml = '\LeagueClient/LeagueClient.exe" --locale=th_TH --landing-token='


for process in processes:
    if LeagueClient_cml in str(process.Commandline):
        print(process.ProcessId , process.Name)
        commandline = str(process.Commandline).replace('--locale=th_TH' , '--locale=en_US')
        commandline = "@echo off\n" + commandline
        print(commandline)
        #save bat
        f = open("(English) League of Legends.bat", "w")
        f.write(commandline)
        f.close()
        #terminate LoL
        c.Win32_Process(ProcessId=process.ProcessId)[0].Terminate()
        # time.sleep(1)
        subprocess.call(['League of Legends(English).bat'])