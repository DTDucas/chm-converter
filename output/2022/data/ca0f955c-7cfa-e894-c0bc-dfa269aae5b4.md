# GetLabelFor Method (BuiltInParameter) (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
LabelUtils..::..GetLabelFor Method (BuiltInParameter)  
[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.md "LabelUtils Class") See Also  
---  
Gets the user-visible name for a BuiltInParameter. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public static string GetLabelFor(
	BuiltInParameter builtInParam
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetLabelFor ( _
	builtInParam As BuiltInParameter _
) As String
```
  
Visual C++  
---  
```text
public:
static String^ GetLabelFor(
	BuiltInParameter builtInParam
)
```
  
# ### Parameters
builtInParam
    Type: [Autodesk.Revit.DB..::..BuiltInParameter](fb011c91-be7e-f737-28c7-3f1e1917a0e0.md "BuiltInParameter Enumeration") The BuiltInParameter to get the user-visible name. 
# Remarks
The name is obtained in the current Revit language. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown when the BuiltInParameter cannot be found. |

# See Also
[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.md "LabelUtils Class")
[GetLabelFor Overload](39e41221-70f9-fae6-53e6-872eff5a2c63.md "GetLabelFor Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 