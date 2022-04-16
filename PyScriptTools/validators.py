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
    
class BooleanValidator:
    def is_boolean(boolean):
        if (type(boolean) is bool):
            return boolean
        else:
            try:
                return bool(boolean)
            except TypeError:
                return 0

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