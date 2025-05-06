# GetMultiplanarDefinition Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
RebarShape..::..GetMultiplanarDefinition Method   
[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.md "RebarShape Class") See Also  
---  
The optional 3D structure of the shape. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public RebarShapeMultiplanarDefinition GetMultiplanarDefinition()
```
  
Visual Basic  
---  
```text
Public Function GetMultiplanarDefinition As RebarShapeMultiplanarDefinition
```
  
Visual C++  
---  
```text
public:
RebarShapeMultiplanarDefinition^ GetMultiplanarDefinition()
```
  
# ### Return Value
A copy of the multiplanar definition. Changes will not affect the RebarShape. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md "DisabledDisciplineException Class") | None of the following disciplines is enabled: Structural. |

# See Also
[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.md "RebarShape Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 