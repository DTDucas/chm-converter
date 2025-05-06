# CreateByThreePoints Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Plane..::..CreateByThreePoints Method   
[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.md "Plane Class") See Also  
---  
Creates a Plane object passing through three points supplied as arguments. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public static Plane CreateByThreePoints(
	XYZ point1,
	XYZ point2,
	XYZ point3
)
```
  
Visual Basic  
---  
```text
Public Shared Function CreateByThreePoints ( _
	point1 As XYZ, _
	point2 As XYZ, _
	point3 As XYZ _
) As Plane
```
  
Visual C++  
---  
```text
public:
static Plane^ CreateByThreePoints(
	XYZ^ point1, 
	XYZ^ point2, 
	XYZ^ point3
)
```
  
# ### Parameters
point1
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class") First of the three points that define a unique plane. The created Plane object will pass through these points. 
point2
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class") Second of the three points that define a unique plane. 
point3
    Type: [Autodesk.Revit.DB..::..XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class") Third of the three points that define a unique plane. 
# Remarks
The points supplied as arguments must fully define a plane: they may not lie on a straight line or be too close to each other. The points must lie within the Revit design limits. This function does not guarantee a specific parameterization of the created Plane. Use Plane.Create(Frame) to enforce a specific parameterization of the created Plane object. All three points are expected to lie within the Revit design limits [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.md "IsWithinLengthLimits Method"). 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The input point lies outside of Revit design limits. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.md "ArgumentsInconsistentException Class") | Throws if the input points do not define a unique plane. This is typically caused by points being too close to each other, or all three points being on or close to a straight line. |

# See Also
[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.md "Plane Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 