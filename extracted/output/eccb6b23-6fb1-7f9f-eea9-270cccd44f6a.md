# MarkerSize Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AnalysisDisplayMarkersAndTextSettings..::..MarkerSize Property   
[AnalysisDisplayMarkersAndTextSettings Class](bb940def-7483-32c6-01cb-1c79e6666290.md "AnalysisDisplayMarkersAndTextSettings Class") See Also  
---  
Size of marker. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public double MarkerSize { get; set; }
```
  
Visual Basic  
---  
```text
Public Property MarkerSize As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double MarkerSize {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.md "ArgumentsInconsistentException Class") | When setting this property: markerSize is negative |

# See Also
[AnalysisDisplayMarkersAndTextSettings Class](bb940def-7483-32c6-01cb-1c79e6666290.md "AnalysisDisplayMarkersAndTextSettings Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)