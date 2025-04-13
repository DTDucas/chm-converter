

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
IndexStreamPoint..::..AddPoint Method   
[IndexStreamPoint Class](b2ab0423-2e31-d5a2-ef70-197ca1bf9687.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Inserts a [IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md) into the stream and associated buffer. 

**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public void AddPoint(
    	[IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md) point
    )  
  
Visual Basic  
---  
      
    
    Public Sub AddPoint ( _
    	point As [IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md) _
    )  
  
Visual C++  
---  
      
    
    public:
    void AddPoint(
    	[IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md)^ point
    )  
  
#### Parameters

point
    Type: [Autodesk.Revit.DB.DirectContext3D..::..IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.md) The point to be inserted. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Thrown if the associated buffer is not mapped. -or- Thrown if the associated buffer has insufficient space. |
  
# See Also

[IndexStreamPoint Class](b2ab0423-2e31-d5a2-ef70-197ca1bf9687.md)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)