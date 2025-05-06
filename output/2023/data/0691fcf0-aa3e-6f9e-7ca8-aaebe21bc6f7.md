# IsSynchronizedWithCurrentItem Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
SplitButton..::..IsSynchronizedWithCurrentItem Property   
[SplitButton Class](5301a4c6-ba0f-1f66-61c3-8d0909ab0fe6.md "SplitButton Class") See Also  
---  
Indicates whether the top PushButton on the SplitButton changes based on the CurrentButton property. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2011
# Syntax
C#  
---  
```text
public bool IsSynchronizedWithCurrentItem { get; set; }
```
  
Visual Basic  
---  
```text
Public Property IsSynchronizedWithCurrentItem As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool IsSynchronizedWithCurrentItem {
	bool get ();
	void set (bool value);
}
```
  
# Remarks
If this property is true the SplitButton uses the current PushButton's properties to display the image, text, tooltip, etc. and executes the current item when clicked. If it is false the first listed PushButton in the GetItems() return is shown, and executes this PushButton when clicked. If it is false the items in drop down list can only be executed by opening the drop down list and clicking an item in the list. The default value is true. 
# See Also
[SplitButton Class](5301a4c6-ba0f-1f66-61c3-8d0909ab0fe6.md "SplitButton Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 