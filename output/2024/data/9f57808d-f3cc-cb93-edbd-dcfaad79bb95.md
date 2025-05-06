# MultipleValuesCustomText Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ScheduleField..::..MultipleValuesCustomText Property   
[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.md "ScheduleField Class") See Also  
---  
The custom multiple values text to be used when the schedule field displays multiple element values, used when [MultipleValuesDisplayType](64592725-4f20-d2a0-010d-220a9315ff39.md "MultipleValuesDisplayType Property") is set to [Custom](cc6f0e5f-958c-8062-2b8f-b443b0fae708.md "ScheduleFieldMultipleValuesDisplayType Enumeration"). 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public string MultipleValuesCustomText { get; set; }
```
  
Visual Basic  
---  
```text
Public Property MultipleValuesCustomText As String
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property String^ MultipleValuesCustomText {
	String^ get ();
	void set (String^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.md "ScheduleField Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 