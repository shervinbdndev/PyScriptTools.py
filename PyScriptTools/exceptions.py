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

    PyScriptTools Exceptions
    ========================
    version : 4.3.1\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/
    
    PyScriptTools Builtin Exceptions : \n
        AdminPermissionRequestDenied\n
        NoneTypeArgumentBool\n
        NoneTypeArgumentInt\n
        NoneTypeArgumentString\n
        NoneLinuxMethod\n
        UndefinedOperatingSystem\n
        UnrecognizeableTypeArgument\n
        InvalidVariableType

"""



class AdminPermissionRequestDenied(Exception):
    """ Set the Argument Variable 'show' to 'True' """
class NoneTypeArgumentBool(Exception):
    """ The Variable For Argument 'show' Should be 'Boolean' Type """
class NoneTypeArgumentInt(Exception):
    """ The Variable For Argument 'timeout' Should be 'Int' Type """
class NoneTypeArgumentString(Exception):
    """ The Variable For Argument 'link' Should be 'String' Type """
class NoneLinuxMethod(Exception):
    """ This Method is not Used in Linux OS """
class UndefinedOperatingSystem(Exception):
    """ The Operating System is Not Defined Yet """
class UnrecognizeableTypeArgument(Exception):
    """ The Variable For Arguments is not Recognizeable """
class InvalidVariableType(Exception):
    """ The Variable Type Chosen is not The Correct One """