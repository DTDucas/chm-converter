# DoubleClickAction Enumeration

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DoubleClickAction Enumeration  
See Also  
---  
Possible actions Revit can take in response to the user double-clicking on an element. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 **Since:** 2016 
# Syntax
C#  
---  
```text
public enum DoubleClickAction
```
  
Visual Basic  
---  
```text
Public Enumeration DoubleClickAction
```
  
Visual C++  
---  
```text
public enum class DoubleClickAction
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| NoAction | Double-clicks should be ignored. |
| EditFamily | Double-click should open the family for editing. |
| EditType | Double-click should take the user to the edit type dialog. |
| ActivateView | Double-click should activate the view or schedule. |
| EnterEditMode | Double-click will enter a specific edit mode for the element. |
| DeactivateView | Double-click should deactivate the active view. |

# See Also
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)