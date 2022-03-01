# PyScriptTools

Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Shervin Badanara (shervinbdndev) on Github

## Examples of How To Use

Print Your Public Address

```python
from PyScriptTools import NetworkTools

network_obj = NetworkTools()
public_ip = network_obj.ShowPublicIP()
print(public_ip)
```

Also You Can Print Your Public IP To asccii Art !!!
```python
from PyScriptTools import (NetworkTools , OtherTools)

network_obj = NetworkTools()
ascii_obj = OtherTools()

print(ascii_obj.ConvertToAscii(network_obj.ShowPublicIP() , ['green' , 'red'] , 'center' , 'shade'))
```