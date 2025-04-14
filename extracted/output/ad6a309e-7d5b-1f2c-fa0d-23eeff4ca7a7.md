# Scale Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AnalysisResultSchema..::..Scale Property   
[AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.md "AnalysisResultSchema Class") See Also  
---  
Multiplier used for displaying diagram or vector values in view. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public double Scale { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Scale As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double Scale {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: scale is zero or negative |

# See Also
[AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.md "AnalysisResultSchema Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)