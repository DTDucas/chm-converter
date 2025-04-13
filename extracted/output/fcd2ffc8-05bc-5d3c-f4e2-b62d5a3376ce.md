

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
CompoundStructure..::..GetWidth Method   
[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The width implied by this compound structure. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public double GetWidth()  
  
Visual Basic  
---  
      
    
    Public Function GetWidth As Double  
  
Visual C++  
---  
      
    
    public:
    double GetWidth()  
  
#### Return Value

The width of a host object with this compound structure. 

# Remarks

If the structure is not vertically compound, then this is simply the sum of all layers' widths. If the structure is vertically compound, this is the width of the rectangular grid stored in the vertically compound structure. The presence of a layer with variable width has no effect on the value returned by this method. The value returned assumes that all layers have their specified width. 

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.md)

[GetWidth Overload](b131b5cc-f977-51bb-c0ab-be4a5a025b44.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)