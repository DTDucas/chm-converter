# ValidateExportOptions Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
INavisworksExporter..::..ValidateExportOptions Method   
[INavisworksExporter Interface](b389017c-d7af-f0a4-7440-e9dc30f47718.md "INavisworksExporter Interface") See Also  
---  
Determines if the inputs are valid, and returns an error message if not. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
bool ValidateExportOptions(
	Document document,
	string folder,
	string name,
	NavisworksExportOptions options,
	out string exceptionMessage
)
```
  
Visual Basic  
---  
```text
Function ValidateExportOptions ( _
	document As Document, _
	folder As String, _
	name As String, _
	options As NavisworksExportOptions, _
	<OutAttribute> ByRef exceptionMessage As String _
) As Boolean
```
  
Visual C++  
---  
```text
bool ValidateExportOptions(
	Document^ document, 
	String^ folder, 
	String^ name, 
	NavisworksExportOptions^ options, 
	[OutAttribute] String^% exceptionMessage
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document to export. 
folder
    Type: System..::..String The folder path. 
name
    Type: System..::..String The file name. 
options
    Type: [Autodesk.Revit.DB..::..NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.md "NavisworksExportOptions Class") The export options. 
exceptionMessage
    Type: System..::..String% The message to show in the exception thrown. This is not an end-user visible message, it is a developer message, and does not have to be localized. Ignored if the function returns true. 
# ### Return Value
True if the options are valid, false otherwise. 
# See Also
[INavisworksExporter Interface](b389017c-d7af-f0a4-7440-e9dc30f47718.md "INavisworksExporter Interface")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 