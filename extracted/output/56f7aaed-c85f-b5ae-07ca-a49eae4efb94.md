# IsCurveLoopsInsideHostBoundaries Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AreaLoad..::..IsCurveLoopsInsideHostBoundaries Method   
[AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.md "AreaLoad Class") See Also  
---  
Checks if contour loops is inside host boundaries. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public static bool IsCurveLoopsInsideHostBoundaries(
	Document doc,
	ElementId hostId,
	IList<CurveLoop> loops
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsCurveLoopsInsideHostBoundaries ( _
	doc As Document, _
	hostId As ElementId, _
	loops As IList(Of CurveLoop) _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsCurveLoopsInsideHostBoundaries(
	Document^ doc, 
	ElementId^ hostId, 
	IList<CurveLoop^>^ loops
)
```
  
# ### Parameters
doc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") Document. 
hostId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The id of the analytical element that is about to host a load 
loops
    Type: System.Collections.Generic..::..IList<(Of <(<'[CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.md "CurveLoop Class")>)>)> CurveLoops to be checked. 
# ### Return Value
Returns true if area load is positioned with entire distribution over the host, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.md "AreaLoad Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)