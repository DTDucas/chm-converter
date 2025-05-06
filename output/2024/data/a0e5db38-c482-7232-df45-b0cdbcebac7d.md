# RebarContainerParameterManager Class (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
RebarContainerParameterManager Class  
[Members](3d9c1f41-bc7c-1af5-f647-cb96de7318d1.md "RebarContainerParameterManager Members") See Also  
---  
Provides implementation of RebarContainer parameters overrides. 
**Namespace:** [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public class RebarContainerParameterManager : IDisposable
```
  
Visual Basic  
---  
```text
Public Class RebarContainerParameterManager _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class RebarContainerParameterManager : IDisposable
```
  
# Remarks
When a new override is created, by default, the parameter will show the overridden value as read-only. You can control whether or not the parameter is modifiable using [SetOverriddenParameterReadonly(ElementId)](13dfe73c-aa3c-767d-c939-45feab28cd21.md "SetOverriddenParameterReadonly Method") and [SetOverriddenParameterModifiable(ElementId)](0b91fcec-09b4-8e89-01cf-24272512395f.md "SetOverriddenParameterModifiable Method").a 
# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB.Structure..::..RebarContainerParameterManager
# See Also
[RebarContainerParameterManager Members](3d9c1f41-bc7c-1af5-f647-cb96de7318d1.md "RebarContainerParameterManager Members")
[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.md "Autodesk.Revit.DB.Structure Namespace")
Send comments on this topic to 