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
    from typing import (Tuple , Any)
    from Exceptions.Exceptions import (
        NoneTypeArgumentInt ,
        NoneTypeArgumentString , 
        AdminPermissionRequestDenied , 
        UnrecognizeableTypeArgument ,
        UndefinedOperatingSystem
    )

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
    localIP = str(socket.gethostbyname(socket.gethostname()))
    publicIPLoader = requests.get('https://api.myip.com').content
    loadedIP = json.loads(publicIPLoader)
    publicIP = str(loadedIP['ip'])
    ipAddrs =  psutil.net_if_addrs()
    
    @classmethod
    def ShowLocalIP(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Local IP_
        """
        if (show is True):
            return cls.localIP
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowPublicIP(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Public IP_
        """
        if (show is True):
            try:
                return cls.publicIP
            except ConnectionError:
                pass
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowMacAddress(cls , show : bool = False , network_request : bool = True) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            network_request (bool): _Use Internet To get MacAddress(better to use True)_. Defaults to True.

        Returns:
            str: _MAC Address_
        """
        if (show is True):
            try:
                return getmac.get_mac_address(ip = socket.gethostbyname(socket.gethostname()) , network_request = network_request)
            except ConnectionError:
                pass
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowNetworkInfo(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Shows Some of Your Network Information_
        """
        if (show is True):
            for interfaceName , interfaceAddresses in cls.ipAddrs.items():
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
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowSavedNetworks(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Shows Saved Networks_
        """
        if (show is True):
            if (platform.system()[0].upper() == "W"):
                for i in os.popen("netsh wlan show profiles"):
                    if ("All User Profile" in i):
                        i = str(i).split(":")
                        i = f"{colorama.ansi.Fore.GREEN}Network Name : {colorama.ansi.Fore.MAGENTA} {i[1].strip()}"
                        print(i)
                        continue
            else:
                return f"{colorama.ansi.Fore.YELLOW}This Method Only Works on Windows OS !!!"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def TestConnection(cls , show : bool = False , timeout : int = 5):
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            timeout (int): _Sets The Timeout For Each Request_. Defaults to 5.

        Returns:
            _str_: _Tests Internet Connection_
        """
        if (show is True):
            if (type(timeout) is int):
                try:
                    req = requests.get("https://www.google.com" , timeout = timeout)
                    return f"{colorama.ansi.Fore.GREEN}You're Connected To Internet"
                except (requests.ConnectionError , requests.Timeout) as E:
                    return f"{colorama.ansi.Fore.RED}You're not Connected To Internet \n{E}"
            else:
                return NoneTypeArgumentInt
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def StatusCodeChecker(cls , show : bool = False , link : str = ''):
        """_summary_

        Args:
            _show_ (bool): _Shows The Output_. Defaults to False.
            _link_ (str): Link to The Target Website or IP Address.

        Returns:
            _str_: Status Codes Available in Link or IP Address
        """
        if (show is True):
            if (type(link) is str):
                for code in range(200 , 599 + 1):
                    if (requests.get(link).status_code == code):
                        print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.GREEN}is Available")
                    else:
                        print(f"{colorama.ansi.Fore.MAGENTA}Status : {colorama.ansi.Fore.BLUE}{code} {colorama.ansi.Fore.RED}is not Available")
            else:
                return NoneTypeArgumentString
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument






class CPUTools:
    phCores = psutil.cpu_count(logical = False)
    totCores = psutil.cpu_count(logical = True)
    cpuFreq = psutil.cpu_freq()
    cpuType = platform.uname().processor

    @classmethod
    def ShowCPUType(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _CPU Type_
        """
        if (show is True):
            return cls.cpuType
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowCPUPhysicalCores(cls , show : bool = False) -> int:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            int: _CPU Physical Cores_
        """
        if (show is True):
            return cls.phCores
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowCPUTotalCores(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _CPU Total Cores_
        """
        if (show is True):
            return cls.totCores
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowCPUMaxFreq(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Maximum Frequency_
        """
        if (show is True):
            return f"{cls.cpuFreq.max:.2f}Mhz"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument
    
    @classmethod
    def ShowCPUMinFreq(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Minimum Frequency_
        """
        if (show is True):
            return f"{cls.cpuFreq.min:.2f}Mhz"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowCPUCurrentFreq(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Current Frequency_
        """
        if (show is True):
            return f"{cls.cpuFreq.current:.2f}Mhz"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowCPUTotalUsage(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Total Frequency_
        """
        if (show is True):
            return f"{psutil.cpu_percent()}%"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowCPUUsagePerCore(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Usage Per Cores_
        """
        if (show is True):
            for core , percentage in enumerate(psutil.cpu_percent(percpu = True , interval = 1)):
                print(f"Core {core} : {percentage}%")
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument






class GPUTools:
    gpuInfo = GPUtil.getGPUs()

    @classmethod
    def ShowGPU_ID(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _GPU ID_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuID = gpu.id
            return gpuID
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowGPUName(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _GPU Name_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuName = gpu.name
            return gpuName
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowGPULoad(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Load_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuLoad = gpu.load * 100
                if (gpuLoad > 50.0):
                    newGpu = f"{colorama.ansi.Fore.RED}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                    return newGpu
                else:
                    newGpu = f"{colorama.ansi.Fore.GREEN}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                    return newGpu
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowGPUFreeMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Free Memory_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuFree = gpu.memoryFree
            return gpuFree
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowGPUUsedMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Used Memory_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuUsed = f"{gpu.memoryUsed}MB"
            return gpuUsed
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowGPUTotalMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Total Memory_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuTot = f"{gpu.memoryTotal}MB"
            return gpuTot
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowGPUTemperature(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Temperature_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuTemp = f"{gpu.temperature}℃"
            return gpuTemp
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowGPU_UUID(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _GPU UUID_
        """
        if (show is True):
            for gpu in cls.gpuInfo:
                gpuUUID = gpu.uuid
            return gpuUUID
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument





class RAMTools:
    ramVir = psutil.virtual_memory()
    swapMemo = psutil.swap_memory()
    
    @classmethod
    def ShowTotalRAM(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Total RAM Memory_
        """
        if (show is True):
            return f"{getSize(cls.ramVir.total)}"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowAvailableRAM(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Available RAM Memory_
        """
        if (show is True):
            return f"{getSize(cls.ramVir.available)}"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowUsedRAM(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Used RAM Memory_
        """
        if (show is True):
            return f"{getSize(cls.ramVir.used)}"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowRAMPercentage(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _RAM Percentage_
        """
        if (show is True):
            return f"{getSize(cls.ramVir.percent)}%"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowTotalSwap(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Total Swap Memory_
        """
        if (show is True):
            return f"{getSize(cls.swapMemo.total)}"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowFreeSwap(cls , show : bool = False) -> int:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            int: _Free Swap Memory_
        """
        if (show is True):
            return f"{getSize(cls.swapMemo.free)}"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowUsedSwap(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Used Swap Memory_
        """
        if (show is True):
            return f"{getSize(cls.swapMemo.used)}"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowSwapPercentage(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Swap Percentage_
        """
        if (show is True):
            return f"{getSize(cls.swapMemo.percent)}%"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument






class DiskTools:
    listDrives = []
    bitMask = ctypes.windll.kernel32.GetLogicalDrives()
    drivesInfo = psutil.disk_partitions()
    parentDiskInfo = psutil.disk_usage(path='/')

    @classmethod
    def ShowDrives(cls , show : bool = False) -> list:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _List Of All Available Drives_
        """
        if (show is True):
            for driver in string.ascii_uppercase:
                if (cls.bitMask & 1) :
                    cls.listDrives.append(driver)
                cls.bitMask >>= 1
            return cls.listDrives
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowParentDiskTotalMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Total Memory_
        """
        if (show is True):
            return cls.parentDiskInfo.total / 1024 ** 3
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod    
    def ShowParentDiskUsedMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Used Memory_
        """
        if (show is True):
            return cls.parentDiskInfo.used / 1024 ** 3
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod    
    def ShowParentDiskFreeMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Free Memory_
        """
        if (show is True):
            return cls.parentDiskInfo.free / 1024 ** 3
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod    
    def ShowParentDiskPercentage(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Percentage_
        """
        if (show is True):
            return f"{cls.parentDiskInfo.percent:.2f}"
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod    
    def ShowDiskInfo(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Disk Information_
        """
        if (show is True):
            for partition in cls.drivesInfo:
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
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument






class SystemTools:
    osName = str(platform.system())
    osType = list(platform.architecture())[0]
    systemName = str(platform.node())
    getKernel32 = ctypes.windll.kernel32.GetTickCount64()
    getTime = int(str(getKernel32)[:-3])
    mins, sec = divmod(getTime, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    uptimeSystem = str("{0}:{1}:{2}:{3}").format(days , hour , mins , sec)
    userName = getpass.getuser()
    listSysInfo = []
    pythonVer = sys.version[0:6]
    nodeName = platform.uname().node
    sysRelease = platform.uname().release
    sysVersion = platform.uname().version
    bootTime = datetime.datetime.fromtimestamp(psutil.boot_time())

    @classmethod
    def ShowOsName(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Name_
        """
        if (show is True):
            return cls.osName
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowOsType(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Type
        """
        if (show is True):
            return cls.osType
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowNodeName(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Node Name or System's Name_
        """
        if (show is True):
            return cls.nodeName
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowOSRelease(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Release_
        """
        if (show is True):
            return cls.sysRelease
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowOSVersion(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Version_
        """
        if (show is True):
            return cls.sysVersion
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowSystemName(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _System's Name_
        """
        if (show is True):
            return cls.systemName
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowSystemUptime(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _System's Uptime_
        """
        if (show is True):
            return cls.uptimeSystem
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowUserName(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Active Logined Username_
        """
        if (show is True):
            return cls.userName
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowSystemInformation(cls , show : bool = False , os_name : str = "Windows") -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            os_name (str): _Choose The Operating System_. Defaults to "Windows".

        Returns:
            str: _Shows System Information Based On Your Operating System_
        """
        if (show is True):
            if (type(os_name) is str):
                if (os_name == "Windows" or os_name.startswith(("W" , "w"))):
                    print(
                        f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.BLUE}{cls.osName}" ,
                        f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{cls.osType}" ,
                        f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{cls.sysRelease}" ,
                        f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{cls.sysVersion}" ,
                        f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{cls.systemName or cls.nodeName}" ,
                        f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{cls.uptimeSystem}" ,
                        f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{cls.userName}"
                    )
                elif (os_name == "Linux" or os_name.startswith(("L" , "l"))):
                    print(
                        f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.YELLOW}{cls.osName}" ,
                        f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{cls.osType}" ,
                        f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{cls.sysRelease}" ,
                        f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{cls.sysVersion}" ,
                        f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{cls.systemName or cls.nodeName}" ,
                        f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{cls.uptimeSystem}" ,
                        f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{cls.userName}"
                    )
                else:
                    return UndefinedOperatingSystem
            else:
                return NoneTypeArgumentString
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            UnrecognizeableTypeArgument

    @classmethod
    def ShowPythonVersion(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Python Version_
        """
        if (show is True):
            return cls.pythonVer
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    @classmethod
    def ShowBootTime(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Boot Time_
        """
        if (show is True):
            return cls.bootTime
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument






class OtherTools:
    pathValidation = bool()

    def ConvertToAscii(cls , show : bool = False , text : Any = '' , colors : list = [] , align : Tuple[str] = "" , font : str = "") -> str:
        """_summary_

        Args:
            show (bool, optional): _Show The Output_. Defaults to False.
            text (str, optional): _Your Text Here_. Defaults to ''.
            colors (list, optional): _['color1' , 'color2']_. Defaults to [].
            align (Tuple, optional): _("left" , "center" , "right") Use One_. Defaults to "".
            font (str, optional): _("console" , "block" , "simpleBlock" , "simple" , "3d" , "simple3d" , "chrome" , "huge" , "grid" , "pallet" , "shade" , "slick" , "tiny") Use One_. Defaults to "".

        Returns:
            str: _Customized Ascii Art_
        """
        if (show is True):
            if (type(text) is Any):
                cls.text = text
                cls.colors = colors
                cls.align = align
                cls.font = font
                cls.configuration = cfonts.render(
                    text = cls.text ,
                    colors = cls.colors ,
                    align = cls.align ,
                    font = cls.font
                )
                return cls.configuration
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument

    def IsPath(cls , show : bool = False , pathaddr : str = '') -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            pathaddr (str): _System's Local Address_. Defaults to ''.

        Returns:
            str: _Validates The Path You've Entered_
        """
        if (show is True):
            if (type(pathaddr) is str):
                if (os.path.exists(r"{0}".format(pathaddr)) and (platform.system()[0].upper() in ["W" , "L" , "J"])):
                    return f"{colorama.ansi.Fore.GREEN}The Path Exists\nThe Code Output is {colorama.ansi.Fore.BLUE}{True}"
                else:
                    return f"{colorama.ansi.Fore.RED}The Path Doesn't Exist\nThe Code Output is {colorama.ansi.Fore.BLUE}{False}"
            else:
                return NoneTypeArgumentString
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument
        
    def GetAbsOutput(cls , show : bool = False , string : str = '') -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            string (str): _Your Python Command or Expression_. Defaults to ''.

        Returns:
            str: _Runs The Text as a Python Command or Expression_
        """
        if (show is True):
            if (type(string) is str):
                return eval(string)
            else:
                return NoneTypeArgumentString
        elif (show is False):
            return AdminPermissionRequestDenied
        else:
            return UnrecognizeableTypeArgument





class PrintHeaderClass:
    def __init__(self , *args , **kwargs) -> str:
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