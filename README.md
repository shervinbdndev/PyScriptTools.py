<h1 align='center'>PyScriptTools</h1>

<img style="display:block;margin-left:auto;margin-right:auto;width:50%;" src="https://github-readme-stats.vercel.app/api/pin/?username=shervinbdndev&repo=PyScriptTools&theme=dracula"></img>

<h3 align='center'>Under construction! Not ready for use yet! Currently experimenting and planning!</h3>
<h3 align='center'>Developed by Shervin Badanara (shervinbdndev) on Github</h3>
<hr>

<br><br><br>
<h1 align='center'>Update Your Interpreter</h1>

# Windows / CMD

```python
py -m pip install --upgrade pip
```

# Linux / Terminal

```python
python -m pip install --upgrade pip
```
<br>

<hr>
<br><br><br>
<h1 align='center'>Installation</h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install PyScriptTools
```
<h2 align='left'>or</h2>

```python
pip3 install PyScriptTools
```
<h2 align='left'>or</h2>

```python
py -m pip install PyScriptTools
```

<br><br><br>
<h1 align='center'>Update Library</h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install -U PyScriptTools
```

<h2 align='left'>or</h2>

```python
py -m pip install --upgrade PyScriptTools
```

<br>

<hr>
<br><br><br>
<h1 align='center'>Usage</h1>

<b>Print Your Public IP Address</b>

```python
from PyScriptTools import NetworkTools

network_obj = NetworkTools()
public_ip = network_obj.ShowPublicIP()
print(public_ip)
```
<b>Output</b>

```python
89.39.108.150
```

<hr>

<b>Also You Can Print Your Public IP To asccii Art !!!</b>

```python
from PyScriptTools import (NetworkTools , OtherTools)

network_obj = NetworkTools()
ascii_obj = OtherTools()

print(ascii_obj.ConvertToAscii(network_obj.ShowPublicIP() , ['green' , 'red'] , 'center' , 'shade'))
```

<b>Output</b>

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

<b>Wanna See Your CPU Information?</b>

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
<b>Output</b>

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

</b>How About GPU Information?</b>

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

<b>Output</b>

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

<b>If You Want To See Your RAM Status Use These Codes Below</b>

```python
from PyScriptTools import RAMTools

ram_obj = RAMTools()

print(ram_obj.ShowTotalRAM())
print(ram_obj.ShowAvailableRAM())
print(ram_obj.ShowUsedRAM())
print(ram_obj.ShowRAMPercentage())
print(ram_obj.ShowTotalSwap())
print(ram_obj.ShowFreeSwap())
print(ram_obj.ShowUsedSwap())
print(ram_obj.ShowSwapPercentage())
```
<b>Output</b>

```python
31.90GB
24.55GB
7.34GB
23.00B%
36.65GB
26.97GB
9.67GB
26.40B%
```
<hr>

<b>And Many Many Methods That You Can Use To See Your System Information Like</b>

```python
from PyScriptTools import SystemTools

system_obj = SystemTools()

print(system_obj.ShowOsName())
print(system_obj.ShowOSRelease())
print(system_obj.ShowOSVersion())
print(system_obj.ShowSystemUptime())
print(system_obj.ShowPythonVersion())
print(system_obj.ShowBootTime())
```

<b>Output</b>

```python
Windows
10
10.0.22000
7:1:8:41
3.9.0 
2022-02-22 00:19:29.929349
```
<hr>

<h3 align='center'>and many many Other methods . . . so</h3>
<h1 align='center'>Enjoy :)</h1>

<br>
<h3><b>Package Uploaded in PYPI :<a href="https://pypi.org/project/PyScriptTools/">Here</a></b></h3>