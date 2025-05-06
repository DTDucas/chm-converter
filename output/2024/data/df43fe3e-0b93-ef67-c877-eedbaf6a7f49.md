# IsValidParameterDefinitionId Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ColorFillScheme..::..IsValidParameterDefinitionId Method   
[ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.md "ColorFillScheme Class") See Also  
---  
Checks whether the input parameter id can be applied to the scheme. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public bool IsValidParameterDefinitionId(
	ElementId parameterId
)
```
  
Visual Basic  
---  
```text
Public Function IsValidParameterDefinitionId ( _
	parameterId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsValidParameterDefinitionId(
	ElementId^ parameterId
)
```
  
# ### Parameters
parameterId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")
# ### Return Value
Returns true if the input parameter id can be set to this scheme, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.md "ColorFillScheme Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 