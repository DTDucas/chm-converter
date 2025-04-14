# ToolTipImage Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RibbonItem..::..ToolTipImage Property   
[RibbonItem Class](79225f03-1633-3722-15b0-752c91a3740d.md "RibbonItem Class") See Also  
---  
The image to show as a part of the button extended tooltip 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public ImageSource ToolTipImage { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ToolTipImage As ImageSource
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ImageSource^ ToolTipImage {
	ImageSource^ get ();
	void set (ImageSource^ value);
}
```
  
# Remarks
Shown when the cursor hovers over the command. If neither this property nor LongDescription is supplied, the button will not have an extended tooltip. Maximum height or width is 355 pixels. SplitButton and RadioButtonGroup cannot display the tooltip set by this method. SplitButton shows the current PushButton tooltip and RadioButtonGroup has no tooltip.
# See Also
[RibbonItem Class](79225f03-1633-3722-15b0-752c91a3740d.md "RibbonItem Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)