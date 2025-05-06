# CreateCurve Method (IList(XYZ), IList(Double)) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
NurbSpline..::..CreateCurve Method (IList<(Of <(<'XYZ>)>)>, IList<(Of <(<'Double>)>)>)  
[NurbSpline Class](65c43ffe-3972-ae2b-4aa4-e2901cdbb3a8.md "NurbSpline Class") See Also  
---  
Creates a new geometric Curve object from NURBS curve data containing just control points and weights. The created curve may be a NURBSpline or a simpler curve such as line or arc. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public static Curve CreateCurve(
	IList<XYZ> controlPoints,
	IList<double> weights
)
```
  
Visual Basic  
---  
```text
Public Shared Function CreateCurve ( _
	controlPoints As IList(Of XYZ), _
	weights As IList(Of Double) _
) As Curve
```
  
Visual C++  
---  
```text
public:
static Curve^ CreateCurve(
	IList<XYZ^>^ controlPoints, 
	IList<double>^ weights
)
```
  
# ### Parameters
controlPoints
    Type: System.Collections.Generic..::..IList<(Of <(<'[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class")>)>)> The control points of the NURBSpline. 
weights
    Type: System.Collections.Generic..::..IList<(Of <(<'Double>)>)> The weights of the NURBSpline. 
# ### Return Value
The new Curve object. 
# Remarks
There must be at least 2 control points. The number of weights must be equal to the the number of control points. The values of all weights must be positive. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The number of control points must be at least 2. -or- The number of weights must be the same as the number of control points and all weights must be positive. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions..::..ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.md "ArgumentsInconsistentException Class") | Curve length is too small for Revit's tolerance (as identified by Application.ShortCurveTolerance). |

# See Also
[NurbSpline Class](65c43ffe-3972-ae2b-4aa4-e2901cdbb3a8.md "NurbSpline Class")
[CreateCurve Overload](774a9983-44a1-6cd9-36f2-0e40a819c5f7.md "CreateCurve Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 