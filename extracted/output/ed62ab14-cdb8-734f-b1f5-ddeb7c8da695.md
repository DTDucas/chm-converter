# RadioButtonGroupData Constructor

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RadioButtonGroupData Constructor   
[RadioButtonGroupData Class](eeda7b4e-226f-b9a2-12d8-6768d295ca4a.md "RadioButtonGroupData Class") See Also  
---  
Constructs a new instance of RadioButtonGroupData.
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011
# Syntax
C#  
---  
```text
public RadioButtonGroupData(
	string name
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	name As String _
)
```
  
Visual C++  
---  
```text
public:
RadioButtonGroupData(
	String^ name
)
```
  
# ### Parameters
name
    Type: System..::..StringThe internal name of the RadioButtonGroup.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | Thrown when nullNothingnullptra null reference (Nothing in Visual Basic) is passed for name. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Thrown when an empty string is passed for name. |

# See Also
[RadioButtonGroupData Class](eeda7b4e-226f-b9a2-12d8-6768d295ca4a.md "RadioButtonGroupData Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)