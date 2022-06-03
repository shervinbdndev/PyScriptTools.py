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

    CPUTools
    ========
    version : 4.3.10\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""

try:
    import psutil
    import platform
    from typing import Type
    from typing_extensions import Self
    
    from ...exceptions import *

except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run') from None


class CPUTools:
    phCores = psutil.cpu_count(logical = False)
    totCores = psutil.cpu_count(logical = True)
    cpuFreq = psutil.cpu_freq()
    cpuType = platform.uname().processor

    @classmethod
    def ShowCPUType(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _CPU Type_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.cpuType
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
    def ShowCPUPhysicalCores(cls : Type[Self] , show : bool = False) -> int:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            int: _CPU Physical Cores_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.phCores
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
    def ShowCPUTotalCores(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _CPU Total Cores_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.totCores
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
    def ShowCPUMaxFreq(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Maximum Frequency_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{cls.cpuFreq.max:.2f}Mhz"
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
    def ShowCPUMinFreq(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Minimum Frequency_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{cls.cpuFreq.min:.2f}Mhz"
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
    def ShowCPUCurrentFreq(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Current Frequency_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{cls.cpuFreq.current:.2f}Mhz"
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
    def ShowCPUTotalUsage(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Total Frequency_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{psutil.cpu_percent()}%"
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
    def ShowCPUUsagePerCore(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _CPU Usage Per Cores_
        """
        if (type(show) is bool):
            if (show is True):
                for core , percentage in enumerate(psutil.cpu_percent(percpu = True , interval = 1)):
                    print(f"Core {core} : {percentage}%")
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__