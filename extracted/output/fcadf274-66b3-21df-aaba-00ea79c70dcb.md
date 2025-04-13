

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
PartUtils..::..CreateParts Method (Document, ICollection<(Of <(<'LinkElementId>)>)>)  
[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new set of parts out of the original elements. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 

# Syntax

C#  
---  
      
    
    public static void CreateParts(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) document,
    	ICollection<[LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md)> hostOrLinkElementIds
    )  
  
Visual Basic  
---  
      
    
    Public Shared Sub CreateParts ( _
    	document As [Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md), _
    	hostOrLinkElementIds As ICollection(Of [LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md)) _
    )  
  
Visual C++  
---  
      
    
    public:
    static void CreateParts(
    	[Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)^ document, 
    	ICollection<[LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md)^>^ hostOrLinkElementIds
    )  
  
#### Parameters

document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) The document containing the elements. 

hostOrLinkElementIds
    Type: System.Collections.Generic..::..ICollection<(Of <(<'[LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.md)>)>)> The elements that parts will be created from. 

# Remarks

Parts will be added to the model after regeneration. To get the ids of the parts created by this method use PartUtils.GetAssociatedParts() with the contents of hostOrLinkElementIds. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | One or more element ids was not permitted for creating parts. HostOrLinkElements should be of a valid category and the ids should be valid and should not already be divided into parts. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md) | The document has no open transaction. |
  
# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.md)

[CreateParts Overload](7d85355b-ef4a-6c00-a2fe-01e6f5a7c4cb.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)