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
        
        

class IntegerValidator:
    def is_integer(integer):
        if (type(integer) is int):
            return integer
        else:
            try:
                return int(integer)
            except TypeError:
                return ''
            
            
            
class BooleanValidator:
    def is_boolean(boolean):
        if (type(boolean) is bool):
            return boolean
        else:
            try:
                return bool(boolean)
            except TypeError:
                return ''