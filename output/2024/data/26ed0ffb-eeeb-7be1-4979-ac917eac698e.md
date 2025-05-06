# Contains Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Categories..::..Contains Method   
[Categories Class](6708af38-6a62-ead0-88ff-c68bedd88ffe.md "Categories Class") See Also  
---  
Identifies if a category which has the specified name is in the list of top-level categories.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public override bool Contains(
	string name
)
```
  
Visual Basic  
---  
```text
Public Overrides Function Contains ( _
	name As String _
) As Boolean
```
  
Visual C++  
---  
```text
public:
virtual bool Contains(
	String^ name
) override
```
  
# ### Parameters
name
    Type: System..::..StringThe name of the category to be retrieved.
# ### Field Value
Whether the category exists in the list of top-level categories.
# See Also
[Categories Class](6708af38-6a62-ead0-88ff-c68bedd88ffe.md "Categories Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 