# DivisionRuleId Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PartMakerMethodToDivideVolumes..::..DivisionRuleId Property   
[PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.md "PartMakerMethodToDivideVolumes Class") See Also  
---  
Id of the 'DivisionRule' which is used to augment the cutting sketch. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public ElementId DivisionRuleId { get; set; }
```
  
Visual Basic  
---  
```text
Public Property DivisionRuleId As ElementId
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ElementId^ DivisionRuleId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: The provided element id cannot be assigned as a division rule to this PartMakerMethodToDivideVolumes. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.md "PartMakerMethodToDivideVolumes Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 