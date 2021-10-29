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

except:
    raise Exception


def getSize(bytes , default = "B"):
    bandLength = 1024
    for unit in ["" , "K" , "M" , "G" , "T" , "P"]:
        if bytes < bandLength:
            return f"{bytes:.2f}{unit}{default}"
        bytes /= bandLength


class Tools:
    def __init__(self):
        builtins.super(Tools , self).__init__()
        self.listDrives = []
        self.localIP = builtins.str(socket.gethostbyname(socket.gethostname()))
        self.publicIPLoader = requests.get("https://api.myip.com").content
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
        self.bootTime = datetime.datetime.fromtimestamp(psutil.boot_time())
        self.phCores = psutil.cpu_count(logical = False)
        self.totCores = psutil.cpu_count(logical = True)
        self.cpuFreq = psutil.cpu_freq()
        self.ramVir = psutil.virtual_memory()
        self.swapMemo = psutil.swap_memory()

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

    def ShowSystemName(self) -> builtins.str:
        builtins.print(self.systemName)

    def ShowSystemUptime(self) -> builtins.str:
        builtins.print(self.uptimeSystem)

    def ShowUserName(self) -> builtins.str:
        builtins.print(self.userName)

    def ShowSystemInformation(self) -> builtins.str:
        builtins.print(
            f"OS Name : {self.osName}\n" ,
            f"OS Type : {self.osType}\n" ,
            f"System Name : {self.systemName}\n" ,
            f"System Uptime : {self.uptimeSystem}\n" ,
            f"User : {self.userName}\n"
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

    def ShowDiskInfo(self):
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