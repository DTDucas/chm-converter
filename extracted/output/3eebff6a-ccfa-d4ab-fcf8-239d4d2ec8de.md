# GetDefaultFloorType Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Floor..::..GetDefaultFloorType Method   
[Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.md "Floor Class") See Also  
---  
Returns id of default floor type. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2022 
# Syntax
C#  
---  
```text
public static ElementId GetDefaultFloorType(
	Document document,
	bool isFoundation
)
```
  
Visual Basic  
---  
```text
Public Shared Function GetDefaultFloorType ( _
	document As Document, _
	isFoundation As Boolean _
) As ElementId
```
  
Visual C++  
---  
```text
public:
static ElementId^ GetDefaultFloorType(
	Document^ document, 
	bool isFoundation
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document. 
isFoundation
    Type: System..::..Boolean True to return id of foundation floor type. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.md "Floor Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)