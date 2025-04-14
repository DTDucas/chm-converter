# GetDBServerId Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
IExternalResourceUIServer..::..GetDBServerId Method   
[IExternalResourceUIServer Interface](aee37f3f-98e9-79c6-e02d-1b07e3ffd89c.md "IExternalResourceUIServer Interface") See Also  
---  
Implement this method to return the id of the server which is associated with this UI server. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
Guid GetDBServerId()
```
  
Visual Basic  
---  
```text
Function GetDBServerId As Guid
```
  
Visual C++  
---  
```text
Guid GetDBServerId()
```
  
# ### Return Value
The id of the associated DB server. 
# Remarks
If there's no DB server associated with this UI server, an empty GUID value will be returned. 
# See Also
[IExternalResourceUIServer Interface](aee37f3f-98e9-79c6-e02d-1b07e3ffd89c.md "IExternalResourceUIServer Interface")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)