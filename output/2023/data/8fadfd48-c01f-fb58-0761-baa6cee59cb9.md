# STLExportOptions Constructor (ExportResolution) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
STLExportOptions Constructor (ExportResolution)  
[STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.md "STLExportOptions Class") See Also  
---  
Constructs a new instance of STLExportOptions with all predefined tessellation settings, depending on export resolution type. Note: in case of Custom resolution type, tessellation settings won't be predefined and will have default values. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2021.1 
# Syntax
C#  
---  
```text
public STLExportOptions(
	ExportResolution resolutionType
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	resolutionType As ExportResolution _
)
```
  
Visual C++  
---  
```text
public:
STLExportOptions(
	ExportResolution resolutionType
)
```
  
# ### Parameters
resolutionType
    Type: [Autodesk.Revit.DB..::..ExportResolution](671e963b-c211-17e7-2c26-5d772d34798a.md "ExportResolution Enumeration") The type of export resolution. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.md "STLExportOptions Class")
[STLExportOptions Overload](202b3151-da4b-fbad-08e1-d63e2fb80930.md "STLExportOptions Constructor")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 