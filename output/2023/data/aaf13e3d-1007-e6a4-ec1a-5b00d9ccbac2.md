# StairsPathOffset Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
StairsPath..::..StairsPathOffset Property   
[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md "StairsPath Class") See Also  
---  
The offset of stairs path to center line of stairs. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public double StairsPathOffset { get; set; }
```
  
Visual Basic  
---  
```text
Public Property StairsPathOffset As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double StairsPathOffset {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: The given value for stairsPathOffset is not finite -or- When setting this property: The stairsPathOffset is larger than half the width of the stairs. |

# See Also
[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.md "StairsPath Class")
[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.md "Autodesk.Revit.DB.Architecture Namespace")
Send comments on this topic to 