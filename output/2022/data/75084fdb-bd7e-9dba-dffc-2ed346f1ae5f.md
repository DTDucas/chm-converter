# IsParentViewValidForCallout Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ViewSection..::..IsParentViewValidForCallout Method   
[ViewSection Class](fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.md "ViewSection Class") See Also  
---  
This validator checks that the parent view is appropriate for callout views. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public static bool IsParentViewValidForCallout(
	Document document,
	ElementId parentViewId
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsParentViewValidForCallout ( _
	document As Document, _
	parentViewId As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsParentViewValidForCallout(
	Document^ document, 
	ElementId^ parentViewId
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document which contains the ViewFamilyType and parent view. 
parentViewId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The view in which the new callout will appear. Callouts can be created in FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation, and Detail views. 
# ### Return Value
True if the ViewFamilyType can be used for callout views in the parent view, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ViewSection Class](fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.md "ViewSection Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 