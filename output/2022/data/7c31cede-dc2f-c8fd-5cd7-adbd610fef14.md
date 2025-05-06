# GetSegment Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
RebarShapeDefinitionBySegments..::..GetSegment Method   
[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.md "RebarShapeDefinitionBySegments Class") See Also  
---  
Return a reference to one of the segments in the definition. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public RebarShapeSegment GetSegment(
	int segmentIndex
)
```
  
Visual Basic  
---  
```text
Public Function GetSegment ( _
	segmentIndex As Integer _
) As RebarShapeSegment
```
  
Visual C++  
---  
```text
public:
RebarShapeSegment^ GetSegment(
	int segmentIndex
)
```
  
# ### Parameters
segmentIndex
    Type: System..::..Int32 Index of the segment (0 to NumberOfSegments - 1). 
# ### Return Value
The requested segment. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | segmentIndex is not between 0 and NumberOfSegments. |

# See Also
[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.md "RebarShapeDefinitionBySegments Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 