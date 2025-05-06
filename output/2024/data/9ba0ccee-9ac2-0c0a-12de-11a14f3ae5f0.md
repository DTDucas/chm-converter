# BaseElevation Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
StairsRun..::..BaseElevation Property   
[StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.md "StairsRun Class") See Also  
---  
The base elevation of the stairs run. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public double BaseElevation { get; set; }
```
  
Visual Basic  
---  
```text
Public Property BaseElevation As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double BaseElevation {
	double get ();
	void set (double value);
}
```
  
# Remarks
The base elevation has following restrictions: 
  * The base elevation is relative to the base elevation of the stairs to which the stairs run belongs.
  * When setting this property the value will be rounded automatically to a multiple of the riser height.
  * When setting this property for common run, the run's height will change according to the new base/top elevation. So the value must be less than the top elevation to keep run valid.
  * When setting this property for sketched run, whose height is fixed, the run's top elevation will be adjusted to keep the same run height.

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: The given value for baseElevation must be no more than 30000 feet in absolute value. -or- When setting this property: The baseElevation doesn't meet the restriction that bottom of run should not be lower than bottom of stairs. -or- When setting this property: The baseElevation doesn't meet the minimal height restriction of the stairs run. -or- When setting this property: The baseElevation impacts the top elevation which is less than extension below base. |

# See Also
[StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.md "StairsRun Class")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 