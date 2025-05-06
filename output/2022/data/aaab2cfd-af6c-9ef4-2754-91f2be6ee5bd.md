# CanHaveOrdinateDimensionSetting Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
DimensionType..::..CanHaveOrdinateDimensionSetting Method   
[DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.md "DimensionType Class") See Also  
---  
Checks whether this DimensionType can have an ordinate dimension settings. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public bool CanHaveOrdinateDimensionSetting()
```
  
Visual Basic  
---  
```text
Public Function CanHaveOrdinateDimensionSetting As Boolean
```
  
Visual C++  
---  
```text
public:
bool CanHaveOrdinateDimensionSetting()
```
  
# ### Return Value
True when the DimensionType is linear and the Dimension String Type parameter is ordinate, false otherwise. 
# Remarks
It returns true when the DimensionType is linear and when Dimension String Type parameter is set to Ordinate. 
# See Also
[DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.md "DimensionType Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 