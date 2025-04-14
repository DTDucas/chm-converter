# EndTangent Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
HermiteSplineTangents..::..EndTangent Property   
[HermiteSplineTangents Class](b77a59cc-229c-52c4-5bc4-94670f5d3571.md "HermiteSplineTangents Class") See Also  
---  
The tangent vector at the end of the curve. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public XYZ EndTangent { get; set; }
```
  
Visual Basic  
---  
```text
Public Property EndTangent As XYZ
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property XYZ^ EndTangent {
	XYZ^ get ();
	void set (XYZ^ value);
}
```
  
# ### Field Value
This must be a nomalized unit vector. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: endTangent has zero length. |
| [Autodesk.Revit.Exceptions..::..InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.md "InapplicableDataException Class") | The end tangent value is not set. |

# See Also
[HermiteSplineTangents Class](b77a59cc-229c-52c4-5bc4-94670f5d3571.md "HermiteSplineTangents Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)