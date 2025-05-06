# GetCellSpec Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
TableSectionData..::..GetCellSpec Method   
[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.md "TableSectionData Class") See Also  
---  
Gets the spec describing values of a cell, if applicable. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public ForgeTypeId GetCellSpec(
	int nRow,
	int nCol
)
```
  
Visual Basic  
---  
```text
Public Function GetCellSpec ( _
	nRow As Integer, _
	nCol As Integer _
) As ForgeTypeId
```
  
Visual C++  
---  
```text
public:
ForgeTypeId^ GetCellSpec(
	int nRow, 
	int nCol
)
```
  
# ### Parameters
nRow
    Type: System..::..Int32 The row index of the cell 
nCol
    Type: System..::..Int32 The column index of the cell 
# ### Return Value
Identifier of the spec, or empty if the cell does not contain a number with units. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The given row number nRow is invalid. -or- The given column number nCol is invalid. |

# See Also
[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.md "TableSectionData Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 