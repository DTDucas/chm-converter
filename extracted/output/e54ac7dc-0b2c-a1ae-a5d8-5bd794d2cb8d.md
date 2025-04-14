# Create Method (Document, String)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ExportDWGSettings..::..Create Method (Document, String)  
[ExportDWGSettings Class](a17fc52f-f67a-9763-e52f-29f867106908.md "ExportDWGSettings Class") See Also  
---  
Create a DWG export settings with default values. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static ExportDWGSettings Create(
	Document document,
	string name
)
```
  
Visual Basic  
---  
```text
Public Shared Function Create ( _
	document As Document, _
	name As String _
) As ExportDWGSettings
```
  
Visual C++  
---  
```text
public:
static ExportDWGSettings^ Create(
	Document^ document, 
	String^ name
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") Document where created settings is saved. 
name
    Type: System..::..String The name specified to this settings. 
# ### Return Value
The new DWG export settings instance. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | ExistOrEmpty |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ExportDWGSettings Class](a17fc52f-f67a-9763-e52f-29f867106908.md "ExportDWGSettings Class")
[Create Overload](b7cec5bd-8f85-4fd4-dded-4c73317d8b71.md "Create Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)