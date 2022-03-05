try:
    import os
    import ctypes
    import getpass
    import sys
    import platform
    import requests
    import json
    import socket
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





class Constants:
    class Name:
        __packagename__ : str = str("PyScriptTools")
        
        @classmethod
        def name(cls , name : str = __packagename__) -> str:
            return name
    class Author:
        __author__ : str = str("Shervin Badanara")
        
        @classmethod
        def author(cls , author : str = __author__) -> str:
            return author
    class Version:
        __version__ : str = str("4.1.2")
        
        @classmethod
        def version(cls , version : str = __version__) -> str:
            return version





class NetworkTools:
    def __init__(self , *args , **kwargs):
        super(NetworkTools , self).__init__(*args , **kwargs)
        self.localIP = str(socket.gethostbyname(socket.gethostname()))
        self.publicIPLoader = requests.get('https://api.myip.com').content
        self.loadedIP = json.loads(self.publicIPLoader)
        self.publicIP = str(self.loadedIP['ip'])
        self.ipAddrs =  psutil.net_if_addrs()
    
    def ShowLocalIP(self) -> str:
        """_summary_

        Returns:
            str: Local IP Address
        """
        return self.localIP

    def ShowPublicIP(self) -> str:
        """_summary_

        Returns:
            str: Public IP Address
        """
        try:
            return self.publicIP
        except ConnectionError:
            pass

    def ShowMacAddress(self) -> str:
        """_summary_

        Returns:
            str: Mac Address
        """
        try:
            return getmac.get_mac_address(ip = socket.gethostbyname(socket.gethostname()) , network_request = True)
        except ConnectionError:
            pass

    def ShowNetworkInfo(self) -> str:
        """_summary_

        Returns:
            str: Some of Your Network Informations
        """
        for interfaceName , interfaceAddresses in self.ipAddrs.items():
            for address in interfaceAddresses:
                print(f"{colorama.ansi.Fore.GREEN}=== Interface :{colorama.ansi.Fore.MAGENTA} {interfaceName} {colorama.ansi.Fore.GREEN}===")
                if (str(address.family) == "AddressFamily.AF_INET"):
                    print(f"{colorama.ansi.Fore.WHITE}IP Address : {address.address}")
                    print(f"Netmask : {address.netmask}")
                    print(f"Broadcast IP : {address.broadcast}")
                elif (str(address.family) == "AddressFamily.AF_PACKET"):
                    print(f"Mac Address : {address.address}")
                    print(f"Netmask : {address.netmask}")
                    print(f"Broadcast MAC : {address.broadcast}")

    def ShowSavedNetworks(self) -> str:
        """_summary_

        Returns:
            str: Saved Networks On Your PC
        """
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
        """_summary_

        Returns:
            _type_: Test Connection To Internet
        """
        try:
            req = requests.get("https://google.com" , timeout = 5)
            return f"{colorama.ansi.Fore.GREEN}You're Connected To Internet"
        except (requests.ConnectionError , requests.Timeout) as E:
            return f"{colorama.ansi.Fore.RED}You're not Connected To Internet \n{E}"

    def StatusCodeChecker(self , link : str):
        """_summary_

        Args:
            link (str): Link to The Target Website or IP Address
            
        Returns:
            str: Status Codes Available in Link or IP Address
        """
        for code in range(200 , 599 + 1):
            if (requests.get(link).status_code == code):
                print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.GREEN}is Available")
            else:
                print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.RED}is not Available")





class CPUTools:
    def __init__(self , *args , **kwargs):
        super(CPUTools , self).__init__(*args , **kwargs)
        self.phCores = psutil.cpu_count(logical = False)
        self.totCores = psutil.cpu_count(logical = True)
        self.cpuFreq = psutil.cpu_freq()
        self.cpuType = platform.uname().processor

    def ShowCPUType(self) -> str:
        """_summary_

        Returns:
            str: CPU Type
        """
        return self.cpuType

    def ShowCPUPhysicalCores(self) -> int:
        """_summary_

        Returns:
            int: CPU Physical Cores
        """
        return self.phCores

    def ShowCPUTotalCores(self) -> str:
        """_summary_

        Returns:
            str: CPU Total Cores
        """
        return self.totCores

    def ShowCPUMaxFreq(self) -> float:
        """_summary_

        Returns:
            float: Maximum CPU Frequency
        """
        return f"{self.cpuFreq.max:.2f}Mhz"

    def ShowCPUMinFreq(self) -> float:
        """_summary_

        Returns:
            float: Minimum CPU Frequency
        """
        return f"{self.cpuFreq.min:.2f}Mhz"

    def ShowCPUCurrentFreq(self) -> float:
        """_summary_

        Returns:
            float: Current CPU Frequency
        """
        return f"{self.cpuFreq.current:.2f}Mhz"

    def ShowCPUTotalUsage(self) -> float:
        """_summary_

        Returns:
            float: Total CPU Usage
        """
        return f"{psutil.cpu_percent()}%"

    def ShowCPUUsagePerCore(self) -> str:
        """_summary_

        Returns:
            str: CPU Usage Per Cores
        """
        for core , percentage in enumerate(psutil.cpu_percent(percpu = True , interval = 1)):
            print(f"Core {core} : {percentage}%")





