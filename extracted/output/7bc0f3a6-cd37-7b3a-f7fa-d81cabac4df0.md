# Image Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ComboBox..::..Image Property   
[ComboBox Class](a5667995-e628-13df-c157-39c95b2435d6.md "ComboBox Class") See Also  
---  
The image shown on the ComboBox.
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011
# Syntax
C#  
---  
```text
public ImageSource Image { get; set; }
```
  
Visual Basic  
---  
```text
Public Property Image As ImageSource
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ImageSource^ Image {
	ImageSource^ get ();
	void set (ImageSource^ value);
}
```
  
# Remarks
The image will be shown on the left side of the item. The best size is 16 x 16 pixels. 
# See Also
[ComboBox Class](a5667995-e628-13df-c157-39c95b2435d6.md "ComboBox Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)