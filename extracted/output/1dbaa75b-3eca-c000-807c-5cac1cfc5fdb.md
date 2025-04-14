# IsEqual Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
TableData..::..IsEqual Method   
[TableData Class](ab967e17-822e-fd5f-760a-4810e2e7eb61.md "TableData Class") See Also  
---  
Checks if this element is equal in value to the other element. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public bool IsEqual(
	TableData OtherElem
)
```
  
Visual Basic  
---  
```text
Public Function IsEqual ( _
	OtherElem As TableData _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsEqual(
	TableData^ OtherElem
)
```
  
# ### Parameters
OtherElem
    Type: [Autodesk.Revit.DB..::..TableData](ab967e17-822e-fd5f-760a-4810e2e7eb61.md "TableData Class")
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[TableData Class](ab967e17-822e-fd5f-760a-4810e2e7eb61.md "TableData Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)