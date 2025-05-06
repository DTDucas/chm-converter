# GetSecondProfileCurve Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RuledSurface..::..GetSecondProfileCurve Method   
[RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.md "RuledSurface Class") See Also  
---  
Returns a copy of the second profile curve if it is set. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public Curve GetSecondProfileCurve()
```
  
Visual Basic  
---  
```text
Public Function GetSecondProfileCurve As Curve
```
  
Visual C++  
---  
```text
public:
Curve^ GetSecondProfileCurve()
```
  
# ### Return Value
A copy of the second profile curve, if it exists. If a point was used to define the second profile, this function will return nullNothingnullptra null reference (Nothing in Visual Basic). 
# See Also
[RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.md "RuledSurface Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 