# IsValidObject Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
DuctFittingAndAccessoryPressureDropUIDataItem..::..IsValidObject Property   
[DuctFittingAndAccessoryPressureDropUIDataItem Class](21430cd5-52d1-fcae-d793-43fcef03dfdc.md "DuctFittingAndAccessoryPressureDropUIDataItem Class") See Also  
---  
Specifies whether the .NET object represents a valid Revit entity. 
**Namespace:** [Autodesk.Revit.UI.Mechanical](9c9cf593-a9fe-7469-53c5-7b56ba7cd17e.md "Autodesk.Revit.UI.Mechanical Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
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
[DuctFittingAndAccessoryPressureDropUIDataItem Class](21430cd5-52d1-fcae-d793-43fcef03dfdc.md "DuctFittingAndAccessoryPressureDropUIDataItem Class")
[Autodesk.Revit.UI.Mechanical Namespace](9c9cf593-a9fe-7469-53c5-7b56ba7cd17e.md "Autodesk.Revit.UI.Mechanical Namespace")
Send comments on this topic to 