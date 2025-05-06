# GetSymbolId Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
GroupNode..::..GetSymbolId Method   
[GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.md "GroupNode Class") See Also  
---  
The Id of the symbol associated with the node. This property is deprecated in Revit 2023 and may be removed in a future version of Revit. For an InstanceNode please use the GetSymbolGeometryId().SymbolId. For a LinkNode please use SymbolId property. In Revit 2023 we introduced instance nodes that point to a part of the symbol's geometry. For comparing if two such nodes point to the same geometry, the SymbolId isn't enough. SymbolGeometryId can be used to identify a piece of geometry managed by a symbol element. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
[ObsoleteAttribute]
public ElementId GetSymbolId()
```
  
Visual Basic  
---  
```text
<ObsoleteAttribute> _
Public Function GetSymbolId As ElementId
```
  
Visual C++  
---  
```text
[ObsoleteAttribute]
public:
ElementId^ GetSymbolId()
```
  
# See Also
[GroupNode Class](8b1cabde-3c37-1735-a186-2ce026555ce0.md "GroupNode Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 