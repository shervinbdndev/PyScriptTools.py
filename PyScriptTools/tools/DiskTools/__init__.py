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

    DiskTools
    =========
    version : 4.3.7\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import ctypes
    import platform
    import psutil
    import string
    import colorama
    
    from ...validators import *
    from ...exceptions import *

except:
    raise ModuleNotFoundError



class DiskTools:
    listDrives = []
    try:
        bitMask = ctypes.windll.kernel32.GetLogicalDrives()
    except:
        bitMask = str(NoneLinuxMethod.__doc__)
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
        if (type(show) is bool):
            if (platform.system()[0].upper() == 'W'):
                if (show is True):
                    for driver in string.ascii_uppercase:
                        if (cls.bitMask & 1) :
                            cls.listDrives.append(driver)
                        cls.bitMask >>= 1
                    return cls.listDrives
                elif (show is False):
                    return AdminPermissionRequestDenied.__doc__
                elif (show is None):
                    show = None
                    return NotNullableArgument.__doc__
                else:
                    return UnrecognizeableTypeArgument.__doc__
            else:
                return NoneLinuxMethod
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def ShowParentDiskTotalMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Total Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.parentDiskInfo.total / 1024 ** 3
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod    
    def ShowParentDiskUsedMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Used Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.parentDiskInfo.used / 1024 ** 3
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod    
    def ShowParentDiskFreeMemory(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Free Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.parentDiskInfo.free / 1024 ** 3
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod    
    def ShowParentDiskPercentage(cls , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Parent Disk Percentage_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{cls.parentDiskInfo.percent:.2f}"
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod    
    def ShowDiskInfo(cls , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            list: _Disk Information_
        """
        if (type(show) is bool):
            if (show is True):
                for partition in cls.drivesInfo:
                    print(f"{colorama.ansi.Fore.GREEN}=== Device : {partition.device} ===")
                    print(f"{colorama.ansi.Fore.WHITE}Mountpoint : {colorama.ansi.Fore.MAGENTA}{partition.mountpoint}{colorama.ansi.Fore.WHITE}")
                    print(f"File System Type : {partition.fstype}")
                    try:
                        partitionUsage = psutil.disk_usage(partition.mountpoint)
                    except PermissionError:
                        continue
                    print(f"Total Size : {LengthValidator.getSize(partitionUsage.total)}")
                    print(f"Used : {LengthValidator.getSize(partitionUsage.used)}")
                    print(f"Free : {LengthValidator.getSize(partitionUsage.free)}")
                    print(f"Percentage : {LengthValidator.getSize(partitionUsage.percent)}\n")
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__