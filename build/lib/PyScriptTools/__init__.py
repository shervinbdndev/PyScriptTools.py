from PyScriptTools import (
    Constants ,
    NetworkTools ,
    CPUTools ,
    GPUTools ,
    RAMTools ,
    DiskTools ,
    SystemTools ,
    OtherTools
    )


classes : dict = dict({
    'tools' :{
        'netwrok-tools' : NetworkTools() ,
        'cpu-tools' : CPUTools() ,
        'gpu-tools' : GPUTools() ,
        'ram-tools' : RAMTools() ,
        'disk-tools' : DiskTools() ,
        'system-tools' : SystemTools() ,
        'other-tools' : OtherTools()
    } ,
    'const-values' : {
        'constants' : Constants()
    }
})