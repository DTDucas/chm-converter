

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RebarContainerParameterManager Class  
[Members](3d9c1f41-bc7c-1af5-f647-cb96de7318d1.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Provides implementation of RebarContainer parameters overrides. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 

# Syntax

C#  
---  
      
    
    public class RebarContainerParameterManager : IDisposable  
  
Visual Basic  
---  
      
    
    Public Class RebarContainerParameterManager _
    	Implements IDisposable  
  
Visual C++  
---  
      
    
    public ref class RebarContainerParameterManager : IDisposable  
  
# Remarks

When a new override is created, by default, the parameter will show the overridden value as read-only. You can control whether or not the parameter is modifiable using [SetOverriddenParameterReadonly(ElementId)](13dfe73c-aa3c-767d-c939-45feab28cd21.md) and [SetOverriddenParameterModifiable(ElementId)](0b91fcec-09b4-8e89-01cf-24272512395f.md).a 

# Inheritance Hierarchy

System..::..Object Autodesk.Revit.DB.Structure..::..RebarContainerParameterManager

# See Also

[RebarContainerParameterManager Members](3d9c1f41-bc7c-1af5-f647-cb96de7318d1.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)