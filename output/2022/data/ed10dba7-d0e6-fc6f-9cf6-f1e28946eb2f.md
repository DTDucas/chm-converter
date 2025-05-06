# ComputeDerivatives Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
CurveUV..::..ComputeDerivatives Method   
[CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.md "CurveUV Class") See Also  
---  
Computes the first derivative, the second derivative and the unit tangent vector at the specified parameter along the curve. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2021 
# Syntax
C#  
---  
```text
public IList<UV> ComputeDerivatives(
	double parameter,
	bool normalized
)
```
  
Visual Basic  
---  
```text
Public Function ComputeDerivatives ( _
	parameter As Double, _
	normalized As Boolean _
) As IList(Of UV)
```
  
Visual C++  
---  
```text
public:
IList<UV^>^ ComputeDerivatives(
	double parameter, 
	bool normalized
)
```
  
# ### Parameters
parameter
    Type: System..::..Double The specified parameter along the curve. 
normalized
    Type: System..::..Boolean If false, parameter is interpreted as natural parameterization of the curve. If true, param is expected to be in [0,1] interval mapped to the bounds of the curve. Setting to true is valid only if the curve is bound. 
# ### Return Value
The array containing three members: the first derivative (at index [0]), the second derivative (at index [1]) and the unit tangent vector (at index [2]). 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The given value for parameter is not finite |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | The curve cannot be evaluated as normalized because it is unbound. -or- The parameter is not a valid value for normalized evaluation. |

# See Also
[CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.md "CurveUV Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 