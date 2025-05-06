# IsNotEmpty Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DisplacementElement..::..IsNotEmpty Method   
[DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.md "DisplacementElement Class") See Also  
---  
Validates that the input set of element ids is valid for a DisplacementElement. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public static bool IsNotEmpty(
	ICollection<ElementId> elementIds
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsNotEmpty ( _
	elementIds As ICollection(Of ElementId) _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsNotEmpty(
	ICollection<ElementId^>^ elementIds
)
```
  
# ### Parameters
elementIds
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> A set of element ids. 
# ### Return Value
True if the set of element ids is not empty. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.md "DisplacementElement Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 