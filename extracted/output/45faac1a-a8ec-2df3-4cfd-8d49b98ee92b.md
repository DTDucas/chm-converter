# ScheduleMark Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarContainer..::..ScheduleMark Property   
[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.md "RebarContainer Class") See Also  
---  
The Schedule Mark parameter. On creation, the Schedule Mark is set to a value that is unique to the host, but it can be set to any value. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public string ScheduleMark { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ScheduleMark As String
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property String^ ScheduleMark {
	String^ get ();
	void set (String^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.md "RebarContainer Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)