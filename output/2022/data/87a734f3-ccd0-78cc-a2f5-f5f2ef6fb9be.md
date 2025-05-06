# AssociatedBuildingPadId Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
TopographySurface..::..AssociatedBuildingPadId Property   
[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.md "TopographySurface Class") See Also  
---  
The element id of the building pad which causes this topography surface to be formed. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public ElementId AssociatedBuildingPadId { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property AssociatedBuildingPadId As ElementId
	Get
```
  
Visual C++  
---  
```text
public:
property ElementId^ AssociatedBuildingPadId {
	ElementId^ get ();
}
```
  
# Remarks
InvalidElementId returned signals that there is no associated building pad. 
# See Also
[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.md "TopographySurface Class")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 