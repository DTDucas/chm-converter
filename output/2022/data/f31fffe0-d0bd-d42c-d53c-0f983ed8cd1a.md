# GetAutoDetectMatchedElements Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
AnalyticalModel..::..GetAutoDetectMatchedElements Method   
[AnalyticalModel Class](b4466cf0-0fa0-1f67-d442-fdf0fb073fc9.md "AnalyticalModel Class") See Also  
---  
Retrieves other Element Ids that this Element is Auto-detecting against. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public ICollection<ElementId> GetAutoDetectMatchedElements(
	AnalyticalDirection direction
)
```
  
Visual Basic  
---  
```text
Public Function GetAutoDetectMatchedElements ( _
	direction As AnalyticalDirection _
) As ICollection(Of ElementId)
```
  
Visual C++  
---  
```text
public:
ICollection<ElementId^>^ GetAutoDetectMatchedElements(
	AnalyticalDirection direction
)
```
  
# ### Parameters
direction
    Type: [Autodesk.Revit.DB.Structure..::..AnalyticalDirection](28165f4a-7863-07e2-7b95-c2bcbbae1872.md "AnalyticalDirection Enumeration") Direction in which Analytical Auto-detect is being done. 
# ### Return Value
A set of Element Ids against which this Element is Auto-detecting. The set may be empty if this Element is not Auto-detecting against anything. 
# Remarks
An empty set is a valid return value. It just means that this Element is not Auto-detecting against any other Elements in the given direction. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | direction is invalid for Analytical Auto-detect. |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[AnalyticalModel Class](b4466cf0-0fa0-1f67-d442-fdf0fb073fc9.md "AnalyticalModel Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 