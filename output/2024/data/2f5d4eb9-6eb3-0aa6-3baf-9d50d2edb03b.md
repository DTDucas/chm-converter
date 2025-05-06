# Rounding Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
AnalysisDisplayDiagramSettings..::..Rounding Property   
[AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.md "AnalysisDisplayDiagramSettings Class") See Also  
---  
Increment to which numeric values of analysis results are rounded in diagram. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public double Rounding { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Rounding As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double Rounding {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.md "ArgumentsInconsistentException Class") | When setting this property: rounding is not positive |

# See Also
[AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.md "AnalysisDisplayDiagramSettings Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 