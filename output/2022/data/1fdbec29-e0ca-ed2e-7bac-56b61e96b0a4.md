# LineLightShape Constructor (Double) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
LineLightShape Constructor (Double)  
[LineLightShape Class](3fce7f00-ae7a-04db-a6e8-dab9794bd6a7.md "LineLightShape Class") See Also  
---  
Creates a line light shape object with the given emit length. 
**Namespace:** [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.md "Autodesk.Revit.DB.Lighting Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public LineLightShape(
	double emitLength
)
```
  
Visual Basic  
---  
```text
Public Sub New ( _
	emitLength As Double _
)
```
  
Visual C++  
---  
```text
public:
LineLightShape(
	double emitLength
)
```
  
# ### Parameters
emitLength
    Type: System..::..Double The emit length as a numerical value in feet between 1.0e-9 and 30000.0 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | The shape dimension is not valid because it is not between 1.0e-9 and 30000.0. |

# See Also
[LineLightShape Class](3fce7f00-ae7a-04db-a6e8-dab9794bd6a7.md "LineLightShape Class")
[LineLightShape Overload](a22b9f7b-92cf-9469-e1ca-9ce442740fee.md "LineLightShape Constructor")
[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.md "Autodesk.Revit.DB.Lighting Namespace")
Send comments on this topic to 