# NatureId Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
LoadCase..::..NatureId Property   
[LoadCase Class](2a215599-9c4c-d817-e170-605fd705699d.md "LoadCase Class") See Also  
---  
The nature ID of the load case. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public ElementId NatureId { get; set; }
```
  
Visual Basic  
---  
```text
Public Property NatureId As ElementId
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ElementId^ NatureId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: the natureId does not refer to LoadNature element. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[LoadCase Class](2a215599-9c4c-d817-e170-605fd705699d.md "LoadCase Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 