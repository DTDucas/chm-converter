# SaveToProjectAsImage Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Document..::..SaveToProjectAsImage Method   
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") See Also  
---  
Creates an image view from the currently active view. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public ElementId SaveToProjectAsImage(
	ImageExportOptions options
)
```
  
Visual Basic  
---  
```text
Public Function SaveToProjectAsImage ( _
	options As ImageExportOptions _
) As ElementId
```
  
Visual C++  
---  
```text
public:
ElementId^ SaveToProjectAsImage(
	ImageExportOptions^ options
)
```
  
# ### Parameters
options
    Type: [Autodesk.Revit.DB..::..ImageExportOptions](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.md "ImageExportOptions Class") The options which govern the image creation. 
# ### Return Value
Id of the newly created view if the operation succeeded, invalid element id otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | options object is invalid: the ExportRange is invalid, must be CurrentView or VisibleRegionOfCurrentView, or the ViewName is invalid, must be non-empty, unique and should not contain prohibited characters. -or- The current view cannot be exported as an image |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)