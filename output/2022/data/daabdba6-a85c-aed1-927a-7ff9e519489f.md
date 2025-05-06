# CreateSingleLayerCompoundStructure Method (MaterialFunctionAssignment, Double, ElementId) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
CompoundStructure..::..CreateSingleLayerCompoundStructure Method (MaterialFunctionAssignment, Double, ElementId)  
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class") See Also  
---  
Creates a CompoundStructure containing a single layer. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public static CompoundStructure CreateSingleLayerCompoundStructure(
	MaterialFunctionAssignment layerFunction,
	double width,
	ElementId materialId
)
```
  
Visual Basic  
---  
```text
Public Shared Function CreateSingleLayerCompoundStructure ( _
	layerFunction As MaterialFunctionAssignment, _
	width As Double, _
	materialId As ElementId _
) As CompoundStructure
```
  
Visual C++  
---  
```text
public:
static CompoundStructure^ CreateSingleLayerCompoundStructure(
	MaterialFunctionAssignment layerFunction, 
	double width, 
	ElementId^ materialId
)
```
  
# ### Parameters
layerFunction
    Type: [Autodesk.Revit.DB..::..MaterialFunctionAssignment](1cbeb006-f7a2-f6d2-491f-faa0b9a006fc.md "MaterialFunctionAssignment Enumeration") The function of the single layer. 
width
    Type: System..::..Double The width of the single layer. 
materialId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class") The ElementId of the material for the single layer. 
# ### Return Value
The newly created compound structure. 
# Remarks
It is not verified that materialId corresponds to a valid Material element. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | The given value for width must be greater than 0 and no more than 30000 feet. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class")
[CreateSingleLayerCompoundStructure Overload](a21f3c6f-4c25-43b7-3714-75eab33db398.md "CreateSingleLayerCompoundStructure Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 