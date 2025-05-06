# GetCurveUV Method (Int32, Transform2D) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Edge..::..GetCurveUV Method (Int32, Transform2D)  
[Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.md "Edge Class") See Also  
---  
Calculate and transform a 2D curve that represents the edge in the uv-parameter plane of one of the edge's faces. The output curve's direction will follow the parametric direction of the edge, not the topological direction of the edge on the given face. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2021
# Syntax
C#  
---  
```text
public CurveUV GetCurveUV(
	int index,
	Transform2D transform
)
```
  
Visual Basic  
---  
```text
Public Function GetCurveUV ( _
	index As Integer, _
	transform As Transform2D _
) As CurveUV
```
  
Visual C++  
---  
```text
public:
CurveUV^ GetCurveUV(
	int index, 
	Transform2D^ transform
)
```
  
# ### Parameters
index
    Type: System..::..Int32The index of the face (0 or 1).
transform
    Type: [Autodesk.Revit.DB..::..Transform2D](49a13f08-08d7-95b1-d52e-65f90e6d4061.md "Transform2D Class")Transformation to apply to the curve.
# ### Return Value
If successful, returns the calculated and transformed CurveUV, nullNothingnullptra null reference (Nothing in Visual Basic) otherwise.
# Remarks
Use of this function is preferred over using GetCurveUV(int index) and then transforming the curve, as the latter approach may yield a less accurate result. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | Thrown when the specified index is not 0 or 1. |

# See Also
[Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.md "Edge Class")
[GetCurveUV Overload](fa95b450-4354-00d7-f02c-f5319086f63f.md "GetCurveUV Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 