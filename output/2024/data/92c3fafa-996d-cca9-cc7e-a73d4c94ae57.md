# RebarShapeSegmentEndReferenceType Enumeration (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarShapeSegmentEndReferenceType Enumeration  
See Also  
---  
A choice of two reference points for one end of a constraint driving the length of a RebarShapeSegment. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 **Since:** 2012 
# Syntax
C#  
---  
```text
public enum RebarShapeSegmentEndReferenceType
```
  
Visual Basic  
---  
```text
Public Enumeration RebarShapeSegmentEndReferenceType
```
  
Visual C++  
---  
```text
public enum class RebarShapeSegmentEndReferenceType
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| Straight | Refers to the end of the straight part of the segment: the point where the bend begins. |
| Exterior | Refers to the farthest point on the arc of the bend. Assuming the bend is 90 degrees or more, an Exterior constraint will be longer than a Straight constraint by an amount equal to the bend radius. |

# Remarks
The RebarShapeSegmentEndReferenceType of a constraint is meaningful only when the bend is [right](176a9649-853e-f173-c108-d6722fcd5b61.md "RebarShapeBendAngle Enumeration") or [obtuse](176a9649-853e-f173-c108-d6722fcd5b61.md "RebarShapeBendAngle Enumeration"). If the bend is [acute](176a9649-853e-f173-c108-d6722fcd5b61.md "RebarShapeBendAngle Enumeration"), the reference type is ignored. 
# See Also
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 