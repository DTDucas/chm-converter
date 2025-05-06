# IsViewIdValidForPreview Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
DocumentPreviewSettings..::..IsViewIdValidForPreview Method   
[DocumentPreviewSettings Class](e38ea350-9951-ee05-5e3d-ab7f31815fb3.md "DocumentPreviewSettings Class") See Also  
---  
Identifies if the view id is valid as a preview view id. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public bool IsViewIdValidForPreview(
	ElementId viewId
)
```
  
Visual Basic  
---  
```text
Public Function IsViewIdValidForPreview ( _
	viewId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsViewIdValidForPreview(
	ElementId^ viewId
)
```
  
# ### Parameters
viewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The view id. 
# ### Return Value
True if the view id is valid for preview, false otherwise. 
# Remarks
Only graphical views (3d or 2d) are valid for use as a preview view. Other views (such as view templates) will not pass this method. InvalidElementId is accepted by this method as this id means that no special view is set for the preview. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DocumentPreviewSettings Class](e38ea350-9951-ee05-5e3d-ab7f31815fb3.md "DocumentPreviewSettings Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 