# Location Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AssemblyInstance..::..Location Property   
[AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.md "AssemblyInstance Class") See Also  
---  
This property is used to find the physical location of the assembly instance within project.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013
# Syntax
C#  
---  
```text
public override Location Location { get; }
```
  
Visual Basic  
---  
```text
Public Overrides ReadOnly Property Location As Location
	Get
```
  
Visual C++  
---  
```text
public:
virtual property Location^ Location {
	Location^ get () override;
}
```
  
# Remarks
The Location property returns an object that can be used to find the location of an object within the project. Assembly instances return a point location object positioned at the center of the assembly instance.
# See Also
[AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.md "AssemblyInstance Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)