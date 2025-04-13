

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
FailuresAccessor..::..IsElementsDeletionPermitted Method (IList<(Of <(<'ElementId>)>)>, String%)  
[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Checks if resolution of the failures by deleting given collection of elements is permitted. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 

# Syntax

C#  
---  
      
    
    public bool IsElementsDeletionPermitted(
    	IList<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)> idsToDelete,
    	out string reason
    )  
  
Visual Basic  
---  
      
    
    Public Function IsElementsDeletionPermitted ( _
    	idsToDelete As IList(Of [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)), _
    	<OutAttribute> ByRef reason As String _
    ) As Boolean  
  
Visual C++  
---  
      
    
    public:
    bool IsElementsDeletionPermitted(
    	IList<[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)^>^ idsToDelete, 
    	[OutAttribute] String^% reason
    )  
  
#### Parameters

idsToDelete
    Type: System.Collections.Generic..::..IList<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md)>)>)> The Ids of elements to be deleted. 

reason
    Type: System..::..String% A localized string explaining reason why the elements cannot be deleted. 

#### Return Value

True if resolution of the failures by deleting given elements is permitted 

# Remarks

Method does not confirm if deletion of the elements will or may resolve the failure - it simply verifies that given elements can be deleted in the current state of the document. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | This FailuresAccessor is inactive (is used outside of failures processing). |
  
# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.md)

[IsElementsDeletionPermitted Overload](be9a4660-d27f-f062-060e-347277e7f39a.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)