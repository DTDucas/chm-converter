# IsEndReferenceValid Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
StructuralFramingUtils..::..IsEndReferenceValid Method   
[StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.md "StructuralFramingUtils Class") See Also  
---  
Determines if the given reference can be set for the given end of the framing element. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public static bool IsEndReferenceValid(
	FamilyInstance familyInstance,
	int end,
	Reference pick
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsEndReferenceValid ( _
	familyInstance As FamilyInstance, _
	end As Integer, _
	pick As Reference _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsEndReferenceValid(
	FamilyInstance^ familyInstance, 
	int end, 
	Reference^ pick
)
```
  
# ### Parameters
familyInstance
    Type: [Autodesk.Revit.DB..::..FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md "FamilyInstance Class") The FamilyInstance, which must be of a structural framing category, non-concrete and joined at the given end. 
end
    Type: System..::..Int32 The index of the end (0 for the start, 1 for the end). 
pick
    Type: [Autodesk.Revit.DB..::..Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.md "Reference Class") The reference to be checked against the given end of the framing element. 
# ### Return Value
True if the given reference can be set for the given end of the framing element. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | end must be 0 or 1. |

# See Also
[StructuralFramingUtils Class](93d93c87-dfa2-12d5-dcb0-13d5cb0c0696.md "StructuralFramingUtils Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)