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

    PyScriptTools Validators
    ========================
    version : 4.3.4\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/
    
    PyScriptTools Builtin Validators: \n
        LengthValidator\n
        StringValidator\n
        BooleanValidator\n
        IntegerValidator\n
        LinuxOperatingSystemIdentifierValidator\n
        WindowsOperatingSystemIdentifierValidator

"""



import platform



class OperatingSystem(object):
    WINDOWS : bool
    LINUX : bool

class LengthValidator:
    def getSize(bytes , default = "B"):
        for unit in ["" , "K" , "M" , "G" , "T" , "P"]:
            if (bytes < 1024):
                return f"{bytes:.2f}{unit}{default}"
            bytes /= 1024

class StringValidator:
    def is_string(string):
        if (type(string) is str):
            return string
        else:
            return str(string)
    
"""class BooleanValidator:
    def is_boolean(boolean):
        if (boolean in [True , False]):
            return boolean
        else:
            try:
                return bool(boolean)
            except TypeError:
                return 0"""

class IntegerValidator:
    def is_integer(integer):
        if (type(integer) is int):
            return integer
        else:
            try:
                return int(integer)
            except TypeError:
                return 0
            
class LinuxOperatingSystemIdentifierValidator(OperatingSystem):
    @classmethod
    def is_linux(cls , lnx):
        if (platform.system() == lnx):
            cls.LINUX = True
            cls.WINDOWS = False
            return lnx
        
    @property
    @classmethod
    def current_is_linux(cls):
        if (platform.system()[0].upper() == 'L'):
            cls.LINUX = True
            
class WindowsOperatingSystemIdentifierValidator(OperatingSystem):

    @classmethod
    def is_windows(cls , win):
        if (platform.system() == win):
            cls.WINDOWS = True
            cls.LINUX = False
            return win
        
    @property
    @classmethod
    def current_is_windows(cls):
        if (platform.system()[0].upper() == 'W'):
            cls.WINDOWS = True