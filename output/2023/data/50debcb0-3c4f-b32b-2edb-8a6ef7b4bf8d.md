# EraseSchemaAndAllEntities Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Document..::..EraseSchemaAndAllEntities Method   
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") See Also  
---  
Erases Schema and all its Entities from the document. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2021 
# Syntax
C#  
---  
```text
public void EraseSchemaAndAllEntities(
	Schema schema
)
```
  
Visual Basic  
---  
```text
Public Sub EraseSchemaAndAllEntities ( _
	schema As Schema _
)
```
  
Visual C++  
---  
```text
public:
void EraseSchemaAndAllEntities(
	Schema^ schema
)
```
  
# ### Parameters
schema
    Type: [Autodesk.Revit.DB.ExtensibleStorage..::..Schema](9817e7db-8367-ea4e-1769-0488f3faa37f.md "Schema Class") The Schema to erase. 
# Remarks
The Schema remains in memory. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | No write access to this Schema. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md "ModificationForbiddenException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md "ModificationOutsideTransactionException Class") | The document has no open transaction. |

# See Also
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 