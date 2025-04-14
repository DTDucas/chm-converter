# Print Method (ViewSet)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Document..::..Print Method (ViewSet)  
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") See Also  
---  
Prints a set of views with default view template and default print settings.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public void Print(
	ViewSet views
)
```
  
Visual Basic  
---  
```text
Public Sub Print ( _
	views As ViewSet _
)
```
  
Visual C++  
---  
```text
public:
void Print(
	ViewSet^ views
)
```
  
# ### Parameters
views
    Type: [Autodesk.Revit.DB..::..ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.md "ViewSet Class")The set of views which need to be printed.
# Remarks
If one view in the set can not be printed successfully then an exception will be thrown.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when printing is not allowed in the current application mode. Or when at least one view from the view set is not a printable view. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | Thrown when the view set to be printed is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Thrown when the view set contains a nullNothingnullptra null reference (Nothing in Visual Basic) element. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when at least one view from the view set could not be printed. |
| [Autodesk.Revit.Exceptions..::..OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.md "OperationCanceledException Class") | Thrown when print is cancelled by event handler. |

# See Also
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")
[Print Overload](e491ce6c-4350-0335-5388-28875da09c7e.md "Print Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)