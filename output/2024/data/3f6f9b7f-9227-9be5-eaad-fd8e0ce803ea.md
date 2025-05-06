# RemoveEndReference Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
StructuralFramingUtils..::..RemoveEndReference Method   
[StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.md "StructuralFramingUtils Class") See Also  
---  
Resets the end reference of the structural framing element. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public static void RemoveEndReference(
	FamilyInstance familyInstance,
	int end
)
```
  
Visual Basic  
---  
```text
Public Shared Sub RemoveEndReference ( _
	familyInstance As FamilyInstance, _
	end As Integer _
)
```
  
Visual C++  
---  
```text
public:
static void RemoveEndReference(
	FamilyInstance^ familyInstance, 
	int end
)
```
  
# ### Parameters
familyInstance
    Type: [Autodesk.Revit.DB..::..FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md "FamilyInstance Class") The FamilyInstance, which must be of a structural framing category, non-concrete and joined. 
end
    Type: System..::..Int32 The index of the end (0 for the start, 1 for the end). 
# Remarks
The setback value will be changed as a result of the removal. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | end must be 0 or 1. |
| [Autodesk.Revit.Exceptions..::..ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.md "ArgumentsInconsistentException Class") | The input familyInstance is not of a structural framing category or is concrete or is not joined at given end and cannot have an end reference set. |

# See Also
[StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.md "StructuralFramingUtils Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 