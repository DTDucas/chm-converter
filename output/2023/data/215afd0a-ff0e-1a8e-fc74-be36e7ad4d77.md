# Station Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
AlignmentStationLabelOptions..::..Station Property   
[AlignmentStationLabelOptions Class](65682466-07b4-766b-a215-fefcdcfd32ce.md "AlignmentStationLabelOptions Class") See Also  
---  
Specifies the station at which the label will be placed, in Revit internal model units (standard Imperial feet). The station determines the location of the label's origin: [Origin](df8b9dc6-9d36-ac2b-04cf-816d88f039b8.md "Origin Property") by setting it to the closest point on the alignment geometry which corresponds to this station. 
**Namespace:** [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.md "Autodesk.Revit.DB.Infrastructure Namespace")**Assembly:** Autodesk.CivilAlignments.DBApplication (in Autodesk.CivilAlignments.DBApplication.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2021.1 
# Syntax
C#  
---  
```text
public double Station { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Station As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double Station {
	double get ();
	void set (double value);
}
```
  
# See Also
[AlignmentStationLabelOptions Class](65682466-07b4-766b-a215-fefcdcfd32ce.md "AlignmentStationLabelOptions Class")
[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.md "Autodesk.Revit.DB.Infrastructure Namespace")
Send comments on this topic to 