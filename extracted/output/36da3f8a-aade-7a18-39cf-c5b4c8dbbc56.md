# SegmentLengthDimensionsOffset Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarBendingDetailType..::..SegmentLengthDimensionsOffset Property   
[RebarBendingDetailType Class](9e6af0fc-1c7a-47e2-d6fd-460a36d6bc89.md "RebarBendingDetailType Class") See Also  
---  
Identifies the offset of the segment length dimensions. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public double SegmentLengthDimensionsOffset { get; set; }
```
  
Visual Basic  
---  
```text
Public Property SegmentLengthDimensionsOffset As Double
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property double SegmentLengthDimensionsOffset {
	double get ();
	void set (double value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: The given value for segmentLengthDimensionsOffset must be between 0 and 30000 feet. |

# See Also
[RebarBendingDetailType Class](9e6af0fc-1c7a-47e2-d6fd-460a36d6bc89.md "RebarBendingDetailType Class")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)