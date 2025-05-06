# IsValidTime Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
HVACLoadBuildingType..::..IsValidTime Method   
[HVACLoadBuildingType Class](db7c8da2-260f-94b7-990e-f32ad234ec87.md "HVACLoadBuildingType Class") See Also  
---  
Check if the string can be parsed to a valid time for opening time and closing time. A valid string can be "16:30" or "4:30 PM"; 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018 
# Syntax
C#  
---  
```text
public static bool IsValidTime(
	string hourMinute
)
```
  
Visual Basic  
---  
```text
Public Shared Function IsValidTime ( _
	hourMinute As String _
) As Boolean
```
  
Visual C++  
---  
```text
public:
static bool IsValidTime(
	String^ hourMinute
)
```
  
# ### Parameters
hourMinute
    Type: System..::..String
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[HVACLoadBuildingType Class](db7c8da2-260f-94b7-990e-f32ad234ec87.md "HVACLoadBuildingType Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to 