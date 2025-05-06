# Create Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
PointCloudType..::..Create Method   
[PointCloudType Class](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.md "PointCloudType Class") Example See Also  
---  
Creates a new point cloud type for a given point cloud engine. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public static PointCloudType Create(
	Document document,
	string engineIdentifier,
	string typeIdentifier
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	engineIdentifier As String, _
	typeIdentifier As String _
) As PointCloudType
```
  
Visual C++  
---  
```text
public:
static PointCloudType^ Create(
	Document^ document, 
	String^ engineIdentifier, 
	String^ typeIdentifier
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document in which to create the point cloud. 
engineIdentifier
    Type: System..::..String The string identifying the engine to be invoked. It should be the file extension or engine identifier registered by the third party. 
typeIdentifier
    Type: System..::..String The file name or the identification string for a non-file based engine. 
# ### Return Value
The newly created PointCloudType object to be used to create instances of this point cloud. 
# Remarks
A list of supported engine identifiers and whether they are file-based or not can be obtained from PointCloudEngineRegistry. The method GetSupportedEngines() returns a list of the identifiers registered for engines. 
# Examples
CopyC#
```text
private PointCloudInstance CreatePointCloud(Document doc)
{
    PointCloudType type = PointCloudType.Create(doc, "rcs", "c:\\32_cafeteria.rcs");
    return (PointCloudInstance.Create(doc, type.Id, Transform.Identity));
}
```

CopyVB.NET
```text
Private Function CreatePointCloud(doc As Document) As PointCloudInstance
    Dim type As PointCloudType = PointCloudType.Create(doc, "rcs", "c:\32_cafeteria.rcs")
    Return (PointCloudInstance.Create(doc, type.Id, Transform.Identity))
End Function
```

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | The engine identifier was not found in the Revit session. -or- document is not a project document. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..FileNotFoundException](73250198-dbc6-e760-4297-ec062f00f574.md "FileNotFoundException Class") | The external file could not be found or loaded. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | Unable to create a point cloud from the third party engine. |
| [Autodesk.Revit.Exceptions..::..ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.md "ModificationForbiddenException Class") | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions..::..ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.md "ModificationOutsideTransactionException Class") | The document has no open transaction. |

# See Also
[PointCloudType Class](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.md "PointCloudType Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 