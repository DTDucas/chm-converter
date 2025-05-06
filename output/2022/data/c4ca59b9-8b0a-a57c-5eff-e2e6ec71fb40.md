# DivisionGap Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
PartMakerMethodToDivideVolumes..::..DivisionGap Property   
[PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.md "PartMakerMethodToDivideVolumes Class") See Also  
---  
The gap which is created between matching profiles of parts. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public double DivisionGap { get; set; }
```
  
Visual Basic  
---  
```text
Public Property DivisionGap As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double DivisionGap {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: The given value for divisionGap must be between 0 and 30000 feet. |

# See Also
[PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.md "PartMakerMethodToDivideVolumes Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 