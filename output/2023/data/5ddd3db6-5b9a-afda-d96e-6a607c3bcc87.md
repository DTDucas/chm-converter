# FaceNormal Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PlanarFace..::..FaceNormal Property   
[PlanarFace Class](e5f08848-bd35-4b17-ac7b-ae39fd817d6d.md "PlanarFace Class") See Also  
---  
Normal of the planar face.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public XYZ FaceNormal { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property FaceNormal As XYZ
	Get
```
  
Visual C++  
---  
```text
public:
property XYZ^ FaceNormal {
	XYZ^ get ();
}
```
  
# Remarks
This property is the "face normal" vector, and thus should return a vector consistently pointing out of the solid that this face is a boundary for (if it is a part of a solid). 
# See Also
[PlanarFace Class](e5f08848-bd35-4b17-ac7b-ae39fd817d6d.md "PlanarFace Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 