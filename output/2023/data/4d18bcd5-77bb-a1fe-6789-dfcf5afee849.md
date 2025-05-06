# Link Method (String, DWFImportOptions) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Document..::..Link Method (String, DWFImportOptions)  
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") See Also  
---  
Links Markups in a DWF file into the project document. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public IList<ElementId> Link(
	string file,
	DWFImportOptions options
)
```
  
Visual Basic  
---  
```text
Public Function Link ( _
	file As String, _
	options As DWFImportOptions _
) As IList(Of ElementId)
```
  
Visual C++  
---  
```text
public:
IList<ElementId^>^ Link(
	String^ file, 
	DWFImportOptions^ options
)
```
  
# ### Parameters
file
    Type: System..::..String Full path of the file to link. File must exist and must be a valid DWF file. 
options
    Type: [Autodesk.Revit.DB..::..DWFImportOptions](8465ab77-dc06-79c2-4bed-e17a564adb22.md "DWFImportOptions Class") Various link options applicable to the DWF format. 
# ### Return Value
A collection of link instance element ids created by the markup link. 
# Remarks
Link isn't supported for family documents. Please use import instead. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Not a valid file for DWF import (.dwf or.dwfx files are valid). -or- Some of the views are not importable. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.md "FileArgumentNotFoundException Class") | The given file does not exist. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Import is temporarily disabled. -or- This Document is not a project document. |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md "ModificationForbiddenException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md "ModificationOutsideTransactionException Class") | The document has no open transaction. |

# See Also
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")
[Link Overload](0e45b625-904e-06be-fabc-8591fed616f8.md "Link Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 