# StartTangent Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
FlexDuct..::..StartTangent Property   
[FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.md "FlexDuct Class") See Also  
---  
Gets or sets the tangent vector at the start of the curve. The invalid or zero vector is ignored when setting the tangent. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.md "Autodesk.Revit.DB.Mechanical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public XYZ StartTangent { get; set; }
```
  
Visual Basic  
---  
```text
Public Property StartTangent As XYZ
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property XYZ^ StartTangent {
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
[FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.md "FlexDuct Class")
[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.md "Autodesk.Revit.DB.Mechanical Namespace")
Send comments on this topic to 