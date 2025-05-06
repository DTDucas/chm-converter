# ShowImageAsButton Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
TextBox..::..ShowImageAsButton Property   
[TextBox Class](5cfff6ff-3982-e8f7-a3c8-43d93204d41a.md "TextBox Class") See Also  
---  
Gets or sets a value that indicates if the Image set in the text box should be displayed as a clickable button.
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2011
# Syntax
C#  
---  
```text
public bool ShowImageAsButton { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ShowImageAsButton As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool ShowImageAsButton {
	bool get ();
	void set (bool value);
}
```
  
# Remarks
If this property is true, the image will shown as a button inside the textbox. Clicking this button will trigger the EnterPressed event. The default value is false.
# See Also
[TextBox Class](5cfff6ff-3982-e8f7-a3c8-43d93204d41a.md "TextBox Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 