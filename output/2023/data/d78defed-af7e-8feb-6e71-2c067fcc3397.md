# GetEndTreatmentTypeId Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
RebarShape..::..GetEndTreatmentTypeId Method   
[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.md "RebarShape Class") See Also  
---  
Gets the id of the EndTreatmentType at the specified rebar shape end. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public ElementId GetEndTreatmentTypeId(
	int iEnd
)
```
  
Visual Basic  
---  
```text
Public Function GetEndTreatmentTypeId ( _
	iEnd As Integer _
) As ElementId
```
  
Visual C++  
---  
```text
public:
ElementId^ GetEndTreatmentTypeId(
	int iEnd
)
```
  
# ### Parameters
iEnd
    Type: System..::..Int32 0 for the start end treatment, 1 for the end end treatment. 
# ### Return Value
Returns the id of an EndTreatmentType, or invalidElementId if the rebar shape has no end treatment at the specified end. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | iEnd not a valid shape end |

# See Also
[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.md "RebarShape Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 