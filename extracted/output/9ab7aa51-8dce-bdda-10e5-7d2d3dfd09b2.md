# IsViewIdValidForViewport Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Viewport..::..IsViewIdValidForViewport Method   
[Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.md "Viewport Class") See Also  
---  
Verifies that the Viewport can change it's view id to the input %viewId%. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2023 
# Syntax
C#  
---  
```text
public bool IsViewIdValidForViewport(
	ElementId viewId
)
```
  
Visual Basic  
---  
```text
Public Function IsViewIdValidForViewport ( _
	viewId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsViewIdValidForViewport(
	ElementId^ viewId
)
```
  
# ### Parameters
viewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The view which will be checked to see if it can be applied to Viewport. 
# ### Return Value
True if the %viewId% is valid for the viewport, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.md "Viewport Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)