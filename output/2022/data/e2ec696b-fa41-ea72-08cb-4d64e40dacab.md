# Erase Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
VoltageTypeSet..::..Erase Method   
[VoltageTypeSet Class](3d6a14b7-0399-2ef9-8685-cbfaaf7739cf.md "VoltageTypeSet Class") See Also  
---  
Removes a specified voltage type from the set.
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public virtual int Erase(
	VoltageType item
)
```
  
Visual Basic  
---  
```text
Public Overridable Function Erase ( _
	item As VoltageType _
) As Integer
```
  
Visual C++  
---  
```text
public:
virtual int Erase(
	VoltageType^ item
)
```
  
# ### Parameters
item
    Type: [Autodesk.Revit.DB.Electrical..::..VoltageType](6b462685-b825-f8f9-f218-035107f7aaf0.md "VoltageType Class")The voltage type to be erased.
# ### Return Value
The number of voltage types that were erased from the set.
# See Also
[VoltageTypeSet Class](3d6a14b7-0399-2ef9-8685-cbfaaf7739cf.md "VoltageTypeSet Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to 