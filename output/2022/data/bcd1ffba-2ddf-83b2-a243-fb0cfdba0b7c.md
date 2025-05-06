# SetDefaultElementTypeId Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Document..::..SetDefaultElementTypeId Method   
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") See Also  
---  
Sets the default element type id of the given DefaultElementType id. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public void SetDefaultElementTypeId(
	ElementTypeGroup defaultTypeId,
	ElementId typeId
)
```
  
Visual Basic  
---  
```text
Public Sub SetDefaultElementTypeId ( _
	defaultTypeId As ElementTypeGroup, _
	typeId As ElementId _
)
```
  
Visual C++  
---  
```text
public:
void SetDefaultElementTypeId(
	ElementTypeGroup defaultTypeId, 
	ElementId^ typeId
)
```
  
# ### Parameters
defaultTypeId
    Type: [Autodesk.Revit.DB..::..ElementTypeGroup](f5b57d98-c551-9693-9009-8eb17fef8a14.md "ElementTypeGroup Enumeration") The default element type id. 
typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The element type id. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The element type id typeId is invalid for the give DefaultElementType id defaultTypeId. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 