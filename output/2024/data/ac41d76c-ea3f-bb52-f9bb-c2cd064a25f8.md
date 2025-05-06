# AddIntersectionElement Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DividedSurface..::..AddIntersectionElement Method   
[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.md "DividedSurface Class") See Also  
---  
Adds an intersection element to the divided surface. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public void AddIntersectionElement(
	ElementId newIntersectionElemId
)
```
  
Visual Basic  
---  
```text
Public Sub AddIntersectionElement ( _
	newIntersectionElemId As ElementId _
)
```
  
Visual C++  
---  
```text
public:
void AddIntersectionElement(
	ElementId^ newIntersectionElemId
)
```
  
# ### Parameters
newIntersectionElemId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The intersection element to be added. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The element newIntersectionElemId is not a level, grid, reference plane, or a curve element whose category is lines and reference lines. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.md "DividedSurface Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 