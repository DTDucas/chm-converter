# AddCutBetweenSolids Method (Document, Element, Element, Boolean) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
SolidSolidCutUtils..::..AddCutBetweenSolids Method (Document, Element, Element, Boolean)  
[SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.md "SolidSolidCutUtils Class") See Also  
---  
Adds a solid-solid cut for the two elements with the option to control splitting of faces of the cutting solid. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public static void AddCutBetweenSolids(
	Document document,
	Element solidToBeCut,
	Element cuttingSolid,
	bool splitFacesOfCuttingSolid
)
```
  
Visual Basic  
---  
```text
Public Shared Sub AddCutBetweenSolids ( _
	document As Document, _
	solidToBeCut As Element, _
	cuttingSolid As Element, _
	splitFacesOfCuttingSolid As Boolean _
)
```
  
Visual C++  
---  
```text
public:
static void AddCutBetweenSolids(
	Document^ document, 
	Element^ solidToBeCut, 
	Element^ cuttingSolid, 
	bool splitFacesOfCuttingSolid
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document containing the two elements. 
solidToBeCut
    Type: [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") The solid to be cut. 
cuttingSolid
    Type: [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") The cutting solid. 
splitFacesOfCuttingSolid
    Type: System..::..Boolean True to split faces of cutting solid where it intersects the solid to be cut, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The element must be in a project document or in a conceptual model, pattern based curtain panel, or adaptive component family. -or- The element does not meet the condition that it must be solid and must be a GenericForm, GeomCombination, or a FamilyInstance. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Failed to add solid-solid cut for the two elements. |

# See Also
[SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.md "SolidSolidCutUtils Class")
[AddCutBetweenSolids Overload](91f9389e-9a5d-beca-b735-1863ceddeac7.md "AddCutBetweenSolids Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 