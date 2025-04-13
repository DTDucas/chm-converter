

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
IExportContext Interface  
[Members](00dd06f6-d262-fd7f-5886-6ae200cb64aa.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
An interface that is used in custom export to process a Revit model. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 

# Syntax

C#  
---  
      
    
    public interface IExportContext  
  
Visual Basic  
---  
      
    
    Public Interface IExportContext  
  
Visual C++  
---  
      
    
    public interface class IExportContext  
  
# Remarks

An instance of a class that implements this interface is passed in as a parameter of the [CustomExporter](d2437433-9183-cbb1-1c67-dedd86db5b5a.md) constructor. The methods of the context are then called at times of exporting entities of the model. 

This is a base class for two other interfaces derived from it: [IPhotoRenderContext](d09d4ea2-1090-f2b9-8073-5fb8a796babf.md) and [IModelExportContext](4309af43-f04e-4e42-2539-3fd1d64cdc6d.md). This base class contains methods that are common to both the leaf interfaces. Although it is still possible to use classes deriving directly from this base interface (for backward compatibility), future applications should implement the new leaf interfaces only. 

# See Also

[IExportContext Members](00dd06f6-d262-fd7f-5886-6ae200cb64aa.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)