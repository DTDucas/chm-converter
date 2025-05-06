# IsValidConceptualConstructionTypeElement Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
MassLevelData..::..IsValidConceptualConstructionTypeElement Method   
[MassLevelData Class](c1e62aaf-b7af-ad0c-60d5-4a1a9c1bed79.md "MassLevelData Class") See Also  
---  
Checks if the ElementId is an acceptable conceptual construction type ElementId for the MassLevelData (Mass Floor). 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public bool IsValidConceptualConstructionTypeElement(
	ElementId id
)
```
  
Visual Basic  
---  
```text
Public Function IsValidConceptualConstructionTypeElement ( _
	id As ElementId _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsValidConceptualConstructionTypeElement(
	ElementId^ id
)
```
  
# ### Parameters
id
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The ElementId to be checked. 
# ### Return Value
True if the ElementId is an acceptable conceptual construction type ElementId, false otherwise. 
# Remarks
In the case that 'conceptualConstructionIsByEnergyData' is true, invalidElementId is also acceptable input. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[MassLevelData Class](c1e62aaf-b7af-ad0c-60d5-4a1a9c1bed79.md "MassLevelData Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 