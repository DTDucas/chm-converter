# IsPermitted Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
EditScope..::..IsPermitted Property   
[EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.md "EditScope Class") See Also  
---  
Tells if the edit scope is permitted to start. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public bool IsPermitted { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property IsPermitted As Boolean
	Get
```
  
Visual C++  
---  
```text
public:
property bool IsPermitted {
	bool get ();
}
```
  
# Remarks
The edit scope is not permitted to start for one of the following possible reasons: The document is in read-only state, or the document is currently modifiable, or there already is another edit mode active in the document. 
# See Also
[EditScope Class](bac11282-3a3b-953e-8bc4-960c62da4946.md "EditScope Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 