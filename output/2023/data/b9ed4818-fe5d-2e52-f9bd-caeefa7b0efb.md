# CanRemoveRow Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
TableSectionData..::..CanRemoveRow Method   
[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.md "TableSectionData Class") See Also  
---  
Verifies that if the row at the given index can be removed.. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public bool CanRemoveRow(
	int nIndex
)
```
  
Visual Basic  
---  
```text
Public Function CanRemoveRow ( _
	nIndex As Integer _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool CanRemoveRow(
	int nIndex
)
```
  
# ### Parameters
nIndex
    Type: System..::..Int32 An integer index. 
# ### Return Value
True if the row can be removed, false otherwise 
# See Also
[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.md "TableSectionData Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 