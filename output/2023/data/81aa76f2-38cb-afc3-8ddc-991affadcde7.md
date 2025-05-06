# SummaryShowsVerticalHeaders Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PanelScheduleData..::..SummaryShowsVerticalHeaders Property   
[PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.md "PanelScheduleData Class") See Also  
---  
Shows text in the Load Summary section's headers vertically instead of horizontally 
**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public bool SummaryShowsVerticalHeaders { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property SummaryShowsVerticalHeaders As Boolean
	Get
```
  
Visual C++  
---  
```text
public:
property bool SummaryShowsVerticalHeaders {
	bool get ();
}
```
  
# Remarks
Setting this value must go through the appropriate update function (updateVerticalHeadersInSection) 
# See Also
[PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.md "PanelScheduleData Class")
[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md "Autodesk.Revit.DB.Electrical Namespace")
Send comments on this topic to 