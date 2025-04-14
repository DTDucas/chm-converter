# IsValidObject Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DuctSizeSettingIterator..::..IsValidObject Property   
[DuctSizeSettingIterator Class](cbbf8157-44b2-6680-c27f-3dd1a7afbaf8.md "DuctSizeSettingIterator Class") See Also  
---  
Specifies whether the .NET object represents a valid Revit entity. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.md "Autodesk.Revit.DB.Mechanical Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public bool IsValidObject { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property IsValidObject As Boolean
	Get
```
  
Visual C++  
---  
```text
public:
property bool IsValidObject {
	bool get ();
}
```
  
# ### Return Value
True if the API object holds a valid Revit native object, false otherwise. 
# Remarks
If the corresponding Revit native object is destroyed, or creation of the corresponding object is undone, a managed API object containing it is no longer valid. API methods cannot be called on invalidated wrapper objects. 
# See Also
[DuctSizeSettingIterator Class](cbbf8157-44b2-6680-c27f-3dd1a7afbaf8.md "DuctSizeSettingIterator Class")
[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.md "Autodesk.Revit.DB.Mechanical Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)