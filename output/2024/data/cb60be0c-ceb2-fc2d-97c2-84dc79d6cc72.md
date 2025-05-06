# SetSelectedElementIds Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
NavisworksExportOptions..::..SetSelectedElementIds Method   
[NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.md "NavisworksExportOptions Class") See Also  
---  
Sets the element ids of the elements to export. Used only when ExportScope = SelectedElements. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public void SetSelectedElementIds(
	ICollection<ElementId> ids
)
```
  
Visual Basic  
---  
```text
Public Sub SetSelectedElementIds ( _
	ids As ICollection(Of ElementId) _
)
```
  
Visual C++  
---  
```text
public:
void SetSelectedElementIds(
	ICollection<ElementId^>^ ids
)
```
  
# ### Parameters
ids
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)>
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.md "NavisworksExportOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 