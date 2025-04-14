# ComputeRawParameter Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Curve..::..ComputeRawParameter Method   
[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class") See Also  
---  
Computes the raw parameter from the normalized parameter.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public double ComputeRawParameter(
	double normalizedParameter
)
```
  
Visual Basic  
---  
```text
Public Function ComputeRawParameter ( _
	normalizedParameter As Double _
) As Double
```
  
Visual C++  
---  
```text
public:
double ComputeRawParameter(
	double normalizedParameter
)
```
  
# ### Parameters
normalizedParameter
    Type: System..::..DoubleThe normalized parameter.
# ### Return Value
The real number equal to the raw curve parameter.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Thrown when normalizedParameter is infinite. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when the curve is unbound. |

# See Also
[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.md "Curve Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)