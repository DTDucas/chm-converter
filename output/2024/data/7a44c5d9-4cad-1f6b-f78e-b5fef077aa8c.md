# GetTopLevelLink Method (Document, ModelPath) (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RevitLinkType..::..GetTopLevelLink Method (Document, ModelPath)  
[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md "RevitLinkType Class") See Also  
---  
Returns the ElementId of the (top-level) linked model with the given path. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public static ElementId GetTopLevelLink(
	Document document,
	ModelPath path
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetTopLevelLink ( _
	document As Document, _
	path As ModelPath _
) As ElementId
```
  
Visual C++  
---  
```text
public:
static ElementId^ GetTopLevelLink(
	Document^ document, 
	ModelPath^ path
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document to look for the linked model in. 
path
    Type: [Autodesk.Revit.DB..::..ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.md "ModelPath Class") A path indicating which linked model to return. 
# ### Return Value
The id of the link with the given path, or InvalidElementId if there is no top-level link at that path. 
# Remarks
This function will not return nested links. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md "RevitLinkType Class")
[GetTopLevelLink Overload](473b3f34-b5eb-7900-0a7e-8550cb066b35.md "GetTopLevelLink Method")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 