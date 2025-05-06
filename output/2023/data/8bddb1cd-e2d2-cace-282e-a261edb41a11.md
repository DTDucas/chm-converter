# EndSpace Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
BalusterPattern..::..EndSpace Property   
[BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.md "BalusterPattern Class") See Also  
---  
The extra space added after a whole baluster pattern. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2019 
# Syntax
C#  
---  
```text
public double EndSpace { get; set; }
```
  
Visual Basic  
---  
```text
Public Property EndSpace As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double EndSpace {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: The given value for endSpace must be between 0 and 30000 feet. |

# See Also
[BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.md "BalusterPattern Class")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 