<h1 align='center' style="font-size:5rem"><b>PyScriptTools</b></h1>
<p align='center'><b>Version 4.2.2</b></p>
<div align="center">
    <div align="center">
        <img src="https://img.shields.io/github/license/shervinbdndev/PyScriptTools.svg"></img>
    </div>
    <img src="https://img.shields.io/github/forks/shervinbdndev/PyScriptTools.svg"></img>
    <img src="https://img.shields.io/github/stars/shervinbdndev/PyScriptTools.svg"></img>
    <img src="https://img.shields.io/github/watchers/shervinbdndev/PyScriptTools.svg"></img>
    <img src="https://img.shields.io/github/issues-pr/shervinbdndev/PyScriptTools.svg"></img>
    <img src="https://img.shields.io/github/issues-pr-closed/shervinbdndev/PyScriptTools.svg"></img>
    <img src="https://img.shields.io/github/downloads/shervinbdndev/PyScriptTools/total.svg"></img>
</div>
<br>
<div align="center">
    <img style="display:block;margin-left:auto;margin-right:auto;width:70%;" src="https://github-readme-stats.vercel.app/api/pin/?username=shervinbdndev&repo=PyScriptTools&theme=dracula"></img>
</div>
<br>
<h3 align='center'>Under construction! Not ready for use yet! Currently experimenting and planning!</h3>
<h3 align='center'>Developed by Shervin Badanara (shervinbdndev) on Github</h3>
<div align="center">
    <img src="https://forthebadge.com/images/badges/made-with-python.svg"></img>
</div>
<br>
<hr>
<br>
<h2 align='center'><b>Language and technologies used in This Project</h2>
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></img>
<img src="https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white"></img>
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"></img>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"></img>
<img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></img>
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></img>
<img src="https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white"></img>
<img src="https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white"></img>

<br>
<h2 align='center'><b>WorkSpace</h2>
<img src="https://img.shields.io/badge/Intel-Core_i5_10700K-0071C5?style=for-the-badge&logo=intel&logoColor=white"></img>
<img src="https://img.shields.io/badge/NVIDIA-RTX2060 OC-76B900?style=for-the-badge&logo=nvidia&logoColor=white"></img>
<img src="https://img.shields.io/badge/Windows11-0078D6?style=for-the-badge&logo=windows&logoColor=white"></img>


<hr>

<br><br><br>
<h1 align='left'><b>Update Your Interpreter</b></h1>

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
<h1 align='left'><b>Installation</b></h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install PyScriptTools
```
<h2 align='left'>or</h2>

```python
py -m pip install PyScriptTools
```

<br><br><br>
<h1 align='left'><b>Update Library</b></h1>
 
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
<h1 align='left'><b>Usage</b></h1>

<br>

Classes  |  Methods Count
------------- | -------------
NetworkTools  | 7  
CPUTools  |  8  
GPUTools  |  8  
RAMTools  |  8  
DiskTools  |  6 
SystemTools  |  11
OtherTools  |  3

<br>

# NetworkTools
Methods  |  Args  |  Efficiency
------------- | ------------- | -------------
ShowLocalIP  |  show  |  Shows Your Local IP Address
ShowPublicIP  |  show  | Shows Your Public IP Address
ShowMacAddress  |  show , network_request  | Shows Your Mac Address
ShowNetworkInfo  |  show  | Shows Your Network Information
ShowSavedNetworks  |  show  | Shows a Bunch of Your Saved Networks
TestConnection  |  show , timeout  | Test That your Connected To Internet
StatusCodeChecker  |  show , link  | Check Every Status Codes on Every Urls You Want

# CPUTools
Methods  |  Args  |  Efficiency
------------- | ------------- | -------------
ShowCPUType  |  show  |  Returns CPU Type
ShowCPUPhysicalCores  |  show  |  Returns CPU Physical Cores
ShowCPUTotalCores  |  show  |  Returns CPU Total Cores
ShowCPUMaxFreq  |  show  |  Returns CPU Maximum Frequency
ShowCPUMinFreq  |  show  |  Returns CPU Minimum Frequency
ShowCPUCurrentFreq  |  show  |  Returns CPU Current Frequency
ShowCPUTotalUsage  |  show  |  Returns CPU Total Usage
ShowCPUUsagePerCore  |  show  |  Returns CPU Usage Per Cores

<br>

<h1 align='left'>Args Details</h1>

Args  |  Default Value  |  Details
------------- | ------------- | -------------
show  |  False  |  Gets The Admin Permission To Return The Output(Set The Value to True)
network_request  |  True  |  Uses Network Request to Get Mac Address(Set The Value to True)
timeout  | 5 |  Send a Request Through Network in Time Per Second
link  | '' |  Set The Value a Url in String Format

<br>

<b>Print Your Public IP Address</b>

```python
from PyScriptTools import NetworkTools

network_obj = NetworkTools()
public_ip = network_obj.ShowPublicIP(show=True)
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

print(ascii_obj.ConvertToAscii(show=True , text=network_obj.ShowPublicIP(show=True) , colors=['green' , 'red'] , align='left' , font='shade'))
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

print(cpu_obj.ShowCPUType(show=True))
print(cpu_obj.ShowCPUPhysicalCores(show=True))
print(cpu_obj.ShowCPUTotalCores(show=True))
print(cpu_obj.ShowCPUMaxFrequency(show=True))
print(cpu_obj.ShowCPUMinFrequency(show=True))
print(cpu_obj.ShowCPUCurrentFrequency(show=True))
print(cpu_obj.ShowCPUTotalUsage(show=True))
print(cpu_obj.ShowCPUUsagePerCore(show=True))
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

print(gpu_obj.ShowGPU_ID(show=True))
print(gpu_obj.ShowGPUName(show=True))
print(gpu_obj.ShowGPULoad(show=True))
print(gpu_obj.ShowGPUFreeMemory(show=True))
print(gpu_obj.ShowGPUUsedMemory(show=True))
print(gpu_obj.ShowGPUTotalMemory(show=True))
print(gpu_obj.ShowGPUTemperature(show=True))
print(gpu_obj.ShowGPU_UUID(show=True))

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

print(ram_obj.ShowTotalRAM(show=True))
print(ram_obj.ShowAvailableRAM(show=True))
print(ram_obj.ShowUsedRAM(show=True))
print(ram_obj.ShowRAMPercentage(show=True))
print(ram_obj.ShowTotalSwap(show=True))
print(ram_obj.ShowFreeSwap(show=True))
print(ram_obj.ShowUsedSwap(show=True))
print(ram_obj.ShowSwapPercentage(show=True))
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

print(system_obj.ShowOsName(show=True))
print(system_obj.ShowOSRelease(show=True))
print(system_obj.ShowOSVersion(show=True))
print(system_obj.ShowSystemUptime(show=True))
print(system_obj.ShowPythonVersion(show=True))
print(system_obj.ShowBootTime(show=True))
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

<h3 align='left'>and many many Other methods . . . so</h3>
<h1 align='left'>Enjoy :)</h1>

<br>
<h3><b>Package Uploaded in PYPI :<a href="https://pypi.org/project/PyScriptTools/">Here</a></b></h3>