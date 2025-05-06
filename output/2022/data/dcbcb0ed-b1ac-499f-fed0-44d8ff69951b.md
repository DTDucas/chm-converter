# RebarShapeDefinitionByArc Constructor (Document, RebarShapeDefinitionByArcType) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
RebarShapeDefinitionByArc Constructor (Document, RebarShapeDefinitionByArcType)  
[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.md "RebarShapeDefinitionByArc Class") See Also  
---  
Create a non-spiral shape definition. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public RebarShapeDefinitionByArc(
	Document doc,
	RebarShapeDefinitionByArcType type
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	doc As Document, _
	type As RebarShapeDefinitionByArcType _
)
```
  
Visual C++  
---  
```text
public:
RebarShapeDefinitionByArc(
	Document^ doc, 
	RebarShapeDefinitionByArcType type
)
```
  
# ### Parameters
doc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")
type
    Type: [Autodesk.Revit.DB.Structure..::..RebarShapeDefinitionByArcType](555907d2-578b-026a-347c-8900bcf538d8.md "RebarShapeDefinitionByArcType Enumeration")
# Remarks
Replaces RebarShape.NewDefinitionByArc() from prior versions. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The arc type cannot be set directly to Spiral. Instead, call SetArcTypeSpiral() to provide defaults for spiral parameters. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.md "RebarShapeDefinitionByArc Class")
[RebarShapeDefinitionByArc Overload](69c14c72-4c10-1840-014b-b48646d003f1.md "RebarShapeDefinitionByArc Constructor")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 