# IsVerticallyHomogeneous Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
CompoundStructure..::..IsVerticallyHomogeneous Method   
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class") See Also  
---  
Indicates whether this CompoundStructure represents a single set of parallel layers. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public bool IsVerticallyHomogeneous()
```
  
Visual Basic  
---  
```text
Public Function IsVerticallyHomogeneous As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsVerticallyHomogeneous()
```
  
# ### Return Value
True if this CompoundStructure represents a series of parallel layers that stretch from bottom to top, false otherwise. 
# Remarks
Differs from IsVerticallyCompound as a vertically compound structure might happen not to have any horizontal breaks. For that situation, both IsVerticallyCompound and this method will return true. 
# See Also
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 