

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RevitLinkType..::..GetTopLevelLink Method (Document, ModelPath)  
[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Returns the ElementId of the (top-level) linked model with the given path. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 

# Syntax

C#  
---  
      
    
    public static [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md) GetTopLevelLink(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	[ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.md) path
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function GetTopLevelLink ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	path As [ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.md) _
    ) As [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)  
  
Visual C++  
---  
      
    
    public:
    static [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^ GetTopLevelLink(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	[ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.md)^ path
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document to look for the linked model in. 

path
    Type: [Autodesk.Revit.DB..::..ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.md) A path indicating which linked model to return. 

#### Return Value

The id of the link with the given path, or InvalidElementId if there is no top-level link at that path. 

# Remarks

This function will not return nested links. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
  
# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md)

[GetTopLevelLink Overload](473b3f34-b5eb-7900-0a7e-8550cb066b35.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)