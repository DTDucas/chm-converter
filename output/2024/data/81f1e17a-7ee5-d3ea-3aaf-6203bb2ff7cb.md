# DiameterDimensionTypeId Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
BendingDetailCustomFieldProperties..::..DiameterDimensionTypeId Property   
[BendingDetailCustomFieldProperties Class](fca17725-1925-31a4-1a9b-c773c4329e46.md "BendingDetailCustomFieldProperties Class") See Also  
---  
Identifies the Id of the diameter dimension type which is used to show dimensions. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public ElementId DiameterDimensionTypeId { get; set; }
```
  
Visual Basic  
---  
```text
Public Property DiameterDimensionTypeId As ElementId
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ElementId^ DiameterDimensionTypeId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: The diameterDimensionTypeId should be an id of a diameter dimension type. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[BendingDetailCustomFieldProperties Class](fca17725-1925-31a4-1a9b-c773c4329e46.md "BendingDetailCustomFieldProperties Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 