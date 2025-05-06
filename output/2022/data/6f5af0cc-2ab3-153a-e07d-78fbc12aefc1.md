# SetAllowVaryBetweenGroups Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
InternalDefinition..::..SetAllowVaryBetweenGroups Method   
[InternalDefinition Class](97f42435-3067-622e-7a34-919f42f6ab97.md "InternalDefinition Class") See Also  
---  
Whether or not the parameter values can vary across group members. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public ICollection<ElementId> SetAllowVaryBetweenGroups(
	Document document,
	bool allowVaryBetweenGroups
)
```
  
Visual Basic  
---  
```text
Public Function SetAllowVaryBetweenGroups ( _
	document As Document, _
	allowVaryBetweenGroups As Boolean _
) As ICollection(Of ElementId)
```
  
Visual C++  
---  
```text
public:
ICollection<ElementId^>^ SetAllowVaryBetweenGroups(
	Document^ document, 
	bool allowVaryBetweenGroups
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document of this parameter. 
allowVaryBetweenGroups
    Type: System..::..Boolean Whether this parameter should be allowed to vary between groups. 
# ### Return Value
The ids of elements that were updated to align the values between groups. 
# Remarks
When a parameter is set to not vary between groups Revit will automatically align the parameter values of any elements that actually varied between group instances. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | This parameter does not support the specified value of allowVaryBetweenGroups. -or- document is not a project document. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md "ModificationForbiddenException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md "ModificationOutsideTransactionException Class") | The document has no open transaction. |

# See Also
[InternalDefinition Class](97f42435-3067-622e-7a34-919f42f6ab97.md "InternalDefinition Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 