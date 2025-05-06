# WorksetTable Class (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
WorksetTable Class  
[Members](cd96335a-ae32-c6a4-6c74-eeb9e84c7127.md "WorksetTable Members") See Also  
---  
A table containing references to all the worksets contained in a document. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public class WorksetTable : IDisposable
```
  
Visual Basic  
---  
```text
Public Class WorksetTable _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class WorksetTable : IDisposable
```
  
# Remarks
There is one WorksetTable for each document. There will be at least one default workset in the table, even if worksharing has not been enabled in the document. 
# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB..::..WorksetTable
# See Also
[WorksetTable Members](cd96335a-ae32-c6a4-6c74-eeb9e84c7127.md "WorksetTable Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 