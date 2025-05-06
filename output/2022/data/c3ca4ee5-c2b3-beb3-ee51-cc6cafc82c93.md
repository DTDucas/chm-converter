# IsValidType Method (ElementId) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Element..::..IsValidType Method (ElementId)  
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") See Also  
---  
Checks if given type is valid for this element. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public bool IsValidType(
	ElementId typeId
)
```
  
Visual Basic  
---  
```text
Public Function IsValidType ( _
	typeId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsValidType(
	ElementId^ typeId
)
```
  
# ### Parameters
typeId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") ElementId of the type to check. 
# ### Return Value
True if element can have a type assigned and this type is valid for this element, false otherwise. 
# Remarks
A type is valid for an element if it can be assigned to the element. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class")
[IsValidType Overload](40c3c3f4-3f80-1f2d-c831-a65400367a55.md "IsValidType Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 