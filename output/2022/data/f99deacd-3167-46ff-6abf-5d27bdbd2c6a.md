# VertexPositionColored Class (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
VertexPositionColored Class  
[Members](31438c12-c049-aadb-a375-0b531e897461.md "VertexPositionColored Members") See Also  
---  
A geometry vertex specified as a position in space with a color. 
**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public class VertexPositionColored : Vertex
```
  
Visual Basic  
---  
```text
Public Class VertexPositionColored _
	Inherits Vertex
```
  
Visual C++  
---  
```text
public ref class VertexPositionColored : public Vertex
```
  
# Remarks
The color of these vertices includes a transparency component In order to render them as transparent they must be rendered in the transparent pass See the 'IsTransparentPass' method of [DrawContext](b9244325-08c8-8bbd-a9f3-5d91d638d85d.md "DrawContext Class")
# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB.DirectContext3D..::..Vertex](0434973b-559d-a27f-25f9-f6bf6ef4f750.md "Vertex Class") Autodesk.Revit.DB.DirectContext3D..::..VertexPositionColored
# See Also
[VertexPositionColored Members](31438c12-c049-aadb-a375-0b531e897461.md "VertexPositionColored Members")
[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")
Send comments on this topic to 