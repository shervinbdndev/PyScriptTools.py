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

    OtherTools
    ==========
    version : 4.3.6\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/

"""


try:
    import os
    import cfonts
    import colorama
    import platform
    from typing import (Tuple , Any)
    
    from ...exceptions import *

except:
    raise ModuleNotFoundError



class OtherTools:
    pathValidation = bool()

    @classmethod
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
        if (type(show) is bool):
            if (show is True):
                if (type(text) in Any and type(font) is str):
                    cls.text = str(text)
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
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__

    @classmethod
    def IsPath(cls , show : bool = False , pathaddr : str = '') -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            pathaddr (str): _System's Local Address_. Defaults to ''.

        Returns:
            str: _Validates The Path You've Entered_
        """
        if (type(show) is bool):
            if (show is True):
                if (type(pathaddr) is str):
                    if (os.path.exists(r"{0}".format(pathaddr)) and (platform.system()[0].upper() in ["W" , "L" , "J"])):
                        return f"{colorama.ansi.Fore.GREEN}The Path Exists\nThe Code Output is {colorama.ansi.Fore.BLUE}{True}"
                    else:
                        return f"{colorama.ansi.Fore.RED}The Path Doesn't Exist\nThe Code Output is {colorama.ansi.Fore.BLUE}{False}"
                else:
                    return InvalidVariableType.__doc__
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
    def GetAbsOutput(cls , show : bool = False , string : str = '') -> str:
        """_summary_

        Args:
            show (bool): _Shows The Output_. Defaults to False.
            string (str): _Your Python Command or Expression_. Defaults to ''.

        Returns:
            str: _Runs The Text as a Python Command or Expression_
        """
        if (type(show) is bool):
            if (show is True):
                if (type(string) is str):
                    return eval(string)
                else:
                    return InvalidVariableType.__doc__
            elif (show is False):
                return AdminPermissionRequestDenied.__doc__
            elif (show is None):
                show = None
                return NotNullableArgument.__doc__
            else:
                return UnrecognizeableTypeArgument.__doc__
        else:
            return NoneTypeArgumentBool.__doc__