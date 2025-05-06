# CreateAddInCommandBinding Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
UIApplication..::..CreateAddInCommandBinding Method   
[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.md "UIApplication Class") See Also  
---  
Creates a new AddInCommandBinding.
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013
# Syntax
C#  
---  
```text
public AddInCommandBinding CreateAddInCommandBinding(
	RevitCommandId revitCommandId
)
```
  
Visual Basic  
---  
```text
Public Function CreateAddInCommandBinding ( _
	revitCommandId As RevitCommandId _
) As AddInCommandBinding
```
  
Visual C++  
---  
```text
public:
AddInCommandBinding^ CreateAddInCommandBinding(
	RevitCommandId^ revitCommandId
)
```
  
# ### Parameters
revitCommandId
    Type: [Autodesk.Revit.UI..::..RevitCommandId](0fb2f851-f469-f739-d6ee-89b40b25c4a2.md "RevitCommandId Class")The Revit command id to identify the command handler you want to replace. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | Thrown when uiApplication or revitCommandId is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when the given command already has been bound. |

# See Also
[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.md "UIApplication Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 