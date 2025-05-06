# EmitLength Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
RectangleLightShape..::..EmitLength Property   
[RectangleLightShape Class](1b9a5edf-d0dc-ce3b-cedd-75c01e431bac.md "RectangleLightShape Class") See Also  
---  
The emit length. 
**Namespace:** [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.md "Autodesk.Revit.DB.Lighting Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public double EmitLength { get; set; }
```
  
Visual Basic  
---  
```text
Public Property EmitLength As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double EmitLength {
	double get ();
	void set (double value);
}
```
  
# ### Field Value
The emit length as a numerical value in feet between 1.0e-9 and 30000.0 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: The shape dimension is not valid because it is not between 1.0e-9 and 30000.0. |

# See Also
[RectangleLightShape Class](1b9a5edf-d0dc-ce3b-cedd-75c01e431bac.md "RectangleLightShape Class")
[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.md "Autodesk.Revit.DB.Lighting Namespace")
Send comments on this topic to 