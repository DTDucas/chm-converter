# Distance Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DividedPath..::..Distance Property   
[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.md "DividedPath Class") See Also  
---  
The distance between points that are distributed along the path according to the selected layout. When the layout is set to 'FixedDistance' this value can be set to desired distance. The measurement type determines how the distance is measured. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public double Distance { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Distance As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double Distance {
	double get ();
	void set (double value);
}
```
  
# Remarks
This does not take into account points obtained by intersections with other elements. When the layout is set to 'None' the distance is the value that would be used by the 'FixedDistance' layout. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: The distance is too small. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | When setting this property: The distance can only be set when the layout of this DividedPath is set to 'FixedDistance' or 'None'. |

# See Also
[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.md "DividedPath Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 