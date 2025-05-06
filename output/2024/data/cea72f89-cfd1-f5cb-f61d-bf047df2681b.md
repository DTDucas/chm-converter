# View Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Options..::..View Property   
[Options Class](aa41fc13-9f81-836c-4271-82568ba5d7e8.md "Options Class") See Also  
---  
The view used for geometry extraction.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public View View { get; set; }
```
  
Visual Basic  
---  
```text
Public Property View As View
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property View^ View {
	View^ get ();
	void set (View^ value);
}
```
  
# Remarks
If a view-specific version of an element exists, it will be extracted in the retrieval of geometry. Also, the detail level of the geometry will be taken from the view's detail level.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | Thrown when setting this property with a nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when setting this property, if DetailLevel is already set. When DetailLevel is set view-specific geometry can't be extracted. |

# See Also
[Options Class](aa41fc13-9f81-836c-4271-82568ba5d7e8.md "Options Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 