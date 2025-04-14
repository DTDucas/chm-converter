# MinimumThickness Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Application..::..MinimumThickness Property   
[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.md "Application Class") See Also  
---  
The minimum thickness allowed in Revit for a variety of geometric constructs. These include blends, extrusions, and wall layers. 
**Namespace:** [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.md "Autodesk.Revit.ApplicationServices Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public static double MinimumThickness { get; }
```
  
Visual Basic  
---  
```text
Public Shared ReadOnly Property MinimumThickness As Double
	Get
```
  
Visual C++  
---  
```text
public:
static property double MinimumThickness {
	double get ();
}
```
  
# Remarks
Do not use this value for any purpose other than its intended purpose. If you want to check for valid thickness value, use the function isValidThickness. 
# See Also
[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.md "Application Class")
[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.md "Autodesk.Revit.ApplicationServices Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)