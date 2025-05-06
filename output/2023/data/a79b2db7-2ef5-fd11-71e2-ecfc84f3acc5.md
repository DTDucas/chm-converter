# HasValidDisplayPath Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
ExternalResourceReference..::..HasValidDisplayPath Method   
[ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md "ExternalResourceReference Class") See Also  
---  
Checks whether this external Resource has a valid display path. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public bool HasValidDisplayPath()
```
  
Visual Basic  
---  
```text
Public Function HasValidDisplayPath As Boolean
```
  
Visual C++  
---  
```text
public:
bool HasValidDisplayPath()
```
  
# ### Return Value
True if the this external Resource has a valid display path. False otherwise. 
# Remarks
For an external resource, such as a Revit link loaded from an external server, the valid display path should be like "My Server://Nested/Nested_1.rvt". For an external resource, such as a Revit link loaded from the "built-in" server, the valid display path should be like "c:\LocalLinks\Link_1.rvt". 
# See Also
[ExternalResourceReference Class](ffad9c15-8fc9-fbfd-f328-101533f4cf74.md "ExternalResourceReference Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 