class GPUTools:
    def __init__(self , *args , **kwargs):
        super(GPUTools , self).__init__(*args , **kwargs)
        self.gpuInfo = GPUtil.getGPUs()

    def ShowGPU_ID(self) -> str:
        """_summary_

        Returns:
            str: GPU ID
        """
        for gpu in self.gpuInfo:
            gpuID = gpu.id
        return gpuID

    def ShowGPUName(self) -> str:
        """_summary_

        Returns:
            str: GPU Name
        """
        for gpu in self.gpuInfo:
            gpuName = gpu.name
        return gpuName

    def ShowGPULoad(self) -> float:
        """_summary_

        Returns:
            float: Average GPU Load Over a Period of Time
        """
        for gpu in self.gpuInfo:
            gpuLoad = gpu.load * 100
            if (gpuLoad > 50.0):
                newGpu = f"{colorama.ansi.Fore.RED}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                return newGpu
            else:
                newGpu = f"{colorama.ansi.Fore.GREEN}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                return newGpu

    def ShowGPUFreeMemory(self) -> float:
        """_summary_

        Returns:
            float: GPU Free Memory
        """
        for gpu in self.gpuInfo:
            gpuFree = gpu.memoryFree
        return gpuFree

    def ShowGPUUsedMemory(self) -> float:
        """_summary_

        Returns:
            float: GPU Used Memory
        """
        for gpu in self.gpuInfo:
            gpuUsed = f"{gpu.memoryUsed}MB"
        return gpuUsed

    def ShowGPUTotalMemory(self) -> float:
        """_summary_

        Returns:
            float: GPU Total Memory
        """
        for gpu in self.gpuInfo:
            gpuTot = f"{gpu.memoryTotal}MB"
        return gpuTot

    def ShowGPUTemperature(self) -> float:
        """_summary_

        Returns:
            float: GPU Temeprature
        """
        for gpu in self.gpuInfo:
            gpuTemp = f"{gpu.temperature}℃"
        return gpuTemp

    def ShowGPU_UUID(self) -> str:
        """_summary_

        Returns:
            str: GPU Unique UUID
        """
        for gpu in self.gpuInfo:
            gpuUUID = gpu.uuid
        return gpuUUID





class RAMTools:
    def __init__(self , *args , **kwargs):
        super(RAMTools , self).__init__(*args , **kwargs)
        self.ramVir = psutil.virtual_memory()
        self.swapMemo = psutil.swap_memory()
    
    def ShowTotalRAM(self) -> float:
        """_summary_

        Returns:
            float: Total RAM Space
        """
        return f"{getSize(self.ramVir.total)}"

    def ShowAvailableRAM(self) -> float:
        """_summary_

        Returns:
            float: Available RAM Space
        """
        return f"{getSize(self.ramVir.available)}"

    def ShowUsedRAM(self) -> float:
        """_summary_

        Returns:
            float: Total Space RAM Used
        """
        return f"{getSize(self.ramVir.used)}"

    def ShowRAMPercentage(self) -> float:
        """_summary_

        Returns:
            float: Total RAM Usage Percentage
        """
        return f"{getSize(self.ramVir.percent)}%"

    def ShowTotalSwap(self) -> float:
        """_summary_

        Returns:
            float: Swap Memory Total Space
        """
        return f"{getSize(self.swapMemo.total)}"

    def ShowFreeSwap(self) -> int:
        """_summary_

        Returns:
            int: Swap Memory Free Space
        """
        return f"{getSize(self.swapMemo.free)}"

    def ShowUsedSwap(self) -> float:
        """_summary_

        Returns:
            float: Swap Memory Used Space
        """
        return f"{getSize(self.swapMemo.used)}"

    def ShowSwapPercentage(self) -> float:
        """_summary_

        Returns:
            float: Swap Memory Usage Percentage
        """
        return f"{getSize(self.swapMemo.percent)}%"





class DiskTools:
    def __init__(self , *args , **kwargs):
        super(DiskTools ,  self).__init__(*args , **kwargs)
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

    def ShowDrives(self) -> list:
        """_summary_

        Returns:
            list: Available DiskDrives
        """
        for driver in string.ascii_uppercase:
            if (self.bitMask & 1) :
                self.listDrives.append(driver)
            self.bitMask >>= 1
        return self.listDrives

    def ShowDiskInfo(self) -> str:
        """_summary_

        Returns:
            str: Disk Information
        """
        for partition in self.drivesInfo:
            print(f"{colorama.ansi.Fore.GREEN}=== Device : {partition.device} ===")
            print(f"{colorama.ansi.Fore.WHITE}Mountpoint : {colorama.ansi.Fore.MAGENTA}{partition.mountpoint}{colorama.ansi.Fore.WHITE}")
            print(f"File System Type : {partition.fstype}")
            try:
                partitionUsage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            print(f"Total Size : {getSize(partitionUsage.total)}")
            print(f"Used : {getSize(partitionUsage.used)}")
            print(f"Free : {getSize(partitionUsage.free)}")
            print(f"Percentage : {getSize(partitionUsage.percent)}\n")





