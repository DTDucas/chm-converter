# IsEqual Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
AlphanumericRevisionSettings..::..IsEqual Method   
[AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.md "AlphanumericRevisionSettings Class") See Also  
---  
Determines whether a specified AlphanumericRevisionSettings is the same as 'this'. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public bool IsEqual(
	AlphanumericRevisionSettings other
)
```
  
Visual Basic  
---  
```text
Public Function IsEqual ( _
	other As AlphanumericRevisionSettings _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsEqual(
	AlphanumericRevisionSettings^ other
)
```
  
# ### Parameters
other
    Type: [Autodesk.Revit.DB..::..AlphanumericRevisionSettings](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.md "AlphanumericRevisionSettings Class") The AlphanumericRevisionSettings object to be compared with 'this'. 
# ### Return Value
True, if two AlphanumericRevisionSettings are the same. 
# Remarks
The two AlphanumericRevisionSettings are regarded as the same only if they have the same revision numbering sequence, and the same prefix and suffix strings. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.md "AlphanumericRevisionSettings Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 