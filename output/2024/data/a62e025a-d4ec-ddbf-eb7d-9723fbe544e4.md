# CreateMaskingRegion Method (Document, SketchPlane, IList(CurveLoop)) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FilledRegion..::..CreateMaskingRegion Method (Document, SketchPlane, IList<(Of <(<'CurveLoop>)>)>)  
[FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.md "FilledRegion Class") See Also  
---  
Creates a masking region on a sketch plane in a 3d model family. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public static FilledRegion CreateMaskingRegion(
	Document document,
	SketchPlane sketchPlane,
	IList<CurveLoop> boundaries
)
```
  
Visual Basic  
---  
```text
Public Shared Function CreateMaskingRegion ( _
	document As Document, _
	sketchPlane As SketchPlane, _
	boundaries As IList(Of CurveLoop) _
) As FilledRegion
```
  
Visual C++  
---  
```text
public:
static FilledRegion^ CreateMaskingRegion(
	Document^ document, 
	SketchPlane^ sketchPlane, 
	IList<CurveLoop^>^ boundaries
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The family document in which to create the masking region. 
sketchPlane
    Type: [Autodesk.Revit.DB..::..SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.md "SketchPlane Class") The sketch plane for use with the masking region. 
boundaries
    Type: System.Collections.Generic..::..IList<(Of <(<'[CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.md "CurveLoop Class")>)>)> The masking region boundaries, which will be projected onto the sketch plane. 
# ### Return Value
The new masking region. 
# Remarks
If the sketch plane is currently in use, then a copy of the sketch plane will be created and used. The sketch plane normal must be parallel to the model's X, Y or Z axis. The sketch plane can be a planar face reference to model geometry. The line style of the boundaries will be set to thin lines by default. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The document is not a 3d model family. -or- Filled regions can't be created in this document or view. -or- The sketch plane is not suitable for model elements. -or- The sketch plane normal is not parallel to the model's X, Y or Z axis. -or- The input curve loops cannot compose a valid boundary, that means: the "curveLoops" collection is empty; or some curve loops intersect with each other; or each curve loop is not closed individually; or each curve loop is not planar; or each curve loop is not in a plane parallel to the sketch plane; or input curves contain at least one helical curve. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.md "FilledRegion Class")
[CreateMaskingRegion Overload](0b90c4da-38ea-c126-3147-b47bc450695d.md "CreateMaskingRegion Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 