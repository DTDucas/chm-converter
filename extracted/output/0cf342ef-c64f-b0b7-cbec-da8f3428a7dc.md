

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Element..::..GetParameters Method   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Retrieves the parameters from the element via the given name.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015

# Syntax

C#  
---  
      
    
    public IList<[Parameter](333ff41b-e6a7-d959-60bf-c3bfae495581.md)> GetParameters(
    	string name
    )  
  
Visual Basic  
---  
      
    
    Public Function GetParameters ( _
    	name As String _
    ) As IList(Of [Parameter](333ff41b-e6a7-d959-60bf-c3bfae495581.md))  
  
Visual C++  
---  
      
    
    public:
    IList<[Parameter](333ff41b-e6a7-d959-60bf-c3bfae495581.md)^>^ GetParameters(
    	String^ name
    )  
  
#### Parameters

name
    Type: System..::..StringThe name of the parameter to be retrieved.

#### Return Value

A collection containing the parameters having the same given parameter name. 

# Remarks

Multiple matches of parameters with the same name can occur because shared parameters or project parameters can be bound to an element category even if there is a built-in parameter with the same name already. 

If this method is used to find built-in parameters the code will not be portable to other languages of Revit (because built-in parameter names are translated, and this method matches the translation).

For the reasons above this method should be used sparingly and when portability across multiple languages is not a requirement.

Safer approaches include:

  * get_Parameter(Guid) to get a shared parameter by stored guid.
  * get_Parameter(BuiltInParameter) to find a built-in parameter in a language-independent way.



# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)