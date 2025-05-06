# ViewSchedule Class (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ViewSchedule Class  
[Members](b7a752f8-9f04-31dc-80f2-0086f24ed020.md "ViewSchedule Members") See Also  
---  
A schedule view. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public class ViewSchedule : TableView
```
  
Visual Basic  
---  
```text
Public Class ViewSchedule _
	Inherits TableView
```
  
Visual C++  
---  
```text
public ref class ViewSchedule : public TableView
```
  
# Remarks
The ViewSchedule class represents schedules and other schedule-like views, including single-category and multi-category schedules, key schedules, material takeoffs, view lists, sheet lists, keynote legends, revision schedules, and note blocks. The ViewSchedule class is not used for panel schedules (see PanelScheduleView) or graphical column schedules.
A schedule is a tabular representation of data. A typical schedule shows all elements of a category (doors, rooms, etc.) with each row representing an element and each column representing a parameter. This basic structure can be modified using filters, sorting, grouping, totals, formulas, and other features.
The ScheduleDefinition class contains most settings that determine the contents of a schedule, including category, fields, filters, and sorting.
A graphical representation of a schedule can be placed on a sheet using the ScheduleSheetInstance class.
# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") [Autodesk.Revit.DB..::..View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md "View Class") [Autodesk.Revit.DB..::..TableView](ba608411-21af-e924-2aa2-3595548ab39f.md "TableView Class") Autodesk.Revit.DB..::..ViewSchedule
# See Also
[ViewSchedule Members](b7a752f8-9f04-31dc-80f2-0086f24ed020.md "ViewSchedule Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 