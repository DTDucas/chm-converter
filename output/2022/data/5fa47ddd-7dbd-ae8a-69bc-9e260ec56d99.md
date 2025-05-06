# Create Method (Document, IList(XYZ), IList(PolymeshFacet)) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
TopographySurface..::..Create Method (Document, IList<(Of <(<'XYZ>)>)>, IList<(Of <(<'PolymeshFacet>)>)>)  
[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.md "TopographySurface Class") See Also  
---  
Creates a new topography surface element from facets and adds it to the document. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2019.2 
# Syntax
C#  
---  
```text
public static TopographySurface Create(
	Document document,
	IList<XYZ> points,
	IList<PolymeshFacet> facets
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	points As IList(Of XYZ), _
	facets As IList(Of PolymeshFacet) _
) As TopographySurface
```
  
Visual C++  
---  
```text
public:
static TopographySurface^ Create(
	Document^ document, 
	IList<XYZ^>^ points, 
	IList<PolymeshFacet^>^ facets
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document to be modified. 
points
    Type: System.Collections.Generic..::..IList<(Of <(<'[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md "XYZ Class")>)>)> A collection of points. The points represent an enclosed area in the XY plane. 
facets
    Type: System.Collections.Generic..::..IList<(Of <(<'[PolymeshFacet](a7315aaf-631d-96af-368c-65f86b6c00ef.md "PolymeshFacet Class")>)>)> Triangle facets composing a polygon mesh. Every facet contains 3 integers representing vertex indices. 
# ### Return Value
The new topography surface. 
# Remarks
The document will be regenerated during the creation of this topography surface element. The topography surface created by facet cannot modify its triangle points and facets. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | document is not a project document. -or- There are invalid facets. Facets with more than two points with same x, y are not allowed. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md "ModificationForbiddenException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md "ModificationOutsideTransactionException Class") | The document has no open transaction. |

# See Also
[TopographySurface Class](64242f41-69e1-84be-f21b-84783e81364a.md "TopographySurface Class")
[Create Overload](7951a6bc-55e8-14bf-c8dc-47ee4a463165.md "Create Method")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 