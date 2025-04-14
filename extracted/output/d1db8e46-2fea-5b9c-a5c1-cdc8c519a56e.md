# GetHostIds Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
WallSweep..::..GetHostIds Method   
[WallSweep Class](8edb03ef-dc10-04d8-d8ea-6342e4a2185b.md "WallSweep Class") See Also  
---  
Gets a list of all host walls on which the sweep resides. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public IList<ElementId> GetHostIds()
```
  
Visual Basic  
---  
```text
Public Function GetHostIds As IList(Of ElementId)
```
  
Visual C++  
---  
```text
public:
IList<ElementId^>^ GetHostIds()
```
  
# ### Return Value
The list of wall ids. 
# Remarks
Fixed wall sweeps from vertically compound structures will return only one host element. 
# See Also
[WallSweep Class](8edb03ef-dc10-04d8-d8ea-6342e4a2185b.md "WallSweep Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)