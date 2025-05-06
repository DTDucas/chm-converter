# UserDefinedMarginX Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
PrintParameters..::..UserDefinedMarginX Property   
[PrintParameters Class](59e6cfe9-b1e8-70c0-814b-ee69c8fca411.md "PrintParameters Class") See Also  
---  
The User defined X value of offset from left bottom corner. Unit is inch. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
[ObsoleteAttribute("This property is obsolete. Use OriginOffsetX instead.")]
public double UserDefinedMarginX { get; set; }
```
  
Visual Basic  
---  
```text
<ObsoleteAttribute("This property is obsolete. Use OriginOffsetX instead.")> _
Public Property UserDefinedMarginX As Double
	Get
	Set
```
  
Visual C++  
---  
```text
[ObsoleteAttribute(L"This property is obsolete. Use OriginOffsetX instead.")]
public:
property double UserDefinedMarginX {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Thrown if PaperPlacement is not Margins and MarginType is not User defined type. |

# See Also
[PrintParameters Class](59e6cfe9-b1e8-70c0-814b-ee69c8fca411.md "PrintParameters Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 