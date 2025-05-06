# Insert Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
DocumentSet..::..Insert Method   
[DocumentSet Class](e1951076-29d2-4817-18d9-a01847fa812a.md "DocumentSet Class") See Also  
---  
Insert the specified item into the set.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public virtual bool Insert(
	Document item
)
```
  
Visual Basic  
---  
```text
Public Overridable Function Insert ( _
	item As Document _
) As Boolean
```
  
Visual C++  
---  
```text
public:
virtual bool Insert(
	Document^ item
)
```
  
# ### Parameters
item
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class")The item to be inserted into the set.
# ### Return Value
Returns whether the item was inserted into the set.
# See Also
[DocumentSet Class](e1951076-29d2-4817-18d9-a01847fa812a.md "DocumentSet Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 