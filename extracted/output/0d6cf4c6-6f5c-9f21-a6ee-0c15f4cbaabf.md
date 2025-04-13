

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RebarHostData..::..IsValidHost Method (Element)  
[RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Identifies whether a given element can host reinforcement. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 

# Syntax

C#  
---  
      
    
    public static bool IsValidHost(
    	[Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) element
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function IsValidHost ( _
    	element As [Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) _
    ) As Boolean  
  
Visual C++  
---  
      
    
    public:
    static bool IsValidHost(
    	[Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md)^ element
    )  
  
#### Parameters

element
    Type: [Autodesk.Revit.DB..::..Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.md) The element to check. 

#### Return Value

True if the input Element can host reinforcement elements, false otherwise. 

# Remarks

Many different elements are allowed to host reinforcement, for example, beams, walls, columns, or parts. Often there are specific restrictions about whether an element can host rebar beyond its type or category. For example, the material type of the element may determine this. Or for parts, the part must have been created from layers that have their role set to Structure. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.md)

[IsValidHost Overload](aaff4dec-529b-0e41-aeb5-e632c4ad084c.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)