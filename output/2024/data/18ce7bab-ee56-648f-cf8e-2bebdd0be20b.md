# IsValidObject Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
StructuralSection..::..IsValidObject Property   
[StructuralSection Class](65b59d7d-bd7b-c71b-7159-dfc506a912ee.md "StructuralSection Class") See Also  
---  
Specifies whether the .NET object represents a valid Revit entity. 
**Namespace:** [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.md "Autodesk.Revit.DB.Structure.StructuralSections Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
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
[StructuralSection Class](65b59d7d-bd7b-c71b-7159-dfc506a912ee.md "StructuralSection Class")
[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.md "Autodesk.Revit.DB.Structure.StructuralSections Namespace")
Send comments on this topic to 