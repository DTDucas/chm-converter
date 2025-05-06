# BoundingBoxContainsPointFilter Constructor (XYZ, Double) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
BoundingBoxContainsPointFilter Constructor (XYZ, Double)  
[BoundingBoxContainsPointFilter Class](a5ea9f5a-ddba-9db7-eaa0-2b37098f0142.md "BoundingBoxContainsPointFilter Class") See Also  
---  
Constructs a new instance of a filter to match elements with a bounding box that contains the given point, while specifying the tolerance to be used in deciding if the point matches the criteria. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public BoundingBoxContainsPointFilter(
	XYZ point,
	double tolerance
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	point As XYZ, _
	tolerance As Double _
)
```
  
Visual C++  
---  
```text
public:
BoundingBoxContainsPointFilter(
	XYZ^ point, 
	double tolerance
)
```
  
# ### Parameters
point
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class") The point used to find elements with a bounding box that contains it. 
tolerance
    Type: System..::..Double The tolerance value to use instead of zero. See the tolerance property for details. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The given value for tolerance is not finite -or- The given value for tolerance is not a number |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[BoundingBoxContainsPointFilter Class](a5ea9f5a-ddba-9db7-eaa0-2b37098f0142.md "BoundingBoxContainsPointFilter Class")
[BoundingBoxContainsPointFilter Overload](293da828-ed6d-9a64-5143-953021760779.md "BoundingBoxContainsPointFilter Constructor")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 