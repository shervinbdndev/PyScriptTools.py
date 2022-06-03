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

    RAMTools
    ========
    version : 4.3.10\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import psutil
    from typing import Type
    from typing_extensions import Self
    
    from ...validators import *
    from ...exceptions import *

except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run') from None


class RAMTools:
    ramVir = psutil.virtual_memory()
    swapMemo = psutil.swap_memory()
    
    @classmethod
    def ShowTotalRAM(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Total RAM Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.ramVir.total)}"
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
    def ShowAvailableRAM(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Available RAM Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.ramVir.available)}"
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
    def ShowUsedRAM(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Used RAM Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.ramVir.used)}"
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
    def ShowRAMPercentage(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _RAM Percentage_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.ramVir.percent)}%"
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
    def ShowTotalSwap(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Total Swap Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.swapMemo.total)}"
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
    def ShowFreeSwap(cls : Type[Self] , show : bool = False) -> int:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            int: _Free Swap Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.swapMemo.free)}"
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
    def ShowUsedSwap(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Used Swap Memory_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.swapMemo.used)}"
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
    def ShowSwapPercentage(cls : Type[Self] , show : bool = False) -> float:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            float: _Swap Percentage_
        """
        if (type(show) is bool):
            if (show is True):
                return f"{LengthValidator.getSize(cls.swapMemo.percent)}%"
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__