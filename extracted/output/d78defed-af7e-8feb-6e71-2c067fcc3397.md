

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RebarShape..::..GetEndTreatmentTypeId Method   
[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Gets the id of the EndTreatmentType at the specified rebar shape end. 

**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 

# Syntax

C#  
---  
      
    
    public [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) GetEndTreatmentTypeId(
    	int iEnd
    )  
  
Visual Basic  
---  
      
    
    Public Function GetEndTreatmentTypeId ( _
    	iEnd As Integer _
    ) As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)  
  
Visual C++  
---  
      
    
    public:
    [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ GetEndTreatmentTypeId(
    	int iEnd
    )  
  
#### Parameters

iEnd
    Type: System..::..Int32 0 for the start end treatment, 1 for the end end treatment. 

#### Return Value

Returns the id of an EndTreatmentType, or invalidElementId if the rebar shape has no end treatment at the specified end. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | iEnd not a valid shape end |
  
# See Also

[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.md)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)