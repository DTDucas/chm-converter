# GetWidth Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
CompoundStructure..::..GetWidth Method   
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class") See Also  
---  
The width implied by this compound structure. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public double GetWidth()
```
  
Visual Basic  
---  
```text
Public Function GetWidth As Double
```
  
Visual C++  
---  
```text
public:
double GetWidth()
```
  
# ### Return Value
The width of a host object with this compound structure. 
# Remarks
If the structure is not vertically compound, then this is simply the sum of all layers' widths. If the structure is vertically compound, this is the width of the rectangular grid stored in the vertically compound structure. The presence of a layer with variable width has no effect on the value returned by this method. The value returned assumes that all layers have their specified width. 
# See Also
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md "CompoundStructure Class")
[GetWidth Overload](b131b5cc-f977-51bb-c0ab-be4a5a025b44.md "GetWidth Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 