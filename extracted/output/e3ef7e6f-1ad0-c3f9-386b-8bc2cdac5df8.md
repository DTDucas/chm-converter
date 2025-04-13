

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ViewSchedule..::..ImageRowHeight Property   
[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Defines the image row height in the schedule. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 

# Syntax

C#  
---  
      
    
    [ObsoleteAttribute("This property is deprecated in Revit 2024 and my be removed in a later version of Revit. We suggest you use the 'RowHeight' property instead.")]
    public double ImageRowHeight { get; set; }  
  
Visual Basic  
---  
      
    
    <ObsoleteAttribute("This property is deprecated in Revit 2024 and my be removed in a later version of Revit. We suggest you use the 'RowHeight' property instead.")> _
    Public Property ImageRowHeight As Double
    	Get
    	Set  
  
Visual C++  
---  
      
    
    [ObsoleteAttribute(L"This property is deprecated in Revit 2024 and my be removed in a later version of Revit. We suggest you use the 'RowHeight' property instead.")]
    public:
    property double ImageRowHeight {
    	double get ();
    	void set (double value);
    }  
  
#### Field Value

The row height for any rows containing images in the schedule. The value is 0.0 by default if not customized. 

# Remarks

If there is at least one image field in the schedule, then setting this property will force all rows containing images to be resized to the indicated height value (when viewed as a ScheduleSheetInstance on a ViewSheet). Setting this property will have no effect if HasImageField returns false. 

This height will be maintained until the user or application restores the original image sizes (in API: [RestoreImageSize()()()()](e9c47953-6070-46ac-5d24-cef0a9cd5b51.md)). 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | When setting this property: The given value for imageRowHeight must be greater than 0 and no more than 30000 feet. |
  
# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)