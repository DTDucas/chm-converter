

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
GenericForm Class  
[Members](6e55796d-1b8b-8910-550e-5c3db5b56312.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Provides access to the Generic Form model in Autodesk Revit.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public class GenericForm : [CombinableElement](c88bdbbc-dbbb-0817-a358-35f8686f68a2.md)  
  
Visual Basic  
---  
      
    
    Public Class GenericForm _
    	Inherits [CombinableElement](c88bdbbc-dbbb-0817-a358-35f8686f68a2.md)  
  
Visual C++  
---  
      
    
    public ref class GenericForm : public [CombinableElement](c88bdbbc-dbbb-0817-a358-35f8686f68a2.md)  
  
# Remarks

The Generic Form object can be queried for a generic form for use in family modeling and massing. It is the base class of Sweep, Blend, Extrusion, Revolution.

# Inheritance Hierarchy

System..::..Object [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) [Autodesk.Revit.DB..::..CombinableElement](c88bdbbc-dbbb-0817-a358-35f8686f68a2.md) Autodesk.Revit.DB..::..GenericForm [Autodesk.Revit.DB..::..Blend](6875edf6-f0ba-60bc-f294-21bb689c5994.md) [Autodesk.Revit.DB..::..Extrusion](1d8cca8f-0ef5-0cb6-a33b-f044b968cd89.md) [Autodesk.Revit.DB..::..Form](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.md) [Autodesk.Revit.DB..::..FreeFormElement](27b9411a-d368-1541-b7db-b5157a58c581.md) [Autodesk.Revit.DB..::..Revolution](c79a0527-7887-2fdf-3d8a-a7845cbf18a0.md) [Autodesk.Revit.DB..::..Sweep](ed383459-badd-2323-4f73-0d94fd76ce0f.md) [Autodesk.Revit.DB..::..SweptBlend](8e50efa3-fc77-64f1-7c14-4e2089699921.md)

# See Also

[GenericForm Members](6e55796d-1b8b-8910-550e-5c3db5b56312.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)