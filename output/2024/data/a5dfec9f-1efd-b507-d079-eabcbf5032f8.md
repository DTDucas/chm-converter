# ScheduleFilter Class (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ScheduleFilter Class  
[Members](2c2fc999-859e-169b-d958-ee248d9d74b7.md "ScheduleFilter Members") See Also  
---  
A filter in a schedule. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public class ScheduleFilter : IDisposable
```
  
Visual Basic  
---  
```text
Public Class ScheduleFilter _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class ScheduleFilter : IDisposable
```
  
# Remarks
The ScheduleFilter class represents a single filter in a schedule. A filter is a condition that must be satisfied for an element to appear in the schedule. All filters must be satisfied for an element to appear in the schedule.
A schedule can be filtered by data that is not displayed in the schedule by marking the field used for filtering as hidden using the ScheduleField.IsHidden property.
# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB..::..ScheduleFilter
# See Also
[ScheduleFilter Members](2c2fc999-859e-169b-d958-ee248d9d74b7.md "ScheduleFilter Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 