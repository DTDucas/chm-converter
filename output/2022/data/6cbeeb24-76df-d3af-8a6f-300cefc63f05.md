# AddItem Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ComboBox..::..AddItem Method   
[ComboBox Class](a5667995-e628-13df-c157-39c95b2435d6.md "ComboBox Class") See Also  
---  
Adds a new item to the ComboBox.
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011
# Syntax
C#  
---  
```text
public ComboBoxMember AddItem(
	ComboBoxMemberData memberData
)
```
  
Visual Basic  
---  
```text
Public Function AddItem ( _
	memberData As ComboBoxMemberData _
) As ComboBoxMember
```
  
Visual C++  
---  
```text
public:
ComboBoxMember^ AddItem(
	ComboBoxMemberData^ memberData
)
```
  
# ### Parameters
memberData
    Type: [Autodesk.Revit.UI..::..ComboBoxMemberData](aba69b9c-dae6-c872-8dea-91ef7fda5e81.md "ComboBoxMemberData Class")An object containing the data needed to construct the ComboBoxMember. 
# ### Return Value
The newly added ComboBoxMember. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | Thrown when memberData is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Thrown when button with memberData.Name already exists in the drop-down list. |

# See Also
[ComboBox Class](a5667995-e628-13df-c157-39c95b2435d6.md "ComboBox Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 