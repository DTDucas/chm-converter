# ShowHeader Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ScheduleSortGroupField..::..ShowHeader Property   
[ScheduleSortGroupField Class](526680eb-ea68-35a7-b0c5-d63459fac04d.md "ScheduleSortGroupField Class") See Also  
---  
Indicates if a header row should be displayed before each group. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public bool ShowHeader { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ShowHeader As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool ShowHeader {
	bool get ();
	void set (bool value);
}
```
  
# ### Field Value
True if a header row should be displayed, false otherwise. 
# Remarks
The header row displays a title consisting of the value of the field that the schedule is grouped by. 
# See Also
[ScheduleSortGroupField Class](526680eb-ea68-35a7-b0c5-d63459fac04d.md "ScheduleSortGroupField Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 