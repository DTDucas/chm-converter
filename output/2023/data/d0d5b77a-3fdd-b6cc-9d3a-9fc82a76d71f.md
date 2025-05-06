# SetSymbolTypeId Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
FormatOptions..::..SetSymbolTypeId Method   
[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.md "FormatOptions Class") See Also  
---  
Sets the symbol that should be displayed to indicate the unit quantifying the value. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public void SetSymbolTypeId(
	ForgeTypeId symbolTypeId
)
```
  
Visual Basic  
---  
```text
Public Sub SetSymbolTypeId ( _
	symbolTypeId As ForgeTypeId _
)
```
  
Visual C++  
---  
```text
public:
void SetSymbolTypeId(
	ForgeTypeId^ symbolTypeId
)
```
  
# ### Parameters
symbolTypeId
    Type: [Autodesk.Revit.DB..::..ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md "ForgeTypeId Class") The symbol identifier. An empty identifier string indicates no symbol. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | symbolTypeId is not a valid symbol for the unit in this FormatOptions. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | UseDefault is true in this FormatOptions. |

# See Also
[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.md "FormatOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 