# IsValidSymbol Method (ForgeTypeId) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FormatOptions..::..IsValidSymbol Method (ForgeTypeId)  
[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.md "FormatOptions Class") See Also  
---  
Checks whether a symbol is valid for the unit in this FormatOptions. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public bool IsValidSymbol(
	ForgeTypeId symbolTypeId
)
```
  
Visual Basic  
---  
```text
Public Function IsValidSymbol ( _
	symbolTypeId As ForgeTypeId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsValidSymbol(
	ForgeTypeId^ symbolTypeId
)
```
  
# ### Parameters
symbolTypeId
    Type: [Autodesk.Revit.DB..::..ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md "ForgeTypeId Class") Identifier of the symbol to check. 
# ### Return Value
True if the symbol is valid, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | UseDefault is true in this FormatOptions. |

# See Also
[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.md "FormatOptions Class")
[IsValidSymbol Overload](a965e857-57c6-25cb-1622-f2d80425e999.md "IsValidSymbol Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 