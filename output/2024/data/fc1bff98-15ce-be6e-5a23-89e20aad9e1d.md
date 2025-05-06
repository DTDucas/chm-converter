# Create Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ConicalSurface..::..Create Method   
[ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.md "ConicalSurface Class") See Also  
---  
Creates a conical surface defined by a local reference frame and a half angle. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public static ConicalSurface Create(
	Frame frameOfReference,
	double halfAngle
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	frameOfReference As Frame, _
	halfAngle As Double _
) As ConicalSurface
```
  
Visual C++  
---  
```text
public:
static ConicalSurface^ Create(
	Frame^ frameOfReference, 
	double halfAngle
)
```
  
# ### Parameters
frameOfReference
    Type: [Autodesk.Revit.DB..::..Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.md "Frame Class") frameOfReference is an orthonormal frame that defines a local coordinate system for the cone. 
  * Frame.Origin is a point on the cylinder's axis.
  * Frame.BasisZ points along the axis, while Frame.BasisX and Frame.BasisY are orthogonal to the axis. 
  * The frame may be either left-handed or right-handed (see Frame.IsRightHanded). Note that the "handedness" of the frame does not, by itself, determine the surface's orientation.

halfAngle
    Type: System..::..Double Cone angle. Must be not 0, lesser than PI/2 and greater than -PI/2. 
# ### Return Value
The created ConicalSurface. 
# Remarks
The parametric equation of the cone is S(u, v) = Frame.Origin + v*[sin(halfAngle)(cos(u)*Frame.BasisX + sin(u)*Frame.BasisY) + cos(halfAngle)*Frame.BasisZ] This implies the following facts: 
  * Frame.BasisX points from the axis point to the point on the cylinder with coordinates (0, 0).
  * Frame.BasisY points in the direction of the partial derivative dS/du at (0, 0).
  * Frame.BasisZ points in the direction of the partial derivative dS/dv at (0, 0).

Only the branch of the cone with v >= 0 should be used. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | This Frame object may not be used as a local frame of reference. -or- The supplied value must be not 0, lesser than PI/2 and greater than -PI/2. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.md "ConicalSurface Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 