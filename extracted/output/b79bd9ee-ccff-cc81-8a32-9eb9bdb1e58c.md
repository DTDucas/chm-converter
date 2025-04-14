# Max Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
BoundingBoxXYZ..::..Max Property   
[BoundingBoxXYZ Class](3c452286-57b1-40e2-2795-c90bff1fcec2.md "BoundingBoxXYZ Class") See Also  
---  
Maximum coordinates (upper-right-front corner of the box).
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public XYZ Max { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Max As XYZ
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property XYZ^ Max {
	XYZ^ get ();
	void set (XYZ^ value);
}
```
  
# Remarks
The bounds are defined in the coordinate space of the box.
# See Also
[BoundingBoxXYZ Class](3c452286-57b1-40e2-2795-c90bff1fcec2.md "BoundingBoxXYZ Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)