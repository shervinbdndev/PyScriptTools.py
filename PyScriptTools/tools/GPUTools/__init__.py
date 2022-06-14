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

    GPUTools
    ========
    version : 4.3.12\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import colorama
    from typing import Type
    from typing_extensions import Self
    
    from ...exceptions import *
    from ...utils import GPUUtils

except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run') from None


class GPUTools(GPUUtils):

    @classmethod
    def ShowGPU_ID(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _GPU ID_
        """
        if (type(show) is bool):
            if (show is True):
                for gpu in cls.gpuInfo:
                    gpuID = gpu.id
                return gpuID
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
    def ShowGPUName(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _GPU Name_
        """
        if (type(show) is bool):
            if (show is True):
                for gpu in cls.gpuInfo:
                    gpuName = gpu.name
                return gpuName
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
    def ShowGPULoad(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Load_
        """
        if (type(show) is bool):
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
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def ShowGPUFreeMemory(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Free Memory_
        """
        if (type(show) is bool):
            if (show is True):
                for gpu in cls.gpuInfo:
                    gpuFree = gpu.memoryFree
                return gpuFree
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
    def ShowGPUUsedMemory(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Used Memory_
        """
        if (type(show) is bool):
            if (show is True):
                for gpu in cls.gpuInfo:
                    gpuUsed = f"{gpu.memoryUsed}MB"
                return gpuUsed
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
    def ShowGPUTotalMemory(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Total Memory_
        """
        if (type(show) is bool):
            if (show is True):
                for gpu in cls.gpuInfo:
                    gpuTot = f"{gpu.memoryTotal}MB"
                return gpuTot
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
    def ShowGPUTemperature(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _GPU Temperature_
        """
        if (type(show) is bool):
            if (show is True):
                for gpu in cls.gpuInfo:
                    gpuTemp = f"{gpu.temperature}℃"
                return gpuTemp
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
    def ShowGPU_UUID(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _GPU UUID_
        """
        if (type(show) is bool):
            if (show is True):
                for gpu in cls.gpuInfo:
                    gpuUUID = gpu.uuid
                return gpuUUID
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__