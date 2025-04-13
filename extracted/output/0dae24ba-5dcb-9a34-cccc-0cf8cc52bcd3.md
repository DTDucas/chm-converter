

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ViewSchedule Class  
[Members](b7a752f8-9f04-31dc-80f2-0086f24ed020.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
A schedule view. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 

# Syntax

C#  
---  
      
    
    public class ViewSchedule : [TableView](ba608411-21af-e924-2aa2-3595548ab39f.md)  
  
Visual Basic  
---  
      
    
    Public Class ViewSchedule _
    	Inherits [TableView](ba608411-21af-e924-2aa2-3595548ab39f.md)  
  
Visual C++  
---  
      
    
    public ref class ViewSchedule : public [TableView](ba608411-21af-e924-2aa2-3595548ab39f.md)  
  
# Remarks

The ViewSchedule class represents schedules and other schedule-like views, including single-category and multi-category schedules, key schedules, material takeoffs, view lists, sheet lists, keynote legends, revision schedules, and note blocks. The ViewSchedule class is not used for panel schedules (see PanelScheduleView) or graphical column schedules.

A schedule is a tabular representation of data. A typical schedule shows all elements of a category (doors, rooms, etc.) with each row representing an element and each column representing a parameter. This basic structure can be modified using filters, sorting, grouping, totals, formulas, and other features.

The ScheduleDefinition class contains most settings that determine the contents of a schedule, including category, fields, filters, and sorting.

A graphical representation of a schedule can be placed on a sheet using the ScheduleSheetInstance class.

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) [Autodesk.Revit.DB..::..View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) [Autodesk.Revit.DB..::..TableView](ba608411-21af-e924-2aa2-3595548ab39f.md) Autodesk.Revit.DB..::..ViewSchedule

# See Also

[ViewSchedule Members](b7a752f8-9f04-31dc-80f2-0086f24ed020.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)