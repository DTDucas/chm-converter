# Bounds Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
BoundingBoxXYZ..::..Bounds Property   
[BoundingBoxXYZ Class](3c452286-57b1-40e2-2795-c90bff1fcec2.md "BoundingBoxXYZ Class") See Also  
---  
Indexed access for loops. Use 0 for Min and 1 for Max.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public XYZ this[
	int bound
] { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Bounds ( _
	bound As Integer _
) As XYZ
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property XYZ^ Bounds[int bound] {
	XYZ^ get (int bound);
	void set (int bound, XYZ^ value);
}
```
  
# ### Parameters
bound
    Type: System..::..Int32
# Remarks
The bounds are defined in the coordinate space of the box.
# See Also
[BoundingBoxXYZ Class](3c452286-57b1-40e2-2795-c90bff1fcec2.md "BoundingBoxXYZ Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 