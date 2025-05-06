# GetChildrenKeys Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
KeyBasedTreeEntry..::..GetChildrenKeys Method   
[KeyBasedTreeEntry Class](119355ca-f9b6-3d6a-b315-6977ac95edbe.md "KeyBasedTreeEntry Class") See Also  
---  
Gets a collection containing the keys of all children entry objects from this entry. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public IList<string> GetChildrenKeys()
```
  
Visual Basic  
---  
```text
Public Function GetChildrenKeys As IList(Of String)
```
  
Visual C++  
---  
```text
public:
IList<String^>^ GetChildrenKeys()
```
  
# ### Return Value
The collection containing the keys of all children entry objects from this entry. 
# Remarks
To look up the entry object corresponding to the child keys using KeyBasedTreeEntries.FindEntry(). 
# See Also
[KeyBasedTreeEntry Class](119355ca-f9b6-3d6a-b315-6977ac95edbe.md "KeyBasedTreeEntry Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 