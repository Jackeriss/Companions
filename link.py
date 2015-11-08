# -*- coding: cp936 -*- # 
import os
import pythoncom
from shell import shell
from shell import shellcon 

def set_shortcut():
    startup_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_STARTUP))
    print startup_path
    shortcut = pythoncom.CoCreateInstance(shell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    shortcut.SetPath(os.getcwd()+"\Companions.exe")
    shortcut.SetWorkingDirectory(os.getcwd())
    shortcut.SetIconLocation(os.getcwd()+"\data\UI\images\Icon.ico",0)
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(startup_path+"\Companions.lnk",0)
    
if __name__ == "__main__":
    set_shortcut()
