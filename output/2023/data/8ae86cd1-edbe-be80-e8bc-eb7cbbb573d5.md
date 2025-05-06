# AddPipeSlope Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PipeSettings..::..AddPipeSlope Method   
[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.md "PipeSettings Class") See Also  
---  
Add a pipe slope value. 
**Namespace:** [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public void AddPipeSlope(
	double slope
)
```
  
Visual Basic  
---  
```text
Public Sub AddPipeSlope ( _
	slope As Double _
)
```
  
Visual C++  
---  
```text
public:
void AddPipeSlope(
	double slope
)
```
  
# ### Parameters
slope
    Type: System..::..Double The pipe slope value. Revit stores the slope value as a percentage (0-100). 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | The given value for slope must be between 0 and 100. Slope value is stored in percentage. e.g. 100 means 100%, and it is 45 degree. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Can not add a pipe slope value that was already added. |

# See Also
[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.md "PipeSettings Class")
[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.md "Autodesk.Revit.DB.Plumbing Namespace")
Send comments on this topic to 