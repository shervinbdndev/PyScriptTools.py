# PyScriptTools

Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Shervin Badanara (shervinbdndev) on Github

## Examples of How To Use

For Installation Open Your CMD or Terminal and Type the Code Bellow
```python
pip install PyScriptTools
```
Thats it Now You Can Use it

<hr>

Print Your Public Address

```python
from PyScriptTools import NetworkTools

network_obj = NetworkTools()
public_ip = network_obj.ShowPublicIP()
print(public_ip)
```
Output
```python
89.39.108.150
```

<hr>

Also You Can Print Your Public IP To asccii Art !!!
```python
from PyScriptTools import (NetworkTools , OtherTools)

network_obj = NetworkTools()
ascii_obj = OtherTools()

print(ascii_obj.ConvertToAscii(network_obj.ShowPublicIP() , ['green' , 'red'] , 'center' , 'shade'))
```
Output
```python

 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░░██░░░██░░░░░░░████░░██░░░░░░░██░░░░██░░░██░░░░░░░██░░░████░░██░░
 ░█  █░█  █░░░░░░   █░█  █░░░░░░ █░░░█  █░█  █░░░░░░ █░░░█   ░█  █░
 ░ ██ ░ ███░░░░░░░░██░ ███░░░░░░░█░░░█░▌█░ ██ ░░░░░░░█░░░███░░█░▌█░
 ░█  █░░  █░░░░░░░░ █░░  █░░░░░░░█░░░█░ █░█  █░░░░░░░█░░░   █░█░ █░
 ░ ██ ░░░█ ░░░█░░████░░░█ ░░░█░░███░░ ██ ░ ██ ░░░█░░███░░███ ░ ██ ░
 ░░  ░░░░ ░░░░ ░░    ░░░ ░░░░ ░░   ░░░  ░░░  ░░░░ ░░   ░░   ░░░  ░░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

```
<hr>

Wanna See Your CPU Information?
```python
from PyScriptTools import CPUTools

cpu_obj = CPUTools()

print(cpu_obj.ShowCPUType())
print(cpu_obj.ShowCPUPhysicalCores())
print(cpu_obj.ShowCPUTotalCores())
print(cpu_obj.ShowCPUMaxFrequency())
print(cpu_obj.ShowCPUMinFrequency())
print(cpu_obj.ShowCPUCurrentFrequency())
print(cpu_obj.ShowCPUTotalUsage())
print(cpu_obj.ShowCPUUsagePerCore())
```
Output
```python
6
12
4104.00Mhz
0.00Mhz
4104.00Mhz
0.0%
Core 0 : 4.6%
Core 1 : 0.0%
Core 2 : 3.1%
Core 3 : 1.5%
Core 4 : 7.7%
Core 5 : 3.1%
Core 6 : 3.1%
Core 7 : 0.0%
Core 8 : 1.5%
Core 9 : 1.5%
Core 10 : 1.5%
Core 11 : 1.5%
```
<hr>

How About GPU Information?
```python
from PyScriptTools import GPUTools

gpu_obj = GPUTools()

print(gpu_obj.ShowGPU_ID())
print(gpu_obj.ShowGPUName())
print(gpu_obj.ShowGPULoad())
print(gpu_obj.ShowGPUFreeMemory())
print(gpu_obj.ShowGPUUsedMemory())
print(gpu_obj.ShowGPUTotalMemory())
print(gpu_obj.ShowGPUTemperature())
print(gpu_obj.ShowGPU_UUID())

```

Output
```python
0
NVIDIA GeForce RTX 2060
10.0%
5250.0
729.0MB
6144.0MB
49.0℃
GPU-fbe80806-8a49-abk8-ab8c-509d65993cb9
```
<hr>

If You Want To See Your RAM Status Use These Codes Below
```python

```
Output
```python

```

<hr>
<h3><b>Package Uploaded in PYPI :<a href="https://pypi.org/project/PyScriptTools/">Here</a></b></h3>
