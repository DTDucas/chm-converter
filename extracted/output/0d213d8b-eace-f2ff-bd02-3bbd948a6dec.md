

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ITransientElementMaker Interface  
[Members](ca5ba0a1-1e7a-e60d-576d-40344ce6cc78.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The interface to be implemented by an application that creates transient element(s) in Revit. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 

# Syntax

C#  
---  
      
    
    public interface ITransientElementMaker  
  
Visual Basic  
---  
      
    
    Public Interface ITransientElementMaker  
  
Visual C++  
---  
      
    
    public interface class ITransientElementMaker  
  
# Remarks

An instance of the implemented interface is passed as an argument to the Document.MakeTransientElements() method, which will call back the Execute method of the interface.

During the execution of the method Revit will allow creation of certain elements, such as DirectShape, and will make them automatically transient . See ([IsTransient](f391d235-555f-6651-99c6-895fc443f8d8.md) for more details about transient elements.)

The code within the Execute method is not allowed to modify the model in any other way. An attempt to change the model or create elements of other kinds will result in an exception. This indirectly means that methods using a transaction internally are not allowed either. Such methods include document Save and SaveAs, certain import and export methods, creating links, syncing with central, etc.

Regenerating the model is also not allowed for the entire duration of the Execute method.

This interface is passed to [MakeTransientElements(ITransientElementMaker)](0decdddc-ae4a-d46d-d141-9d37e7973e05.md) which does the actual transient element creation.

# See Also

[ITransientElementMaker Members](ca5ba0a1-1e7a-e60d-576d-40344ce6cc78.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)