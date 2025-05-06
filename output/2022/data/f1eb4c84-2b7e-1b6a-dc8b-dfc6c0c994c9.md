# Unpin Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
MultistoryStairs..::..Unpin Method   
[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.md "MultistoryStairs Class") See Also  
---  
Removes a particular story of the stairs (identified by its base level id) from a stairs group. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2018 
# Syntax
C#  
---  
```text
public Stairs Unpin(
	ElementId levelId
)
```
  
Visual Basic  
---  
```text
Public Function Unpin ( _
	levelId As ElementId _
) As Stairs
```
  
Visual C++  
---  
```text
public:
Stairs^ Unpin(
	ElementId^ levelId
)
```
  
# ### Parameters
levelId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The base level id. If the level id belongs to the base level of a unpinned stairs element, it returns the stairs id directly. 
# ### Return Value
The unpinned stairs element. 
# Remarks
If the story at the given level is in a group, it will separate an individual stairs element from the group with "unpinned" status. Changes you make to the returned stairs element will not affect any other stairs. If the story of stairs is already an individual stairs element, the status will be changed to "unpinned". 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | There is no stairs instance at the given base levelId. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[MultistoryStairs Class](8b07cbff-013c-889f-8807-703e63a91923.md "MultistoryStairs Class")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 