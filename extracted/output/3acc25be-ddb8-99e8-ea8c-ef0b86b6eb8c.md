

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Document..::..Print Method (ViewSet)  
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Prints a set of views with default view template and default print settings.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public void Print(
    	[ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.md) views
    )  
  
Visual Basic  
---  
      
    
    Public Sub Print ( _
    	views As [ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.md) _
    )  
  
Visual C++  
---  
      
    
    public:
    void Print(
    	[ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.md)^ views
    )  
  
#### Parameters

views
    Type: [Autodesk.Revit.DB..::..ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.md)The set of views which need to be printed.

# Remarks

If one view in the set can not be printed successfully then an exception will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Thrown when printing is not allowed in the current application mode. Or when at least one view from the view set is not a printable view. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | Thrown when the view set to be printed is nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | Thrown when the view set contains a nullNothingnullptra null reference (Nothing in Visual Basic) element. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Thrown when at least one view from the view set could not be printed. |
| [Autodesk.Revit.Exceptions..::..OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.md) | Thrown when print is cancelled by event handler. |
  
# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)

[Print Overload](e491ce6c-4350-0335-5388-28875da09c7e.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)