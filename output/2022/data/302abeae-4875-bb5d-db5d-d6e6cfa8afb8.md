# GetElectricalSettings Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ElectricalSetting..::..GetElectricalSettings Method   
[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.md "ElectricalSetting Class") See Also  
---  
Get the electrical settings of the project. 
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public static ElectricalSetting GetElectricalSettings(
	Document document
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetElectricalSettings ( _
	document As Document _
) As ElectricalSetting
```
  
Visual C++  
---  
```text
public:
static ElectricalSetting^ GetElectricalSettings(
	Document^ document
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document. 
# ### Return Value
The electrical settings of the project. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.md "ElectricalSetting Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to 