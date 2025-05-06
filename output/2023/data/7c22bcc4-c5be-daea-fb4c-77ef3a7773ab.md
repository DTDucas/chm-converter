# GetField Method (Int32) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
ScheduleDefinition..::..GetField Method (Int32)  
[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.md "ScheduleDefinition Class") See Also  
---  
Gets a field. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public ScheduleField GetField(
	int index
)
```
  
Visual Basic  
---  
```text
Public Function GetField ( _
	index As Integer _
) As ScheduleField
```
  
Visual C++  
---  
```text
public:
ScheduleField^ GetField(
	int index
)
```
  
# ### Parameters
index
    Type: System..::..Int32 The index of the field. 
# ### Return Value
The field. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | index is not a valid field index in this ScheduleDefinition. |

# See Also
[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.md "ScheduleDefinition Class")
[GetField Overload](6adf5d49-4644-1c45-7c01-573f061e9562.md "GetField Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 