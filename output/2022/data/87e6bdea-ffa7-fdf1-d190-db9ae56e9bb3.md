# RevealHiddenElements Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
TemporaryViewModes..::..RevealHiddenElements Property   
[TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.md "TemporaryViewModes Class") See Also  
---  
The current state of the RevealHiddenElements mode in the associated view. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2016 Subscription Update 
# Syntax
C#  
---  
```text
public bool RevealHiddenElements { get; set; }
```
  
Visual Basic  
---  
```text
Public Property RevealHiddenElements As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool RevealHiddenElements {
	bool get ();
	void set (bool value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | When setting this property: The RevealHiddenElements mode is either disabled or inapplicable in the associated view. |

# See Also
[TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.md "TemporaryViewModes Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 