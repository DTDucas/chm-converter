# EnterPressed Event (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
TextBox..::..EnterPressed Event  
[TextBox Class](5cfff6ff-3982-e8f7-a3c8-43d93204d41a.md "TextBox Class") See Also  
---  
Subscribe to this event to be notified when the Enter button is pressed in the text box. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public event EventHandler<TextBoxEnterPressedEventArgs> EnterPressed
```
  
Visual Basic  
---  
```text
Public Event EnterPressed As EventHandler(Of TextBoxEnterPressedEventArgs)
```
  
Visual C++  
---  
```text
public:
 event EventHandler<TextBoxEnterPressedEventArgs^>^ EnterPressed {
	void add (EventHandler<TextBoxEnterPressedEventArgs^>^ value);
	void remove (EventHandler<TextBoxEnterPressedEventArgs^>^ value);
}
```
  
# See Also
[TextBox Class](5cfff6ff-3982-e8f7-a3c8-43d93204d41a.md "TextBox Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 