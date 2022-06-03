import socket
from PyScriptTools.tools import NetworkTools


assert NetworkTools.ShowLocalIP(show=True) == socket.gethostbyname(socket.gethostname())