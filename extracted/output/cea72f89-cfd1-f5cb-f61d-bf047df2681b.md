

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Options..::..View Property   
[Options Class](aa41fc13-9f81-836c-4271-82568ba5d7e8.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The view used for geometry extraction.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public [View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md) View { get; set; }  
  
Visual Basic  
---  
      
    
    Public Property View As [View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)
    	Get
    	Set  
  
Visual C++  
---  
      
    
    public:
    property [View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)^ View {
    	[View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)^ get ();
    	void set ([View](fb92a4e7-f3a7-ef14-e631-342179b18de9.md)^ value);
    }  
  
# Remarks

If a view-specific version of an element exists, it will be extracted in the retrieval of geometry. Also, the detail level of the geometry will be taken from the view's detail level.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | Thrown when setting this property with a nullNothingnullptra null reference (Nothing in Visual Basic). |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Thrown when setting this property, if DetailLevel is already set. When DetailLevel is set view-specific geometry can't be extracted. |
  
# See Also

[Options Class](aa41fc13-9f81-836c-4271-82568ba5d7e8.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)