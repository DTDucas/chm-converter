# MajorSegmentIndex Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
RebarShapeDefinitionBySegments..::..MajorSegmentIndex Property   
[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.md "RebarShapeDefinitionBySegments Class") See Also  
---  
Index of a segment that can be considered the most important. Revit attempts to preserve the orientation of this segment when a Rebar instance changes its RebarShape to one with a different number of segments. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public int MajorSegmentIndex { get; set; }
```
  
Visual Basic  
---  
```text
Public Property MajorSegmentIndex As Integer
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property int MajorSegmentIndex {
	int get ();
	void set (int value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: majorSegmentIndex is not between 0 and NumberOfSegments. |

# See Also
[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.md "RebarShapeDefinitionBySegments Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 