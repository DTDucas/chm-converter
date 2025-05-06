# IsValidObject Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
IndexStream..::..IsValidObject Property   
[IndexStream Class](9c300586-7f1f-41db-270b-797d6ad967d8.md "IndexStream Class") See Also  
---  
Specifies whether the .NET object represents a valid Revit entity. 
**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
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
[IndexStream Class](9c300586-7f1f-41db-270b-797d6ad967d8.md "IndexStream Class")
[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")
Send comments on this topic to 