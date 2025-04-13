

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RevisionSettings..::..RevisionCloudSpacing Property   
[RevisionSettings Class](599f75fc-d2b6-63b3-7295-0c314415b638.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Determines the size in paper space of revision clouds drawn in a project. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 

# Syntax

C#  
---  
      
    
    public double RevisionCloudSpacing { get; set; }  
  
Visual Basic  
---  
      
    
    Public Property RevisionCloudSpacing As Double
    	Get
    	Set  
  
Visual C++  
---  
      
    
    public:
    property double RevisionCloudSpacing {
    	double get ();
    	void set (double value);
    }  
  
# Remarks

Revision clouds in Revit are created based on a collection of sketched lines. Revit then generates a series of "cloud bumps" along those lines to create a cloud shape. This setting determines the minimum length between the start and end each "cloud bump" (measured along the line). For example, if this setting were 2" and the sketched line were 3" long, Revit would create only one 3" bump. If the line length was increased to 4", Revit would add two 2" ones. Note that a single "cloud bump" consists of two arcs of slightly different size. Revit will always draw at least one "cloud bump" for each sketched line. 

This value will be interpreted by Revit in paper space rather than in model space so that all of the clouds are shown in a uniform way on a sheet. 

This value will be rounded to a length that can be displayed according to the current project settings. The value may not be zero after rounding. This value may not exceed the maximum distance that can be represented as a length in Revit.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | When setting this property: desiredCloudSpacing is not a valid value for the cloud spacing. |
  
# See Also

[RevisionSettings Class](599f75fc-d2b6-63b3-7295-0c314415b638.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)