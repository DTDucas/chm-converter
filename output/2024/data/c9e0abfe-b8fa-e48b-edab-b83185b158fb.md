# IsEmpty Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
MassLevelData..::..IsEmpty Method   
[MassLevelData Class](c1e62aaf-b7af-ad0c-60d5-4a1a9c1bed79.md "MassLevelData Class") See Also  
---  
Indicates if the MassLevelData (Mass Floor) has a geometrical representation. May not if the level does not intersect the mass geometry. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public bool IsEmpty()
```
  
Visual Basic  
---  
```text
Public Function IsEmpty As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsEmpty()
```
  
# ### Return Value
Returns True if MassLevelData is dimensionless, False otherwise. 
# See Also
[MassLevelData Class](c1e62aaf-b7af-ad0c-60d5-4a1a9c1bed79.md "MassLevelData Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 