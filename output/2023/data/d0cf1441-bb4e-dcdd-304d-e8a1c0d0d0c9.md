# ConnectorTolerance Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PipeSettings..::..ConnectorTolerance Property   
[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.md "PipeSettings Class") See Also  
---  
The connector tolerance value. 
**Namespace:** [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public double ConnectorTolerance { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ConnectorTolerance As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double ConnectorTolerance {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: The given value for dValue is not finite |

# See Also
[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.md "PipeSettings Class")
[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")
Send comments on this topic to 