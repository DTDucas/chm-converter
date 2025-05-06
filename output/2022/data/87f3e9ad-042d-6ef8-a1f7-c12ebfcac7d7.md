# ExternalResourceUIBrowseResultType Enumeration (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ExternalResourceUIBrowseResultType Enumeration  
See Also  
---  
Describes the type of external resource browsing result. 
Describes the type of external resource browsing result. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 **Since:** 2015 
# Syntax
C#  
---  
```text
public enum ExternalResourceUIBrowseResultType
```
  
Visual Basic  
---  
```text
Public Enumeration ExternalResourceUIBrowseResultType
```
  
Visual C++  
---  
```text
public enum class ExternalResourceUIBrowseResultType
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| Success | There is no predefined error happened during this browse operation. The DB server can store any errors itself in this case. |
| FolderNotFound | The specified external resource folder cannot be found by external resource server. |
| ResourceNotFound | The specified external resource cannot be found by external resource server. |

# Remarks
This enum is used to describe the type of external resources browsing operation result ( the browsing operation include list folders and resources of an external server or a folder, or open an external resource in browsing dialog.) The meaning of each enum value: 
  * There is no predefined error happened during this browse operation. The DB server can store any errors itself in this case. 
  * FolderNotFound means the external resource folder want to browse could not be founded in external server.
  * ResourceNotFound means the external resource want to open could not be founded in external server.

# See Also
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 