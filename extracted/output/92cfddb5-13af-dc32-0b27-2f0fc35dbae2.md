# RowHeightOverride Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ViewSchedule..::..RowHeightOverride Property   
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md "ViewSchedule Class") See Also  
---  
Defines the override that is applied to the row height. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public RowHeightOverrideOptions RowHeightOverride { get; set; }
```
  
Visual Basic  
---  
```text
Public Property RowHeightOverride As RowHeightOverrideOptions
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property RowHeightOverrideOptions RowHeightOverride {
	RowHeightOverrideOptions get ();
	void set (RowHeightOverrideOptions value);
}
```
  
# ### Field Value
  * [None](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md "RowHeightOverrideOptions Enumeration") to disable row height override.
  * [All](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md "RowHeightOverrideOptions Enumeration") enables row height override for all the body rows in the schedule.
  * [ImageRows](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md "RowHeightOverrideOptions Enumeration") enables row height override for all the schedule body rows that contains images or custom graphics.

# Remarks
Setting this property to anything but [None](3f75752e-c4df-90c9-e296-ac604f8c4fd9.md "RowHeightOverrideOptions Enumeration") will allow setting the [RowHeight](aca396e1-2fec-666c-005d-7e36d5153999.md "RowHeight Property") property. This is taken into account when the schedule is viewed as a ScheduleSheetInstance on a ViewSheet.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md "ViewSchedule Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)