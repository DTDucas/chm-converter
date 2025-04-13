

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
DirectShapeType..::..SetOptions Method   
[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Sets the options to use for this DirectShapeType. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021 

# Syntax

C#  
---  
      
    
    public void SetOptions(
    	[DirectShapeTypeOptions](ce6d1f15-bceb-5ad2-f3d1-d93f0447da44.md) options
    )  
  
Visual Basic  
---  
      
    
    Public Sub SetOptions ( _
    	options As [DirectShapeTypeOptions](ce6d1f15-bceb-5ad2-f3d1-d93f0447da44.md) _
    )  
  
Visual C++  
---  
      
    
    public:
    void SetOptions(
    	[DirectShapeTypeOptions](ce6d1f15-bceb-5ad2-f3d1-d93f0447da44.md)^ options
    )  
  
#### Parameters

options
    Type: [Autodesk.Revit.DB..::..DirectShapeTypeOptions](ce6d1f15-bceb-5ad2-f3d1-d93f0447da44.md) Options to use for this DirectShapeType. 

# Remarks

The new options take effect immediately. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The DirectShapeTypeOptions provided are not valid for this DirectShapeType. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)