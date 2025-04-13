

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
VertexPositionColored Class  
[Members](31438c12-c049-aadb-a375-0b531e897461.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
A geometry vertex specified as a position in space with a color. 

**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public class VertexPositionColored : [Vertex](0434973b-559d-a27f-25f9-f6bf6ef4f750.md)  
  
Visual Basic  
---  
      
    
    Public Class VertexPositionColored _
    	Inherits [Vertex](0434973b-559d-a27f-25f9-f6bf6ef4f750.md)  
  
Visual C++  
---  
      
    
    public ref class VertexPositionColored : public [Vertex](0434973b-559d-a27f-25f9-f6bf6ef4f750.md)  
  
# Remarks

The color of these vertices includes a transparency component In order to render them as transparent they must be rendered in the transparent pass See the 'IsTransparentPass' method of [DrawContext](b9244325-08c8-8bbd-a9f3-5d91d638d85d.md)

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB.DirectContext3D..::..Vertex](0434973b-559d-a27f-25f9-f6bf6ef4f750.md) Autodesk.Revit.DB.DirectContext3D..::..VertexPositionColored

# See Also

[VertexPositionColored Members](31438c12-c049-aadb-a375-0b531e897461.md)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)