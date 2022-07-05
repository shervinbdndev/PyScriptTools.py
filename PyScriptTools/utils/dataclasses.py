"""

    MIT License

    Copyright (c) 2022 Shervin Badanara

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:\n

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.\n

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    Dataclasses
    ===========
    version : 4.3.13\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import os
    import sys
    import json
    import socket
    import ctypes
    import GPUtil
    import psutil
    import getpass
    import platform
    import datetime
    import requests
    from dataclasses import dataclass
    
    from ..exceptions import *
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run') from None



@dataclass
class CPUUtils:
    phCores = psutil.cpu_count(logical = False)
    totCores = psutil.cpu_count(logical = True)
    cpuFreq = psutil.cpu_freq()
    cpuType = platform.uname().processor
    
    

@dataclass
class DiskUtils:
    listDrives = []
    try:
        bitMask = ctypes.windll.kernel32.GetLogicalDrives()
    except:
        bitMask = str(NoneLinuxMethod.__doc__)
    drivesInfo = psutil.disk_partitions()
    parentDiskInfo = psutil.disk_usage(path='/')
    
    

@dataclass
class GPUUtils:
    gpuInfo = GPUtil.getGPUs()
    
    

@dataclass
class NetworkUtils:
    global __localIP
    global __publicIP
    __localIP = str(socket.gethostbyname(socket.gethostname()))
    __publicIPLoader = requests.get('https://api.myip.com').content
    __loadedIP = json.loads(__publicIPLoader)
    __publicIP = str(__loadedIP['ip'])
    ipAddrs =  psutil.net_if_addrs()

    @staticmethod
    def _localIP() -> str:
        return __localIP
    
    @staticmethod
    def _publicIP() -> str:
        return __publicIP
    
    
    

@dataclass
class RAMUtils:
    ramVir = psutil.virtual_memory()
    swapMemo = psutil.swap_memory()
    
    

@dataclass
class SystemUtils:
    osName = str(platform.system())
    osType = list(platform.architecture())[0]
    systemName = str(platform.node())
    try:
        getKernel32 = ctypes.windll.kernel32.GetTickCount64()
        getTime = int(str(getKernel32)[:-3])
        mins, sec = divmod(getTime, 60)
        hour, mins = divmod(mins, 60)
        days, hour = divmod(hour, 24)
        uptimeSystem = str("{0}:{1}:{2}:{3}").format(days , hour , mins , sec)
        if (not osType):
            osType = [''.join(map(str , str(i).split(sep=':')[1].strip())) for i in os.popen(cmd='systeminfo').readlines() if ('System Type' in i)]
    except:
        getKernel32 = str(NoneLinuxMethod.__doc__);\
        getTime = str(NoneLinuxMethod.__doc__);\
        mins=str(NoneLinuxMethod.__doc__);\
        sec=str(NoneLinuxMethod.__doc__);\
        hour=str(NoneLinuxMethod.__doc__);\
        days=str(NoneLinuxMethod.__doc__);\
        uptimeSystem=str(NoneLinuxMethod.__doc__)
        luts = ''.join(map(str , os.popen(cmd='uptime').readlines()))
        LuptimeSystem = luts.split(sep=' ')[1]
    finally:
        ...
    userName = getpass.getuser()
    listSysInfo = []
    pythonVer = sys.version[0:6]
    nodeName = platform.uname().node
    sysRelease = platform.uname().release
    sysVersion = platform.uname().version
    bootTime = datetime.datetime.fromtimestamp(psutil.boot_time())