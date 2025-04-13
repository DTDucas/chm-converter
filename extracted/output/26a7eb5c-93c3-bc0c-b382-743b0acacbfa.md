

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
DocumentChangedEventArgs..::..GetModifiedElementIds Method (ElementFilter)  
[DocumentChangedEventArgs Class](8fd170b2-df48-209b-438e-54ec7b01b664.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Returns set of elements that were modified according to the given element filter. 

**Namespace:** [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 

# Syntax

C#  
---  
      
    
    public ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> GetModifiedElementIds(
    	[ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md) filter
    )  
  
Visual Basic  
---  
      
    
    Public Function GetModifiedElementIds ( _
    	filter As [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md) _
    ) As ICollection(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md))  
  
Visual C++  
---  
      
    
    public:
    ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ GetModifiedElementIds(
    	[ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md)^ filter
    )  
  
#### Parameters

filter
    Type: [Autodesk.Revit.DB..::..ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.md) The element filter to be applied. 

#### Return Value

The set of ElementId for modified elements that pass the filter. Returns empty set if no elements are found which pass the filter. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[DocumentChangedEventArgs Class](8fd170b2-df48-209b-438e-54ec7b01b664.md)

[GetModifiedElementIds Overload](eb5eab82-7e48-958b-9999-dc8826ca26f3.md)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)