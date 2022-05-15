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
    version : 4.3.7\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import os
    import sys
    import platform
    import ctypes
    import psutil
    import getpass
    import datetime
    import colorama
    
    from ...validators import *
    from ...exceptions import *
    
except:
    raise ModuleNotFoundError



class SystemTools:
    osName = str(platform.system())
    osType = list(platform.architecture())[0]
    systemName = str(platform.node())
    try:
        getKernel32 = ctypes.windll.kernel32.GetTickCount64()
        getTime = int(str(getKernel32)[:-3])
        mins, sec = divmod(getTime, 60)
        hour, mins = divmod(mins, 60)
        days, hour = divmod(hour, 24)
        uptimeSystem = str("{0}:{1}:{2}:{3}").format(days , hour , mins , sec)
    except:
        getKernel32 = str(NoneLinuxMethod.__doc__);\
        getTime = str(NoneLinuxMethod.__doc__);\
        mins=str(NoneLinuxMethod.__doc__);\
        sec=str(NoneLinuxMethod.__doc__);\
        hour=str(NoneLinuxMethod.__doc__);\
        days=str(NoneLinuxMethod.__doc__);\
        uptimeSystem=str(NoneLinuxMethod.__doc__)
        luts = ''.join(map(str , os.popen(cmd='uptime').readlines()))
        LuptimeSystem = luts.split(sep=' ')[1]
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

    @classmethod
    def ShowOsType(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowNodeName(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowOSRelease(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowOSVersion(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowSystemName(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowSystemUptime(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowUserName(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowSystemInformation(cls , show : bool = False , os_name : str = "") -> str:
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

    @classmethod
    def ShowPythonVersion(cls , show : bool = False) -> str:
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

    @classmethod
    def ShowBootTime(cls , show : bool = False) -> str:
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