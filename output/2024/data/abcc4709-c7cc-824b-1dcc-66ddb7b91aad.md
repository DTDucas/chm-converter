# MoveBarInSet Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarInSystem..::..MoveBarInSet Method   
[RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.md "RebarInSystem Class") See Also  
---  
This method applies the transformation matrix to the rebar bar at the desired position in the rebar set. If the bar was already moved, the method will concatenate the transformation matrix with the existing movement. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public void MoveBarInSet(
	int barPositionIndex,
	Transform moveTransform
)
```
  
Visual Basic  
---  
```text
Public Sub MoveBarInSet ( _
	barPositionIndex As Integer, _
	moveTransform As Transform _
)
```
  
Visual C++  
---  
```text
public:
void MoveBarInSet(
	int barPositionIndex, 
	Transform^ moveTransform
)
```
  
# ### Parameters
barPositionIndex
    Type: System..::..Int32 The bar index of the rebar to apply the transformation. 
moveTransform
    Type: [Autodesk.Revit.DB..::..Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.md "Transform Class") The transformation matrix to apply to the specified rebar bar. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | barPositionIndex is not in the range [ 0, NumberOfBarPositions-1 ]. |
| [Autodesk.Revit.Exceptions..::..InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.md "InapplicableDataException Class") | For this RebarInSystem element individual bars can't be moved, excluded or included. |

# See Also
[RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.md "RebarInSystem Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 