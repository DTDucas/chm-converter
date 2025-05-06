# Save Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PrintSetup..::..Save Method   
[PrintSetup Class](9dc30afc-373c-a532-6c89-ff3fa2b3ceed.md "PrintSetup Class") See Also  
---  
Save the changes for the current print setting.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public bool Save()
```
  
Visual Basic  
---  
```text
Public Function Save As Boolean
```
  
Visual C++  
---  
```text
public:
bool Save()
```
  
# ### Return Value
False if save operation fails, otherwise True.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when the current print setting is In-Session or the current print setting has not changed. |

# See Also
[PrintSetup Class](9dc30afc-373c-a532-6c89-ff3fa2b3ceed.md "PrintSetup Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 