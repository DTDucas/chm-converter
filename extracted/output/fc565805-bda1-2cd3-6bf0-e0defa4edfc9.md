# AreTargetAndFallbackCompatible Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
TessellatedShapeBuilder..::..AreTargetAndFallbackCompatible Method   
[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.md "TessellatedShapeBuilder Class") See Also  
---  
Checks whether this combination of fallback and target parameters can be used as a valid combination of inputs. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public bool AreTargetAndFallbackCompatible(
	TessellatedShapeBuilderTarget target,
	TessellatedShapeBuilderFallback fallback
)
```
  
Visual Basic  
---  
```text
Public Function AreTargetAndFallbackCompatible ( _
	target As TessellatedShapeBuilderTarget, _
	fallback As TessellatedShapeBuilderFallback _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool AreTargetAndFallbackCompatible(
	TessellatedShapeBuilderTarget target, 
	TessellatedShapeBuilderFallback fallback
)
```
  
# ### Parameters
target
    Type: [Autodesk.Revit.DB..::..TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.md "TessellatedShapeBuilderTarget Enumeration") What kind of geometrical objects should be built. 
fallback
    Type: [Autodesk.Revit.DB..::..TessellatedShapeBuilderFallback](ce755fa3-8727-2cd3-dbc3-c952bdc83a17.md "TessellatedShapeBuilderFallback Enumeration") What should be done if a geometrical object described by 'target' parameter cannot be built using all data from all stored face sets. 
# ### Return Value
True if the combination of fallback and target are a valid combination, false otherwise. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.md "TessellatedShapeBuilder Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)