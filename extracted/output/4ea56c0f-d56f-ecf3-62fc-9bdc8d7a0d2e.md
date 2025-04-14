# DissolveForms Method (Document, ICollection(ElementId), ICollection(ElementId))

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FormUtils..::..DissolveForms Method (Document, ICollection<(Of <(<'ElementId>)>)>, ICollection<(Of <(<'ElementId>)>)>%)  
[FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.md "FormUtils Class") See Also  
---  
Dissolves a collection of form elements into their defining elements. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public static ICollection<ElementId> DissolveForms(
	Document ADoc,
	ICollection<ElementId> elements,
	out ICollection<ElementId> ProfileOriginPointSet
)
```
  
Visual Basic  
---  
```text
Public Shared Function DissolveForms ( _
	ADoc As Document, _
	elements As ICollection(Of ElementId), _
	<OutAttribute> ByRef ProfileOriginPointSet As ICollection(Of ElementId) _
) As ICollection(Of ElementId)
```
  
Visual C++  
---  
```text
public:
static ICollection<ElementId^>^ DissolveForms(
	Document^ ADoc, 
	ICollection<ElementId^>^ elements, 
	[OutAttribute] ICollection<ElementId^>^% ProfileOriginPointSet
)
```
  
# ### Parameters
ADoc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document 
elements
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> A collection of element IDs of Forms and GeomCombinations that contain Forms that will be dissolved. 
ProfileOriginPointSet
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)>% A collection of the point element ids that represent the 'origin' of the profiles 
# ### Return Value
A collection of curve element ids from the profiles and paths of the dissolved forms. 
# Remarks
Profile origin points define the workplane of form profiles and paths and their curves. The profile origin point represents a coordinate system with an origin (reference point) which can be manipulated to move the curves of a profile together as a unit after dissolve. Profile origin points may themselves be constrained to other parts of the model or parts of the form, based on how the form was created/constructed. This is done through the reference point hosting mechanism. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The elements do not include Forms that can be dissolved. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.md "FormUtils Class")
[DissolveForms Overload](9a152dc3-04f7-aaf2-91a3-2715652ed95d.md "DissolveForms Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)