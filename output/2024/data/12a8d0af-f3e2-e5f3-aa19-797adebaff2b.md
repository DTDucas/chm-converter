# OnPolyline Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
IExportContextBase..::..OnPolyline Method   
[IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.md "IExportContextBase Interface") See Also  
---  
This method is called when a Polyline is being output. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
RenderNodeAction OnPolyline(
	PolylineNode node
)
```
  
Visual Basic  
---  
```text
Function OnPolyline ( _
	node As PolylineNode _
) As RenderNodeAction
```
  
Visual C++  
---  
```text
RenderNodeAction OnPolyline(
	PolylineNode^ node
)
```
  
# ### Parameters
node
    Type: [Autodesk.Revit.DB..::..PolylineNode](d0d38779-f0a4-e975-e71d-c8e7026cadfd.md "PolylineNode Class") An output node that represents a Polyline. 
# ### Return Value
Return RenderNodeAction.Proceed if you wish to receive tessellated geometry (polyline segments) for this polyline, or otherwise return RenderNodeAction.Skip. 
Note for 2D export: if the export is performed for the view in non-Wireframe display style tesselated geometry will be output regardless of the return value.
# Remarks
Note that this method is invoked only if the custom exporter was set up to include geometric objects in the output stream. See [IncludeGeometricObjects](2ce1075e-380e-01e7-6459-b7467c2a2414.md "IncludeGeometricObjects Property") for mode details. 
Note for 2D export: if the export is performed for the view in non-Wireframe display style this method will be called regardless of whether the object will be eventially output, i.e. even if it's occluded by another element.
# See Also
[IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.md "IExportContextBase Interface")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 