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

    SystemTools
    ===========
    version : 4.3.13\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import os
    import platform
    import colorama
    from typing import (Type , final)
    from typing_extensions import Self
    
    from ...validators import *
    from ...exceptions import *
    from ...utils import SystemUtils
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run') from None



class SystemTools(SystemUtils):
    
    def __repr__(self : Self) -> Self:
        super(SystemTools , self).__repr__()
        return 'SystemTools Class in PyScriptTools Library'

    @final
    @classmethod
    def ShowOsName(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Name_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.osName
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowOsType(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Type
        """
        if (type(show) is bool):
            if (show is True):
                return cls.osType
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowWindowsOSFullName(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Windows OS Fullname
        """
        if (platform.system()[0].upper() in ['W']):
            if (type(show) is bool):
                if (show is True):
                    return [str(i).split(sep=':')[1].strip() for i in os.popen(cmd='systeminfo').readlines() if ('OS Name:' in i)]
                elif (show is False):
                    return AdminPermissionRequestDenied.__doc__
                elif (show is None):
                    show = None
                    return NotNullableArgument.__doc__
                else:
                    return UnrecognizeableTypeArgument.__doc__
            else:
                return NoneTypeArgumentBool.__doc__
        else:
            return NoneLinuxMethod.__doc__

    @final
    @classmethod
    def ShowNodeName(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Node Name or System's Name_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.nodeName
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowOSRelease(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Release_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.sysRelease
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowOSVersion(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Version_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.sysVersion
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowSystemName(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _System's Name_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.systemName
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowSystemUptime(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _System's Uptime_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.uptimeSystem
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowUserName(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Active Logined Username_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.userName
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowSystemInformation(cls : Type[Self] , show : bool = False , os_name : str = "") -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            os_name (str): _Choose The Operating System_. Defaults to "".

        Returns:
            str: _Shows System Information Based On Your Operating System_
        """
        if (type(show) is bool):
            if (show is True):
                if (type(os_name) is str):
                    if (platform.system() in ['Windows'] == [os_name]):
                        print (
                            f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.BLUE}{cls.osName}" ,
                            f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{cls.osType}" ,
                            f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{cls.sysRelease}" ,
                            f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{cls.sysVersion}" ,
                            f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{cls.systemName or cls.nodeName}" ,
                            f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{cls.uptimeSystem}" ,
                            f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{cls.userName}"
                        )
                    elif (platform.system() in ['Linux'] == [os_name]):
                        print (
                                f"{colorama.ansi.Fore.GREEN}OS Name : {colorama.ansi.Fore.BLUE}{cls.osName}" ,
                                f"\n{colorama.ansi.Fore.GREEN}OS Type : {colorama.ansi.Fore.WHITE}{cls.osType}" ,
                                f"\n{colorama.ansi.Fore.GREEN}OS Release : {colorama.ansi.Fore.WHITE}{cls.sysRelease}" ,
                                f"\n{colorama.ansi.Fore.GREEN}OS Version : {colorama.ansi.Fore.WHITE}{cls.sysVersion}" ,
                                f"\n{colorama.ansi.Fore.GREEN}System Name : {colorama.ansi.Fore.WHITE}{cls.systemName or cls.nodeName}" ,
                                f"\n{colorama.ansi.Fore.GREEN}System Uptime : {colorama.ansi.Fore.WHITE}{cls.LuptimeSystem}" ,
                                f"\n{colorama.ansi.Fore.GREEN}User Logined As : {colorama.ansi.Fore.WHITE}{cls.userName}"
                            )
                    else:
                        return UndefinedOperatingSystem.__doc__
                else:
                    return InvalidVariableType.__doc__
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                UnrecognizeableTypeArgument
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowPythonVersion(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Python Version_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.pythonVer
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @final
    @classmethod
    def ShowBootTime(cls : Type[Self] , show : bool = False) -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.

        Returns:
            str: _Operating System's Boot Time_
        """
        if (type(show) is bool):
            if (show is True):
                return cls.bootTime
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__