

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
PlumbingUtils..::..HasOpenConnector Method   
[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Checks if there is open piping connector for the given element - object of pipe curve, pipe fitting or pipe accessory. 

**Namespace:** [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 

# Syntax

C#  
---  
      
    
    public static bool HasOpenConnector(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) elemId
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function HasOpenConnector ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	elemId As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) _
    ) As Boolean  
  
Visual C++  
---  
      
    
    public:
    static bool HasOpenConnector(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ elemId
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document. 

elemId
    Type: [Autodesk.Revit.DB..::..ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) Element id to check. 

#### Return Value

True if given element has open piping connector, false otherwise. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.md)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)