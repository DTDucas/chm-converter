# Export Method (String, String, GBXMLExportOptions) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Document..::..Export Method (String, String, GBXMLExportOptions)  
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") See Also  
---  
Export the model in gbXML (green-building) format. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public bool Export(
	string folder,
	string name,
	GBXMLExportOptions options
)
```
  
Visual Basic  
---  
```text
Public Function Export ( _
	folder As String, _
	name As String, _
	options As GBXMLExportOptions _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool Export(
	String^ folder, 
	String^ name, 
	GBXMLExportOptions^ options
)
```
  
# ### Parameters
folder
    Type: System..::..String Indicates the path of a folder where to export the gbXML file. 
name
    Type: System..::..String Indicates the name of the gbXML file to export. If it doesn't end with ".xml", extension ".xml" will be added automatically. The name cannot contain any of the following characters: \/:*?"<>|. Empty name is not acceptable. 
options
    Type: [Autodesk.Revit.DB..::..GBXMLExportOptions](abb350ef-a773-7b70-6881-166e6f3c0a56.md "GBXMLExportOptions Class") Options which control the contents of the export. 
# ### Return Value
True if successful, otherwise False. 
# Remarks
This export operation will operate on the main EnergyAnalysisDetailModel in the document, if it exists (see EnergyAnalysisDetailModel.GetMainEnergyAnalysisDetailModel()). If it does not exist, or if the requested ExportEnergyModelType does not match the type of the main EnergyAnalysisDetailModel, this function will fail. If you need to export a model with different settings or type than the current main energy model in the document, you should delete the current main energy model, update the EnergyAnalysisSettings, and regenerate the energy model. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The path is not valid for exporting gbXML files. -or- The name is empty or not valid for exporting gbXML files. -or- Analysis type is invalid. For AnalysisMode.ConceptualMasses, use Document.Export(String, String, MassGBXMLExportOptions). -or- There is no main EnergyAnalysisDetailModel in the document, or the current main EnergyAnalysisDetailModel is not compatible with the option set in the GBXMLExportOptions. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Exporting is not allowed in the current application mode. -or- Export is temporarily disabled. |

# See Also
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")
[Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.md "Export Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 