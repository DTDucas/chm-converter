# AreValidDirectShapeReferenceOptions Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DirectShape..::..AreValidDirectShapeReferenceOptions Method   
[DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.md "DirectShape Class") See Also  
---  
Validates that the input DirectShapeReferenceOptions are suitable for creating a direct shape reference object. If the options specify an ExternalGeometryId, it must not correspond to any existing reference object belonging to the DirectShape. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public bool AreValidDirectShapeReferenceOptions(
	DirectShapeReferenceOptions options
)
```
  
Visual Basic  
---  
```text
Public Function AreValidDirectShapeReferenceOptions ( _
	options As DirectShapeReferenceOptions _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool AreValidDirectShapeReferenceOptions(
	DirectShapeReferenceOptions^ options
)
```
  
# ### Parameters
options
    Type: [Autodesk.Revit.DB..::..DirectShapeReferenceOptions](c77da180-10dd-8e8a-d5d4-01cfc06135e5.md "DirectShapeReferenceOptions Class") The options to test. 
# ### Return Value
True if the options can be used to add a reference object to this DirectShape. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.md "DirectShape Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)