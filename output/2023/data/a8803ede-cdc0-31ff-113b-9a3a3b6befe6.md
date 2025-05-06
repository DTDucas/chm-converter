# SetSurfaceTransparency Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
OverrideGraphicSettings..::..SetSurfaceTransparency Method   
[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.md "OverrideGraphicSettings Class") See Also  
---  
Sets the projection surface transparency. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public OverrideGraphicSettings SetSurfaceTransparency(
	int transparency
)
```
  
Visual Basic  
---  
```text
Public Function SetSurfaceTransparency ( _
	transparency As Integer _
) As OverrideGraphicSettings
```
  
Visual C++  
---  
```text
public:
OverrideGraphicSettings^ SetSurfaceTransparency(
	int transparency
)
```
  
# ### Parameters
transparency
    Type: System..::..Int32 Value of the transparency of the projection surface (0 = opaque, 100 = fully transparent). 
# ### Return Value
Reference to the changed object. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Transparency must be greater than 0 and less than 100. |

# See Also
[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.md "OverrideGraphicSettings Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 