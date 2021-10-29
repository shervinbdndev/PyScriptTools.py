try:
    import ctypes
    import getpass
    import sys
    import platform
    import requests
    import json
    import socket
    import builtins
    import GPUtil
    import psutil
    import datetime
    import getmac
    import string
    import colorama
    from consts import (API_USE , AF_INET , AF_PACKET)

except:
    raise Exception


def getSize(bytes , default = "B"):
    bandLength = 1024
    for unit in ["" , "K" , "M" , "G" , "T" , "P"]:
        if bytes < bandLength:
            return f"{bytes:.2f}{unit}{default}"
        bytes /= bandLength


class Tools:
    def __init__(self , *args , **kwargs):
        builtins.super(Tools , self).__init__(*args , **kwargs)
        self.listDrives = []
        self.localIP = builtins.str(socket.gethostbyname(socket.gethostname()))
        self.publicIPLoader = requests.get(API_USE).content
        self.loadedIP = json.loads(self.publicIPLoader)
        self.publicIP = builtins.str(self.loadedIP['ip'])
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
        self.bitMask = ctypes.windll.kernel32.GetLogicalDrives()
        self.gpuInfo = GPUtil.getGPUs()
        self.drivesInfo = psutil.disk_partitions()
        self.pythonVer = sys.version[0:6]
        self.cpuType = platform.uname().processor
        self.nodeName = platform.uname().node
        self.sysRelease = platform.uname().release
        self.sysVersion = platform.uname().version
        self.bootTime = datetime.datetime.fromtimestamp(psutil.boot_time())
        self.phCores = psutil.cpu_count(logical = False)
        self.totCores = psutil.cpu_count(logical = True)
        self.cpuFreq = psutil.cpu_freq()
        self.ramVir = psutil.virtual_memory()
        self.swapMemo = psutil.swap_memory()
        self.ipAddrs =  psutil.net_if_addrs()

    def ShowLocalIP(self) -> builtins.str:
        builtins.print(self.localIP)

    def ShowPublicIP(self) -> builtins.str:
        builtins.print(self.publicIP)

    def ShowMacAddress(self) -> builtins.str:
        builtins.print(getmac.get_mac_address(ip = socket.gethostbyname(socket.gethostname()) , network_request = True))

    def ShowOsName(self) -> builtins.str:
        builtins.print(self.osName)

    def ShowOsType(self) -> builtins.str:
        builtins.print(self.osType)

    def ShowNodeName(self) -> builtins.str:
        builtins.print(self.nodeName)

    def ShowOSRelease(self) -> builtins.str:
        builtins.print(self.sysRelease)

    def ShowOSVersion(self) -> builtins.str:
        builtins.print(self.sysVersion)

    def ShowSystemName(self) -> builtins.str:
        builtins.print(self.systemName)

    def ShowSystemUptime(self) -> builtins.str:
        builtins.print(self.uptimeSystem)

    def ShowUserName(self) -> builtins.str:
        builtins.print(self.userName)

    def ShowSystemInformation(self) -> builtins.str:
        builtins.print(
            f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.WHITE}{self.osName}\n" ,
            f"{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{self.osType}\n" ,
            f"{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{self.sysRelease}\n" ,
            f"{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{self.sysVersion}\n" ,
            f"{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{self.systemName or self.nodeName}\n" ,
            f"{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{self.uptimeSystem}\n" ,
            f"{colorama.ansi.Fore.GREEN}User : {colorama.ansi.Fore.WHITE}{self.userName}\n"
        )

    def ShowPythonVersion(self) -> builtins.str:
        builtins.print(self.pythonVer)

    def ShowDrives(self) -> builtins.str:
        for driver in string.ascii_uppercase:
            if self.bitMask & 1 :
                self.listDrives.append(driver)
            self.bitMask >>= 1
        print(self.listDrives)

    def ShowGPU_ID(self) -> builtins.str:
        for gpu in self.gpuInfo:
            gpuID = gpu.id
        print(gpuID)

    def ShowGPUName(self) -> builtins.str:
        for gpu in self.gpuInfo:
            gpuName = gpu.name
        print(gpuName)

    def ShowGPULoad(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuLoad = gpu.load * 100
            if gpuLoad > 50.0:
                newGpu = f"{colorama.ansi.Fore.RED}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                print(newGpu)
            else:
                newGpu = f"{colorama.ansi.Fore.GREEN}{gpu.load * 100}%{colorama.ansi.Fore.WHITE}"
                print(newGpu)

    def ShowGPUFreeMemory(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuFree = gpu.memoryFree
        builtins.print(gpuFree)

    def ShowGPUUsedMemory(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuUsed = f"{gpu.memoryUsed}MB"
        builtins.print(gpuUsed)

    def ShowGPUTotalMemory(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuTot = f"{gpu.memoryTotal}MB"
        builtins.print(gpuTot)

    def ShowGPUTemperature(self) -> builtins.float:
        for gpu in self.gpuInfo:
            gpuTemp = f"{gpu.temperature}℃"
        builtins.print(gpuTemp)

    def ShowGPU_UUID(self) -> builtins.str:
        for gpu in self.gpuInfo:
            gpuUUID = gpu.uuid
        builtins.print(gpuUUID)

    def ShowBootTime(self) -> builtins.str:
        builtins.print(self.bootTime)

    def ShowCPUType(self) -> builtins.str:
        builtins.print(self.cpuType)

    def ShowCPUPhysicalCores(self) -> builtins.int:
        builtins.print(self.phCores)

    def ShowCPUTotalCores(self) -> builtins.str:
        builtins.print(self.totCores)

    def ShowCPUMaxFrequency(self) -> builtins.float:
        builtins.print(f"{self.cpuFreq.max:.2f}Mhz")

    def ShowCPUMinFrequency(self) -> builtins.float:
        builtins.print(f"{self.cpuFreq.min:.2f}Mhz")

    def ShowCPUCurrentFrequency(self) -> builtins.float:
        builtins.print(f"{self.cpuFreq.current:.2f}Mhz")

    def ShowCPUTotalUsage(self) -> builtins.float:
        builtins.print(f"{psutil.cpu_percent()}%")

    def ShowCPUUsagePerCore(self) -> builtins.str:
        for core , percentage in builtins.enumerate(psutil.cpu_percent(percpu = True , interval = 1)):
            builtins.print(f"Core {core} : {percentage}%")

    def ShowTotalRAM(self) -> builtins.float:
        builtins.print(f"{getSize(self.ramVir.total)}")

    def ShowAvailableRAM(self) -> builtins.float:
        builtins.print(f"{getSize(self.ramVir.available)}")

    def ShowUsedRAM(self) -> builtins.float:
        builtins.print(f"{getSize(self.ramVir.used)}")

    def ShowRAMPercentage(self) -> builtins.float:
        builtins.print(f"{getSize(self.ramVir.percent)}%")

    def ShowTotalSwap(self) -> builtins.float:
        builtins.print(f"{getSize(self.swapMemo.total)}")

    def ShowFreeSwap(self) -> builtins.int:
        builtins.print(f"{getSize(self.swapMemo.free)}")

    def ShowUsedSwap(self) -> builtins.float:
        builtins.print(f"{getSize(self.swapMemo.used)}")

    def ShowSwapPercentage(self) -> builtins.float:
        builtins.print(f"{getSize(self.swapMemo.percent)}%")

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

    def ShowNetworkInfo(self) -> builtins.str:
        for interfaceName , interfaceAddresses in self.ipAddrs.items():
            for address in interfaceAddresses:
                builtins.print(f"{colorama.ansi.Fore.GREEN}=== Interface :{colorama.ansi.Fore.MAGENTA} {interfaceName} {colorama.ansi.Fore.GREEN}===")
                if builtins.str(address.family) == AF_INET:
                    builtins.print(f"{colorama.ansi.Fore.WHITE}IP Address : {address.address}")
                    builtins.print(f"Netmask : {address.netmask}")
                    builtins.print(f"Broadcast IP : {address.broadcast}")
                elif builtins.str(address.family) == AF_PACKET:
                    builtins.print(f"Mac Address : {address.address}")
                    builtins.print(f"Netmask : {address.netmask}")
                    builtins.print(f"Broadcast MAC : {address.broadcast}")