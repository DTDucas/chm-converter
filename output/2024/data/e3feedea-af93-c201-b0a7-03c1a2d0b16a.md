# MoveNext Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ComponentRepeaterIterator..::..MoveNext Method   
[ComponentRepeaterIterator Class](d2bc2d9c-ae40-4e5e-a56a-9e5e8e7057cf.md "ComponentRepeaterIterator Class") See Also  
---  
Increments the iterator to the next item. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public virtual bool MoveNext()
```
  
Visual Basic  
---  
```text
Public Overridable Function MoveNext As Boolean
```
  
Visual C++  
---  
```text
public:
virtual bool MoveNext()
```
  
# ### Return Value
True if there is a next available item in this iterator. False if the iterator has completed all available items. 
# See Also
[ComponentRepeaterIterator Class](d2bc2d9c-ae40-4e5e-a56a-9e5e8e7057cf.md "ComponentRepeaterIterator Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 