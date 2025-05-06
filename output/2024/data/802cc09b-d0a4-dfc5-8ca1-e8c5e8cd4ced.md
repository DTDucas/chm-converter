# Project Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Surface..::..Project Method   
[Surface Class](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class") See Also  
---  
Project a 3D point orthogonally onto a surface (to find the nearest point). Throws InvalidOperationException if the projection fails. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018.1 
# Syntax
C#  
---  
```text
public void Project(
	XYZ point,
	out UV uv,
	out double distance
)
```
  
Visual Basic  
---  
```text
Public Sub Project ( _
	point As XYZ, _
	<OutAttribute> ByRef uv As UV, _
	<OutAttribute> ByRef distance As Double _
)
```
  
Visual C++  
---  
```text
public:
void Project(
	XYZ^ point, 
	[OutAttribute] UV^% uv, 
	[OutAttribute] double% distance
)
```
  
# ### Parameters
point
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class") The point to project. 
uv
    Type: [Autodesk.Revit.DB..::..UV](1724be37-059b-91ff-aa74-d1508082f76d.md "UV Class")% The surface coordinates of the projected point. 
distance
    Type: System..::..Double% Holds the distance from input point to its projection. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The projection failed. |

# See Also
[Surface Class](bb391358-5ca0-578d-e8e2-6d1b30c472d8.md "Surface Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 