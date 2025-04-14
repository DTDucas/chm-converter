# IsValidDefaultTemplate Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ViewFamilyType..::..IsValidDefaultTemplate Method   
[ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.md "ViewFamilyType Class") See Also  
---  
Verifies that the input can be used as a default template for this view type. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public bool IsValidDefaultTemplate(
	ElementId templateId
)
```
  
Visual Basic  
---  
```text
Public Function IsValidDefaultTemplate ( _
	templateId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsValidDefaultTemplate(
	ElementId^ templateId
)
```
  
# ### Parameters
templateId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") Id to be validated as default template. 
# ### Return Value
True if %templateId% is valid as default template, false otherwise. 
# Remarks
The id must represent a template view that is compatible with this view type, or InvalidElementId. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.md "ViewFamilyType Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)