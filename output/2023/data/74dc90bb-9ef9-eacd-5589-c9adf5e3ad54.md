# OwnerId Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
AnalyticalLink..::..OwnerId Property   
[AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.md "AnalyticalLink Class") See Also  
---  
ElementId of Analytical Element which created the AnalyticalLink (if any) invalidElementId if this Analytical Link was created by the User or API 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public ElementId OwnerId { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property OwnerId As ElementId
	Get
```
  
Visual C++  
---  
```text
public:
property ElementId^ OwnerId {
	ElementId^ get ();
}
```
  
# See Also
[AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.md "AnalyticalLink Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 