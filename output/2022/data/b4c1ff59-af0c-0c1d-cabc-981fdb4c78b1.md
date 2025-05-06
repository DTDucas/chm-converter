# Shift Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
FillGrid..::..Shift Property   
[FillGrid Class](6dfc3e2f-c869-d06e-876e-49c4007f7e59.md "FillGrid Class") See Also  
---  
Gets and sets the shift of the fill grid. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public double Shift { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Shift As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double Shift {
	double get ();
	void set (double value);
}
```
  
# ### Field Value
The shift of the fill grid. 
# Remarks
Shift moves the pattern of dashes and spaces along the length of each new parallel line. Shift is ignored if the line is solid. 
# See Also
[FillGrid Class](6dfc3e2f-c869-d06e-876e-49c4007f7e59.md "FillGrid Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 