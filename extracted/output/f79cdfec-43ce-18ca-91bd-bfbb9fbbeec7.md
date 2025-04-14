# ElementId Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
MEPNetworkSegmentId..::..ElementId Property   
[MEPNetworkSegmentId Class](cb14904b-7147-4742-09c9-98da77011030.md "MEPNetworkSegmentId Class") See Also  
---  
The element id where this analytical segment belongs. 
**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public ElementId ElementId { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ElementId As ElementId
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ElementId^ ElementId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[MEPNetworkSegmentId Class](cb14904b-7147-4742-09c9-98da77011030.md "MEPNetworkSegmentId Class")
[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md "Autodesk.Revit.DB.Analysis Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)