# SetVisibility Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
SSEPointVisibilitySettings..::..SetVisibility Method   
[SSEPointVisibilitySettings Class](5bd4779b-340d-8509-2376-1f97f828bf42.md "SSEPointVisibilitySettings Class") See Also  
---  
Sets the SSE point visibility for the given category. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public static void SetVisibility(
	Document document,
	ElementId categoryId,
	bool isVisible
)
```
  
Visual Basic  
---  
```text
Public Shared Sub SetVisibility ( _
	document As Document, _
	categoryId As ElementId, _
	isVisible As Boolean _
)
```
  
Visual C++  
---  
```text
public:
static void SetVisibility(
	Document^ document, 
	ElementId^ categoryId, 
	bool isVisible
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document. 
categoryId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The category id. 
isVisible
    Type: System..::..Boolean The visibility of the given category. True means the SSE points are visible. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The category is not valid for SSE. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[SSEPointVisibilitySettings Class](5bd4779b-340d-8509-2376-1f97f828bf42.md "SSEPointVisibilitySettings Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)