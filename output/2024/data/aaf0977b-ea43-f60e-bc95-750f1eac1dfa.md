# Item Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
VertexIndexPairArray..::..Item Property   
[VertexIndexPairArray Class](ebf9396b-0cd1-2510-3957-80cd871a9db7.md "VertexIndexPairArray Class") See Also  
---  
Gets or sets a VertexIndex pair at a specified index within the array.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public virtual VertexIndexPair this[
	int index
] { get; set; }
```
  
Visual Basic  
---  
```text
Public Overridable Property Item ( _
	index As Integer _
) As VertexIndexPair
	Get
	Set
```
  
Visual C++  
---  
```text
public:
virtual property VertexIndexPair^ Item[int index] {
	VertexIndexPair^ get (int index);
	void set (int index, VertexIndexPair^ value);
}
```
  
# ### Parameters
index
    Type: System..::..Int32The index of the VertexIndex pair to be set or retrieved.
# ### Return Value
Returns the VertexIndex pair at the specified index.
# See Also
[VertexIndexPairArray Class](ebf9396b-0cd1-2510-3957-80cd871a9db7.md "VertexIndexPairArray Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 