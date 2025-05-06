# DimensionLineOrigin Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
MultiReferenceAnnotationOptions..::..DimensionLineOrigin Property   
[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.md "MultiReferenceAnnotationOptions Class") See Also  
---  
The origin point for the dimension line. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public XYZ DimensionLineOrigin { get; set; }
```
  
Visual Basic  
---  
```text
Public Property DimensionLineOrigin As XYZ
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property XYZ^ DimensionLineOrigin {
	XYZ^ get ();
	void set (XYZ^ value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |

# See Also
[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.md "MultiReferenceAnnotationOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 