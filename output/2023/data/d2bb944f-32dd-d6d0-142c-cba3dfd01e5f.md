# SetHookOrientation Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Rebar..::..SetHookOrientation Method   
[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.md "Rebar Class") See Also  
---  
Defines the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public void SetHookOrientation(
	int iEnd,
	RebarHookOrientation hookOrientation
)
```
  
Visual Basic  
---  
```text
Public Sub SetHookOrientation ( _
	iEnd As Integer, _
	hookOrientation As RebarHookOrientation _
)
```
  
Visual C++  
---  
```text
public:
void SetHookOrientation(
	int iEnd, 
	RebarHookOrientation hookOrientation
)
```
  
# ### Parameters
iEnd
    Type: System..::..Int32 0 for the start hook, 1 for the end hook. 
hookOrientation
    Type: [Autodesk.Revit.DB.Structure..::..RebarHookOrientation](e8365754-0811-8d4e-864a-55bf34af3a87.md "RebarHookOrientation Enumeration") Only two values are permitted: Value = Right: The hook is on your right as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." Value = Left: The hook is on your left as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." 
# Remarks
If RebarShapeDefinesHooks property of ReinforcementSettings is true (non-European shapes), setHookOrientation method does nothing. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | iEnd must be 0 or 1. -or- A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md "DisabledDisciplineException Class") | None of the following disciplines is enabled: Structural. |

# See Also
[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.md "Rebar Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 