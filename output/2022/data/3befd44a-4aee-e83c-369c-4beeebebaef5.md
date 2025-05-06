# GetPredefinedOptions Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
DGNExportOptions..::..GetPredefinedOptions Method   
[DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.md "DGNExportOptions Class") See Also  
---  
Returns an instance DGNExportOptions containing settings from a predefined export setup. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static DGNExportOptions GetPredefinedOptions(
	Document document,
	string setup
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetPredefinedOptions ( _
	document As Document, _
	setup As String _
) As DGNExportOptions
```
  
Visual C++  
---  
```text
public:
static DGNExportOptions^ GetPredefinedOptions(
	Document^ document, 
	String^ setup
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") A Revit project document to retrieve the setup from. 
setup
    Type: System..::..String The name of a predefined export setup from the specified document. 
# ### Return Value
An instance of predefined DGNExportOptions, or nullNothingnullptra null reference (Nothing in Visual Basic) if the name was not found. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | document is not a project document. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.md "DGNExportOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 