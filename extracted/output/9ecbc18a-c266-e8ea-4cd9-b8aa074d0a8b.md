# MoveNext Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
GroupSetIterator..::..MoveNext Method   
[GroupSetIterator Class](da2e2718-c83a-f386-ae9c-beca78f9a728.md "GroupSetIterator Class") See Also  
---  
Move the iterator one item forward.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
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
Returns True if the iterator was successfully moved forward one item and the Current property will return a valid item. False will be returned it the iterator has reached the end of the set. 
# ### Implements
IEnumerator..::..MoveNext()()()()
# Remarks
MoveNext must be called before the Current property is valid with a new or Reset iterator in line with the expected behavior of IEnumerator. 
# See Also
[GroupSetIterator Class](da2e2718-c83a-f386-ae9c-beca78f9a728.md "GroupSetIterator Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)