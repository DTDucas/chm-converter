# OwnerGroup Property (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
ExternalDefinition..::..OwnerGroup Property   
[ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.md "ExternalDefinition Class") See Also  
---  
Returns or change the group ID of the external parameter definition.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)
# Syntax
C#  
---  
```text
public virtual DefinitionGroup OwnerGroup { get; set; }
```
  
Visual Basic  
---  
```text
Public Overridable Property OwnerGroup As DefinitionGroup
	Get
	Set
```
  
Visual C++  
---  
```text
public:
virtual property DefinitionGroup^ OwnerGroup {
	DefinitionGroup^ get ();
	void set (DefinitionGroup^ value);
}
```
  
# Remarks
If failed When set the group, an InvalidOperationException will be thrown.
# See Also
[ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.md "ExternalDefinition Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 