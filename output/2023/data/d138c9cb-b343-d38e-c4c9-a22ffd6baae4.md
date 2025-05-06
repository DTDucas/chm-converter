# IsElementsDeletionPermitted Method (IList(ElementId), String) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
FailuresAccessor..::..IsElementsDeletionPermitted Method (IList<(Of <(<'ElementId>)>)>, String%)  
[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.md "FailuresAccessor Class") See Also  
---  
Checks if resolution of the failures by deleting given collection of elements is permitted. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public bool IsElementsDeletionPermitted(
	IList<ElementId> idsToDelete,
	out string reason
)
```
  
Visual Basic  
---  
```text
Public Function IsElementsDeletionPermitted ( _
	idsToDelete As IList(Of ElementId), _
	<OutAttribute> ByRef reason As String _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool IsElementsDeletionPermitted(
	IList<ElementId^>^ idsToDelete, 
	[OutAttribute] String^% reason
)
```
  
# ### Parameters
idsToDelete
    Type: System.Collections.Generic..::..IList<(Of <(<'[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.md "ElementId Class")>)>)> The Ids of elements to be deleted. 
reason
    Type: System..::..String% A localized string explaining reason why the elements cannot be deleted. 
# ### Return Value
True if resolution of the failures by deleting given elements is permitted 
# Remarks
Method does not confirm if deletion of the elements will or may resolve the failure - it simply verifies that given elements can be deleted in the current state of the document. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also
[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.md "FailuresAccessor Class")
[IsElementsDeletionPermitted Overload](be9a4660-d27f-f062-060e-347277e7f39a.md "IsElementsDeletionPermitted Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 