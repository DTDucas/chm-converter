# OverrideResult Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DialogBoxData..::..OverrideResult Method   
[DialogBoxData Class](41f22b16-a68b-8c19-53f6-de079feb756c.md "DialogBoxData Class") See Also  
---  
Call this method to cause the Autodesk Revit dialog to be dismissed with the specified return value. 
**Namespace:** [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.md "Autodesk.Revit.UI.Events Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public bool OverrideResult(
	int result
)
```
  
Visual Basic  
---  
```text
Public Function OverrideResult ( _
	result As Integer _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool OverrideResult(
	int result
)
```
  
# ### Parameters
result
    Type: System..::..Int32 The result code you wish the Revit dialog to return. 
# ### Return Value
Returns true if the result code was accepted. 
# See Also
[DialogBoxData Class](41f22b16-a68b-8c19-53f6-de079feb756c.md "DialogBoxData Class")
[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.md "Autodesk.Revit.UI.Events Namespace")
Send comments on this topic to 