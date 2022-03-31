class AdminPermissionRequestDenied(Exception):
    """ Set the Argument Variable 'show' to 'True' """

class NoneTypeArgumentBool(Exception):
    """ The Variable For Argument 'show' Should be 'Boolean' Type """
    
class NoneTypeArgumentInt(Exception):
    """ The Variable For Argument 'timeout' Should be 'Int' Type """
    
class NoneTypeArgumentString(Exception):
    """ The Variable For Argument 'link' Should be 'String' Type """
    
class UnrecognizeableTypeArgument(Exception):
    """ The Variable For Arguments is not Recognizeable """
    
class UndefinedOperatingSystem(Exception):
    """ The Operating System is Not Defined Yet """