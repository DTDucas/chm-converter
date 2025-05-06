# RenameWorkset Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
WorksetTable..::..RenameWorkset Method   
[WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.md "WorksetTable Class") See Also  
---  
Renames the workset. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 Subscription Update 
# Syntax
C#  
---  
```text
public static void RenameWorkset(
	Document aDoc,
	WorksetId worksetId,
	string name
)
```
  
Visual Basic  
---  
```text
Public Shared Sub RenameWorkset ( _
	aDoc As Document, _
	worksetId As WorksetId, _
	name As String _
)
```
  
Visual C++  
---  
```text
public:
static void RenameWorkset(
	Document^ aDoc, 
	WorksetId^ worksetId, 
	String^ name
)
```
  
# ### Parameters
aDoc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document in which the workset is accessed. 
worksetId
    Type: [Autodesk.Revit.DB..::..WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.md "WorksetId Class") The workset Id. 
name
    Type: System..::..String The workset name. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | aDoc is not a workshared document. -or- name is an empty string or contains only whitespace. -or- name cannot include prohibited characters. -or- The given workset name is already in use. -or- There is no workset in the document with this id. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md "ModificationForbiddenException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md "ModificationOutsideTransactionException Class") | The document has no open transaction. |

# See Also
[WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.md "WorksetTable Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 