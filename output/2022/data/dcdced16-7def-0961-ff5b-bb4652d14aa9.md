# Specification Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
FabricationPart..::..Specification Property   
[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.md "FabricationPart Class") See Also  
---  
The fabrication part specification identifier. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public int Specification { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Specification As Integer
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property int Specification {
	int get ();
	void set (int value);
}
```
  
# Remarks
A value of 0 indicates the specification is set to undefined. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: the specification is invalid for the fabrication part. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | When setting this property: the specification is not able to be modified. -or- When setting this property: the fabrication part is connected to more than one item. -or- When setting this property: the specification fails to be set by identifier: specId. |

# See Also
[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.md "FabricationPart Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 