class SystemTools:
    def __init__(self , *args , **kwargs):
        super(SystemTools , self).__init__(*args , **kwargs)
        self.osName = str(platform.system())
        self.osType = list(platform.architecture())[0]
        self.systemName = str(platform.node())
        self.getKernel32 = ctypes.windll.kernel32.GetTickCount64()
        self.getTime = int(str(self.getKernel32)[:-3])
        self.mins, self.sec = divmod(self.getTime, 60)
        self.hour, self.mins = divmod(self.mins, 60)
        self.days, self.hour = divmod(self.hour, 24)
        self.uptimeSystem = str("{0}:{1}:{2}:{3}").format(self.days , self.hour , self.mins , self.sec)
        self.userName = getpass.getuser()
        self.listSysInfo = []
        self.pythonVer = sys.version[0:6]
        self.nodeName = platform.uname().node
        self.sysRelease = platform.uname().release
        self.sysVersion = platform.uname().version
        self.bootTime = datetime.datetime.fromtimestamp(psutil.boot_time())

    def ShowOsName(self) -> str:
        """_summary_

        Returns:
            str: Operating System Name
        """
        return self.osName

    def ShowOsType(self) -> str:
        """_summary_

        Returns:
            str: Operating System Type
        """
        return self.osType

    def ShowNodeName(self) -> str:
        """_summary_

        Returns:
            str: System Name
        """
        return self.nodeName

    def ShowOSRelease(self) -> str:
        """_summary_

        Returns:
            str: Operating System Release
        """
        return self.sysRelease

    def ShowOSVersion(self) -> str:
        """_summary_

        Returns:
            str: Operating System Version
        """
        return self.sysVersion

    def ShowSystemName(self) -> str:
        """_summary_

        Returns:
            str: System Name
        """
        return self.systemName

    def ShowSystemUptime(self) -> str:
        """_summary_

        Returns:
            str: System Uptime
        """
        return self.uptimeSystem

    def ShowUserName(self) -> str:
        """_summary_

        Returns:
            str: System Username
        """
        return self.userName

    def ShowSystemInformation(self) -> str:
        """_summary_

        Returns:
            str: System Information Based On Windows Operating System
        """
        if (platform.system() == "Windows"):
            print(
                f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.BLUE}{self.osName}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{self.osType}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{self.sysRelease}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{self.sysVersion}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{self.systemName or self.nodeName}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{self.uptimeSystem}" ,
                f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{self.userName}"
            )
        elif (platform.system() == "Linux"):
            print(
                f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.YELLOW}{self.osName}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{self.osType}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{self.sysRelease}" ,
                f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{self.sysVersion}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{self.systemName or self.nodeName}" ,
                f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{self.uptimeSystem}" ,
                f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{self.userName}"
            )

    def ShowPythonVersion(self) -> str:
        """_summary_

        Returns:
            str: Python Version
        """
        return self.pythonVer

    def ShowBootTime(self) -> str:
        """_summary_

        Returns:
            str: System Boot Time
        """
        return self.bootTime






class OtherTools:
    def __init__(self , *args , **kwargs):
        super(OtherTools , self).__init__(*args , **kwargs)
        self.pathValidation = bool()

    def ConvertToAscii(self , text:str , colors:list , align:str , font:str) -> str:
        """_summary_

        Args:
            text (str): Your Text Here
            colors (list): ['color1' , 'color2']
            align (str): ("left" , "center" , "right")
            font (str): ("console" , "block" , "simpleBlock" , "simple" , "3d" , "simple3d" , "chrome" , "huge" , "grid" , "pallet" , "shade" , "slick" , "tiny")

        Returns:
            str: Customized Ascii Art
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

    def IsPath(self , pathaddr : str) -> str:
        """_summary_

        Args:
            pathaddr (str): Raw System Address

        Returns:
            str: If the Path Exists Returns True , else Returns False
        """
        if (os.path.exists(r"{0}".format(pathaddr)) and (platform.system()[0].upper() in ["W" , "L" , "J"])):
            return f"{colorama.ansi.Fore.GREEN}The Path Exists\nThe Code Output is {colorama.ansi.Fore.BLUE}{True}"
        else:
            return f"{colorama.ansi.Fore.RED}The Path Doesn't Exist\nThe Code Output is {colorama.ansi.Fore.BLUE}{False}"
        
    def GetAbsOutput(self , string : str) -> str:
        """_summary_

        Args:
            string (str): Math Expressions or Python Commands

        Returns:
            str: Math Expressions or Python Commands
        """
        return eval(string)





class PrintHeaderClass:
    def __init__(self , *args , **kwargs) -> bytearray:
        super(PrintHeaderClass , self).__init__(*args , **kwargs)
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