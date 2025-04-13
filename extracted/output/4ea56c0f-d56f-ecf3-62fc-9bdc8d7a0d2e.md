

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
FormUtils..::..DissolveForms Method (Document, ICollection<(Of <(<'ElementId>)>)>, ICollection<(Of <(<'ElementId>)>)>%)  
[FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Dissolves a collection of form elements into their defining elements. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public static ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> DissolveForms(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) ADoc,
    	ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> elements,
    	out ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> ProfileOriginPointSet
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function DissolveForms ( _
    	ADoc As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	elements As ICollection(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)), _
    	<OutAttribute> ByRef ProfileOriginPointSet As ICollection(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)) _
    ) As ICollection(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md))  
  
Visual C++  
---  
      
    
    public:
    static ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ DissolveForms(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ ADoc, 
    	ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ elements, 
    	[OutAttribute] ICollection<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^% ProfileOriginPointSet
    )  
  
#### Parameters

ADoc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document 

elements
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)>)>)> A collection of element IDs of Forms and GeomCombinations that contain Forms that will be dissolved. 

ProfileOriginPointSet
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)>)>)>% A collection of the point element ids that represent the 'origin' of the profiles 

#### Return Value

A collection of curve element ids from the profiles and paths of the dissolved forms. 

# Remarks

Profile origin points define the workplane of form profiles and paths and their curves. The profile origin point represents a coordinate system with an origin (reference point) which can be manipulated to move the curves of a profile together as a unit after dissolve. Profile origin points may themselves be constrained to other parts of the model or parts of the form, based on how the form was created/constructed. This is done through the reference point hosting mechanism. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | The elements do not include Forms that can be dissolved. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.md)

[DissolveForms Overload](9a152dc3-04f7-aaf2-91a3-2715652ed95d.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)