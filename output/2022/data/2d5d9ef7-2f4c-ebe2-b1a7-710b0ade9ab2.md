# GetFlow Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
MechanicalSystem..::..GetFlow Method   
[MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.md "MechanicalSystem Class") See Also  
---  
Gets the flow of this mechanical system. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.md "Autodesk.Revit.DB.Mechanical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public double GetFlow()
```
  
Visual Basic  
---  
```text
Public Function GetFlow As Double
```
  
Visual C++  
---  
```text
public:
double GetFlow()
```
  
# Remarks
The system flow is calculated in the non-blocking evaluation framework. The caller may set up callbacks that react to the asynchronous calculation results. If no callback is set up (e.g, called from third-party applications), the calculation is automatically switched to synchronous calculation so the caller can access the up-to-date result. Similarly, the public method get_ParameterValue(BuiltInParameter.RBS_DUCT_FLOW_PARAM) has the same behavior. Due to this change, the parameter RBS_DUCT_FLOW_PARAM no longer supports dynamic model update. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The flow can not be calculated for this system. |

# See Also
[MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.md "MechanicalSystem Class")
[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.md "Autodesk.Revit.DB.Mechanical Namespace")
Send comments on this topic to 