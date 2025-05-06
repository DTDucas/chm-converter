# ExportMullions Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
EnergyAnalysisDetailModelOptions..::..ExportMullions Property   
[EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.md "EnergyAnalysisDetailModelOptions Class") See Also  
---  
Indicates if to specify the setting for exporting mullions. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public bool ExportMullions { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ExportMullions As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool ExportMullions {
	bool get ();
	void set (bool value);
}
```
  
# Remarks
When this setting is on, mullions will be exported as shading surfaces. A "simplified" analytical shading surface is produced from a mullion based on its centerline, thickness and offset. 
# See Also
[EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.md "EnergyAnalysisDetailModelOptions Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 