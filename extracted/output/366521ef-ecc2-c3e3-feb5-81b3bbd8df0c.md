

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ParameterValue Class  
[Members](fc18964a-0df5-d477-ca0a-fb0c69d3f152.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
A class that holds a value of a parameter element. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 Subscription Update 

# Syntax

C#  
---  
      
    
    public class ParameterValue : IDisposable  
  
Visual Basic  
---  
      
    
    Public Class ParameterValue _
    	Implements IDisposable  
  
Visual C++  
---  
      
    
    public ref class ParameterValue : IDisposable  
  
# Remarks

This is a non-instantiable base class. Classes that actually store a value of a certain type are all derived from this base class, once class per each value type. 

# Inheritance Hierarchy

System..::..Object Autodesk.Revit.DB..::..ParameterValue [Autodesk.Revit.DB..::..DoubleParameterValue](561ef32b-c3bc-3847-ef2a-27f4a011e650.md) [Autodesk.Revit.DB..::..ElementIdParameterValue](7de25c99-4f85-ef1d-7f64-74092f963c98.md) [Autodesk.Revit.DB..::..IntegerParameterValue](14c16038-74bf-205b-ac93-6ffa6274c034.md) [Autodesk.Revit.DB..::..NullParameterValue](fe10010f-e127-7248-1f17-8c1ee0d41ea0.md) [Autodesk.Revit.DB..::..StringParameterValue](2f79fff4-9773-471a-83f8-5636459bdbe5.md)

# See Also

[ParameterValue Members](fc18964a-0df5-d477-ca0a-fb0c69d3f152.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)