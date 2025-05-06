# FabricationPartBrowserChanged Event (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
UIApplication..::..FabricationPartBrowserChanged Event  
[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.md "UIApplication Class") See Also  
---  
Subscribe to MEP Fabrication part browser changed event to be notified when MEP Fabrication part browser is updated. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public event EventHandler<FabricationPartBrowserChangedEventArgs> FabricationPartBrowserChanged
```
  
Visual Basic  
---  
```text
Public Event FabricationPartBrowserChanged As EventHandler(Of FabricationPartBrowserChangedEventArgs)
```
  
Visual C++  
---  
```text
public:
 event EventHandler<FabricationPartBrowserChangedEventArgs^>^ FabricationPartBrowserChanged {
	void add (EventHandler<FabricationPartBrowserChangedEventArgs^>^ value);
	void remove (EventHandler<FabricationPartBrowserChangedEventArgs^>^ value);
}
```
  
# Remarks
More docs about the different conditions goes here
# See Also
[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.md "UIApplication Class")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 