# GetEdgeNumber Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarConstrainedHandle..::..GetEdgeNumber Method   
[RebarConstrainedHandle Class](08b4c4a3-3bb9-0801-9cc8-cd5420a306d9.md "RebarConstrainedHandle Class") See Also  
---  
If the RebarConstrainedHandle's RebarHandleType is 'Edge', then this function will return the number of the edge that is driven by the handle. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public int GetEdgeNumber()
```
  
Visual Basic  
---  
```text
Public Function GetEdgeNumber As Integer
```
  
Visual C++  
---  
```text
public:
int GetEdgeNumber()
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | RebarConstrainedHandle is no longer valid. -or- The RebarConstrainedHandle is not of RebarHandleType 'Edge'. |

# See Also
[RebarConstrainedHandle Class](08b4c4a3-3bb9-0801-9cc8-cd5420a306d9.md "RebarConstrainedHandle Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 