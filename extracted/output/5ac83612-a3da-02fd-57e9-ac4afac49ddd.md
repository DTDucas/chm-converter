# Evaluate Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
EdgeEndPoint..::..Evaluate Method   
[EdgeEndPoint Class](3388e8f3-22d4-a411-a3da-450c16a31bc5.md "EdgeEndPoint Class") See Also  
---  
Evaluate the end point of the edge in 3d coordinates. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021 
# Syntax
C#  
---  
```text
public XYZ Evaluate()
```
  
Visual Basic  
---  
```text
Public Function Evaluate As XYZ
```
  
Visual C++  
---  
```text
public:
XYZ^ Evaluate()
```
  
# ### Return Value
The end point of the edge in 3d coordinates. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Failed to evaluate the end point of the edge. |

# See Also
[EdgeEndPoint Class](3388e8f3-22d4-a411-a3da-450c16a31bc5.md "EdgeEndPoint Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)