# IsLayerValid Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
CompoundStructure..::..IsLayerValid Method   
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class") See Also  
---  
Verifies that the data in this layer is internally consistent. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public bool IsLayerValid(
	int layerIdx,
	CompoundStructureLayer layer
)
```
  
Visual Basic  
---  
```text
Public Function IsLayerValid ( _
	layerIdx As Integer, _
	layer As CompoundStructureLayer _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsLayerValid(
	int layerIdx, 
	CompoundStructureLayer^ layer
)
```
  
# ### Parameters
layerIdx
    Type: System..::..Int32 The index of the layer in the compound structure to be set. 
layer
    Type: [Autodesk.Revit.DB..::..CompoundStructureLayer](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.md "CompoundStructureLayer Class") The layer to be set. 
# ### Return Value
True if the layer is internally consistent, false if the layer is not internally consistent. 
# Remarks
If the layer function is not Membrane or StructuralDeck, the width must be greater than zero. If the layer function is not StructuralDeck, then the deck embedding type must be Invalid, and the deck profile id must be InvalidElementId. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 