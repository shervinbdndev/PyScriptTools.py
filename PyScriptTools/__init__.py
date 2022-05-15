# █▀█ █▄█ █▀▀ █▀▀ █▀█ █ █▀█ ▀█▀ ▀█▀ █▀█ █▀█ █   █▀▀
# █▀▀  █  ▄▄█ █▄▄ █▀▄ █ █▀▀  █   █  █▄█ █▄█ █▄▄ ▄▄█

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

    PyScriptTools Library
    =====================
    version : 4.3.5\n
    author : Shervin Badanara\n
    author github : https://www.github.com/shervinbdndev/\n
    source github : https://www.github.com/shervinbdndev/PyScriptTools.py/\n
    
    PyScriptTools is a Python Based Library That You Can Use it To Gather your System Information.\n
    for e.x You Can Print Your Public IP Address:\n
        >>> from PyScriptTools import NetworkTools
        
        >>> network_obj = NetworkTools()
        >>> public_ip = network_obj.ShowPublicIP(show=True)
        >>> print(public_ip)

"""

try:
    import os
    import sys
    from pathlib import Path
    
    from .base import *
    from .validators import *
    from .exceptions import *
    from .NetworkTools import *
    from .CPUTools import *
    from .GPUTools import *
    from .RAMTools import *
    from .DiskTools import *
    from .SystemTools import *
    from .OtherTools import *

except:
    pass

    
    
if (__name__ == '__main__' and __package__ is None):
    sys.path.append(os.path.dirname(p=os.path.dirname(p=os.path.abspath(path=__file__))))
    file = Path(__file__).resolve()
    parent , top = file.parent , file.parents[3]
    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:
        pass