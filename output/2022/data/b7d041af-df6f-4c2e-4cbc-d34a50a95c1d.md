# IsValidObject Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
LightDistribution..::..IsValidObject Property   
[LightDistribution Class](39162cb5-d13b-c7fa-9297-9a70c5678ac6.md "LightDistribution Class") See Also  
---  
Specifies whether the .NET object represents a valid Revit entity. 
**Namespace:** [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.md "Autodesk.Revit.DB.Lighting Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public bool IsValidObject { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property IsValidObject As Boolean
	Get
```
  
Visual C++  
---  
```text
public:
property bool IsValidObject {
	bool get ();
}
```
  
# ### Return Value
True if the API object holds a valid Revit native object, false otherwise. 
# Remarks
If the corresponding Revit native object is destroyed, or creation of the corresponding object is undone, a managed API object containing it is no longer valid. API methods cannot be called on invalidated wrapper objects. 
# See Also
[LightDistribution Class](39162cb5-d13b-c7fa-9297-9a70c5678ac6.md "LightDistribution Class")
[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.md "Autodesk.Revit.DB.Lighting Namespace")
Send comments on this topic to 