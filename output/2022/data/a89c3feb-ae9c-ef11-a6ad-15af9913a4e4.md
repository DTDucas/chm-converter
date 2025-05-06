# GetLocalFileName Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ImporterIFCUtils..::..GetLocalFileName Method   
[ImporterIFCUtils Class](63c96f27-12ea-3b90-aa39-515a81c79e33.md "ImporterIFCUtils Class") See Also  
---  
Get the local file name, including the path, corresponding to a linked IFC file. This will create a local copy of the IFC file if necessary. 
**Namespace:** [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2018 
# Syntax
C#  
---  
```text
public static string GetLocalFileName(
	Document aDoc,
	string fileName
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetLocalFileName ( _
	aDoc As Document, _
	fileName As String _
) As String
```
  
Visual C++  
---  
```text
public:
static String^ GetLocalFileName(
	Document^ aDoc, 
	String^ fileName
)
```
  
# ### Parameters
aDoc
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document that will contain the IFC link. 
fileName
    Type: System..::..String The original file name and path. 
# ### Return Value
The local file name and path corresponding to the input file name. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Can't process file name. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[ImporterIFCUtils Class](63c96f27-12ea-3b90-aa39-515a81c79e33.md "ImporterIFCUtils Class")
[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.md "Autodesk.Revit.DB.IFC Namespace")
Send comments on this topic to 