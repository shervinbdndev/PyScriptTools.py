try:
    import os
    import ctypes
    import getpass
    import sys
    import platform
    import requests
    import json
    import socket
    import builtins
    import time
    import GPUtil
    import psutil
    import datetime
    import getmac
    import string
    import colorama
    import cfonts
    import random

except:
    raise ModuleNotFoundError


def getSize(bytes , default = "B"):
    bandLength = 1024
    for unit in ["" , "K" , "M" , "G" , "T" , "P"]:
        if (bytes < bandLength):
            return f"{bytes:.2f}{unit}{default}"
        bytes /= bandLength





class NetworkTools:
    def __init__(self , *args , **kwargs):
        builtins.super(NetworkTools , self).__init__(*args , **kwargs)
        self.localIP = builtins.str(socket.gethostbyname(socket.gethostname()))
        self.publicIPLoader = requests.get('https://api.myip.com').content
        self.loadedIP = json.loads(self.publicIPLoader)
        self.publicIP = builtins.str(self.loadedIP['ip'])
        self.ipAddrs =  psutil.net_if_addrs()
    
    def ShowLocalIP(self) -> builtins.str:
        return self.localIP

    def ShowPublicIP(self) -> builtins.str:
        try:
            return self.publicIP
        except ConnectionError:
            pass

    def ShowMacAddress(self) -> builtins.str:
        try:
            return getmac.get_mac_address(ip = socket.gethostbyname(socket.gethostname()) , network_request = True)
        except ConnectionError:
            pass

    def ShowNetworkInfo(self) -> builtins.str:
        for interfaceName , interfaceAddresses in self.ipAddrs.items():
            for address in interfaceAddresses:
                builtins.print(f"{colorama.ansi.Fore.GREEN}=== Interface :{colorama.ansi.Fore.MAGENTA} {interfaceName} {colorama.ansi.Fore.GREEN}===")
                if (builtins.str(address.family) == "AddressFamily.AF_INET"):
                    builtins.print(f"{colorama.ansi.Fore.WHITE}IP Address : {address.address}")
                    builtins.print(f"Netmask : {address.netmask}")
                    builtins.print(f"Broadcast IP : {address.broadcast}")
                elif (builtins.str(address.family) == "AddressFamily.AF_PACKET"):
                    builtins.print(f"Mac Address : {address.address}")
                    builtins.print(f"Netmask : {address.netmask}")
                    builtins.print(f"Broadcast MAC : {address.broadcast}")

    def ShowSavedNetworks(self) -> builtins.str:
        if (platform.system()[0].upper() == "W"):
            for i in os.popen("netsh wlan show profiles"):
                if ("All User Profile" in i):
                    i = str(i).split(":")
                    i = f"{colorama.ansi.Fore.GREEN}Network Name : {colorama.ansi.Fore.MAGENTA} {i[1].strip()}"
                    print(i)
                    continue
        else:
            return f"{colorama.ansi.Fore.YELLOW}This Method Only Works on Windows OS !!!"

    def TestConnection(self):
        try:
            req = requests.get("https://google.com" , timeout = 5)
            return f"{colorama.ansi.Fore.GREEN}You're Connected To Internet"
        except (requests.ConnectionError , requests.Timeout) as E:
            return f"{colorama.ansi.Fore.RED}You're not Connected To Internet \n{E}"

    def StatusCodeChecker(self , link : str):
        for code in range(200 , 599 + 1):
            if (requests.get(link).status_code == code):
                print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.GREEN}is Available")
            else:
                print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.RED}is not Available")





class CPUTools:
    def __init__(self , *args , **kwargs):
        builtins.super(CPUTools , self).__init__(*args , **kwargs)
        self.phCores = psutil.cpu_count(logical = False)
        self.totCores = psutil.cpu_count(logical = True)
        self.cpuFreq = psutil.cpu_freq()
        self.cpuType = platform.uname().processor

    def ShowCPUType(self) -> builtins.str:
        return self.cpuType

    def ShowCPUPhysicalCores(self) -> builtins.int:
        return self.phCores

    def ShowCPUTotalCores(self) -> builtins.str:
        return self.totCores

    def ShowCPUMaxFrequency(self) -> builtins.float:
        return f"{self.cpuFreq.max:.2f}Mhz"

    def ShowCPUMinFrequency(self) -> builtins.float:
        return f"{self.cpuFreq.min:.2f}Mhz"

    def ShowCPUCurrentFrequency(self) -> builtins.float:
        return f"{self.cpuFreq.current:.2f}Mhz"

    def ShowCPUTotalUsage(self) -> builtins.float:
        return f"{psutil.cpu_percent()}%"

    def ShowCPUUsagePerCore(self) -> builtins.str:
        for core , percentage in builtins.enumerate(psutil.cpu_percent(percpu = True , interval = 1)):
            return f"Core {core} : {percentage}%"





