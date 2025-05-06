# SetExternalGeometryId Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DirectShapeReferenceOptions..::..SetExternalGeometryId Method   
[DirectShapeReferenceOptions Class](c77da180-10dd-8e8a-d5d4-01cfc06135e5.md "DirectShapeReferenceOptions Class") See Also  
---  
Sets the ExternalGeometryId associated with the reference object. The ID must be non-empty. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public DirectShapeReferenceOptions SetExternalGeometryId(
	ExternalGeometryId externalId
)
```
  
Visual Basic  
---  
```text
Public Function SetExternalGeometryId ( _
	externalId As ExternalGeometryId _
) As DirectShapeReferenceOptions
```
  
Visual C++  
---  
```text
public:
DirectShapeReferenceOptions^ SetExternalGeometryId(
	ExternalGeometryId^ externalId
)
```
  
# ### Parameters
externalId
    Type: [Autodesk.Revit.DB..::..ExternalGeometryId](6074854d-72b6-fa2f-b4ec-df48a33b862b.md "ExternalGeometryId Class")
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | externalId cannot be used as an ExternalGeometryId for a direct shape reference. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DirectShapeReferenceOptions Class](c77da180-10dd-8e8a-d5d4-01cfc06135e5.md "DirectShapeReferenceOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 