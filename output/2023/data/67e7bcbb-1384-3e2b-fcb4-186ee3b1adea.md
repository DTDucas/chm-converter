# Spacing Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
LayoutRuleClearSpacing..::..Spacing Property   
[LayoutRuleClearSpacing Class](09ba6ef0-6c4d-904a-715a-33755540fd26.md "LayoutRuleClearSpacing Class") See Also  
---  
Get or set the spacing of the beam system. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public double Spacing { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Spacing As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double Spacing {
	double get ();
	void set (double value);
}
```
  
# Remarks
The value of spacing must be in [0, 30000), but in fact the spacing should not be too small or too great.
# See Also
[LayoutRuleClearSpacing Class](09ba6ef0-6c4d-904a-715a-33755540fd26.md "LayoutRuleClearSpacing Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 