class GPUTools:
    def __init__(self , *args , **kwargs):
        builtins.super(GPUTools , self).__init__(*args , **kwargs)
        self.gpuInfo = GPUtil.getGPUs()

    def ShowGPU_ID(self) -> builtins.str:
        for gpu in self.gpuInfo:
            gpuID = gpu.id
        return gpuID

    def ShowGPUName(self) -> builtins.str:
        for gpu in self.gpuInfo:
            gpuName = gpu.name
        return gpuName

    def ShowGPULoad(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuLoad = gpu.load * 100
            if (gpuLoad > 50.0):
                newGpu = f"{colorama.ansi.Fore.RED}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                return newGpu
            else:
                newGpu = f"{colorama.ansi.Fore.GREEN}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                return newGpu

    def ShowGPUFreeMemory(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuFree = gpu.memoryFree
        return gpuFree

    def ShowGPUUsedMemory(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuUsed = f"{gpu.memoryUsed}MB"
        return gpuUsed

    def ShowGPUTotalMemory(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuTot = f"{gpu.memoryTotal}MB"
        return gpuTot

    def ShowGPUTemperature(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuTemp = f"{gpu.temperature}℃"
        return gpuTemp

    def ShowGPU_UUID(self) -> builtins.str:
        for gpu in self.gpuInfo:
            gpuUUID = gpu.uuid
        return gpuUUID





class RAMTools:
    def __init__(self , *args , **kwargs):
        builtins.super(RAMTools , self).__init__(*args , **kwargs)
        self.ramVir = psutil.virtual_memory()
        self.swapMemo = psutil.swap_memory()
    
    def ShowTotalRAM(self) -> builtins.float:
        return f"{getSize(self.ramVir.total)}"

    def ShowAvailableRAM(self) -> builtins.float:
        return f"{getSize(self.ramVir.available)}"

    def ShowUsedRAM(self) -> builtins.float:
        return f"{getSize(self.ramVir.used)}"

    def ShowRAMPercentage(self) -> builtins.float:
        return f"{getSize(self.ramVir.percent)}%"

    def ShowTotalSwap(self) -> builtins.float:
        return f"{getSize(self.swapMemo.total)}"

    def ShowFreeSwap(self) -> builtins.int:
        return f"{getSize(self.swapMemo.free)}"

    def ShowUsedSwap(self) -> builtins.float:
        return f"{getSize(self.swapMemo.used)}"

    def ShowSwapPercentage(self) -> builtins.float:
        return f"{getSize(self.swapMemo.percent)}%"





class DiskTools:
    def __init__(self , *args , **kwargs):
        builtins.super(DiskTools ,  self).__init__(*args , **kwargs)
        self.listDrives = []
        self.bitMask = ctypes.windll.kernel32.GetLogicalDrives()
        self.drivesInfo = psutil.disk_partitions()
        self.driveTypes = [
            'DRIVE_UNKNOWN',
            'DRIVE_NO_ROOT_DIR',
            'DRIVE_REMOVABLE',
            'DRIVE_FIXED',
            'DRIVE_REMOTE',
            'DRIVE_CDROM',
            'DRIVE_RAMDISK'
        ]

    def ShowDrives(self) -> builtins.list:
        for driver in string.ascii_uppercase:
            if (self.bitMask & 1) :
                self.listDrives.append(driver)
            self.bitMask >>= 1
        return self.listDrives

    def ShowDiskInfo(self) -> builtins.str:
        for partition in self.drivesInfo:
            builtins.print(f"{colorama.ansi.Fore.GREEN}=== Device : {partition.device} ===")
            builtins.print(f"{colorama.ansi.Fore.WHITE}Mountpoint : {colorama.ansi.Fore.MAGENTA}{partition.mountpoint}{colorama.ansi.Fore.WHITE}")
            builtins.print(f"File System Type : {partition.fstype}")
            try:
                partitionUsage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            builtins.print(f"Total Size : {getSize(partitionUsage.total)}")
            builtins.print(f"Used : {getSize(partitionUsage.used)}")
            builtins.print(f"Free : {getSize(partitionUsage.free)}")
            builtins.print(f"Percentage : {getSize(partitionUsage.percent)}\n")





class SystemTools:
    def __init__(self , *args , **kwargs):
        builtins.super(SystemTools , self).__init__(*args , **kwargs)
        self.osName = builtins.str(platform.system())
        self.osType = builtins.list(platform.architecture())[0]
        self.systemName = builtins.str(platform.node())
        self.getKernel32 = ctypes.windll.kernel32.GetTickCount64()
        self.getTime = builtins.int(builtins.str(self.getKernel32)[:-3])
        self.mins, self.sec = builtins.divmod(self.getTime, 60)
        self.hour, self.mins = builtins.divmod(self.mins, 60)
        self.days, self.hour = builtins.divmod(self.hour, 24)
        self.uptimeSystem = builtins.str("{0}:{1}:{2}:{3}").format(self.days , self.hour , self.mins , self.sec)
        self.userName = getpass.getuser()
        self.listSysInfo = []
        self.pythonVer = sys.version[0:6]
        self.nodeName = platform.uname().node
        self.sysRelease = platform.uname().release
        self.sysVersion = platform.uname().version
        self.bootTime = datetime.datetime.fromtimestamp(psutil.boot_time())

    def ShowOsName(self) -> builtins.str:
        return self.osName

    def ShowOsType(self) -> builtins.str:
        return self.osType

    def ShowNodeName(self) -> builtins.str:
        return self.nodeName

    def ShowOSRelease(self) -> builtins.str:
        return self.sysRelease

    def ShowOSVersion(self) -> builtins.str:
        return self.sysVersion

    def ShowSystemName(self) -> builtins.str:
        return self.systemName

    def ShowSystemUptime(self) -> builtins.str:
        return self.uptimeSystem

    def ShowUserName(self) -> builtins.str:
        return self.userName

    def ShowSystemInformation(self) -> builtins.str:
        if (platform.system() == "Windows"):
            builtins.print(
                f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.BLUE}{self.osName}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{self.osType}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{self.sysRelease}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{self.sysVersion}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{self.systemName or self.nodeName}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{self.uptimeSystem}" ,
                f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{self.userName}"
            )
        elif (platform.system() == "Linux"):
            builtins.print(
                f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.YELLOW}{self.osName}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{self.osType}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{self.sysRelease}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{self.sysVersion}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{self.systemName or self.nodeName}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{self.uptimeSystem}" ,
                f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{self.userName}"
            )

    def ShowPythonVersion(self) -> builtins.str:
        return self.pythonVer

    def ShowBootTime(self) -> builtins.str:
        return self.bootTime






class OtherTools:
    def __init__(self , *args , **kwargs):
        builtins.super(OtherTools , self).__init__(*args , **kwargs)
        self.pathValidation = bool()

    def ConvertToAscii(self , text:str , colors:list , align:str , font:str) -> builtins.str:
        """
            Function Usage :
                text = text
                alignment = ("left" , "center" , "right")
                fontType =  "console"
                            "block"
                            "simpleBlock"
                            "simple"
                            "3d"
                            "simple3d"
                            "chrome"
                            "huge"
                            "grid"
                            "pallet"
                            "shade"
                            "slick"
                            "tiny"
                ConverToAscii(text , [color1 , color2] , alignment , fontType)
        """
        self.text = text
        self.colors = colors
        self.align = align
        self.font = font
        self.configuration = cfonts.render(
            text = self.text ,
            colors = self.colors ,
            align = self.align ,
            font = self.font
        )
        return self.configuration


    def IsPath(self , pathaddr : str) -> builtins.str:
        if (os.path.exists(r"{0}".format(pathaddr)) and (platform.system()[0].upper() in ["W" , "L" , "J"])):
            return f"{colorama.ansi.Fore.GREEN}The Path Exists\nThe Code Output is {colorama.ansi.Fore.BLUE}{True}"
        else:
            return f"{colorama.ansi.Fore.RED}The Path Doesn't Exist\nThe Code Output is {colorama.ansi.Fore.BLUE}{False}"





class PrintHeaderClass:
    def __init__(self , *args , **kwargs) -> builtins.bytearray:
        builtins.super(PrintHeaderClass , self).__init__(*args , **kwargs)
        self.colorList = [
            "black" , "red" , "green" , "yellow" ,
            "blue" , "magenta" , "cyan" , "white" ,
            "gray"
        ]
        self.headerShow = cfonts.render(
            text = "PyScriptTools" ,
            colors = [
                random.choice(self.colorList) ,
                random.choice(self.colorList)
            ] ,
            align = "center" ,
            font = "slick"
        )

    def HeaderPrint(self):
        return self.headerShow



if (__name__ == "__main__" and platform.system()[0].upper() in ["W" , "L" , "J"]):
    print(PrintHeaderClass().HeaderPrint())