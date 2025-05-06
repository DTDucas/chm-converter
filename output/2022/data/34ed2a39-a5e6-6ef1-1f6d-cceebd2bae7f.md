# Export2DGeometricObjectsIncludingPatternLines Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
CustomExporter..::..Export2DGeometricObjectsIncludingPatternLines Property   
[CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.md "CustomExporter Class") See Also  
---  
This flag sets the exporter of 2D views to either include or exclude output of face pattern lines as part of geometric objects when the model is being processed by the export context. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2020 
# Syntax
C#  
---  
```text
public bool Export2DGeometricObjectsIncludingPatternLines { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Export2DGeometricObjectsIncludingPatternLines As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool Export2DGeometricObjectsIncludingPatternLines {
	bool get ();
	void set (bool value);
}
```
  
# Remarks
This flag is ignored if view has Wireframe display style. This flag is ignored unless property "IncludeGeometricObjects" is set to true. 
# See Also
[CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.md "CustomExporter Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 