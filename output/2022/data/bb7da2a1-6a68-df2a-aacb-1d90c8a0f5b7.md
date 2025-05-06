# CurveElementType Enumeration (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
CurveElementType Enumeration  
See Also  
---  
An enumerated type listing the curve element types that can be used when filtering elements (via CurveElementFilter). 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public enum CurveElementType
```
  
Visual Basic  
---  
```text
Public Enumeration CurveElementType
```
  
Visual C++  
---  
```text
public enum class CurveElementType
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| Invalid | An invalid curve element type. |
| ModelCurve | A model curve. |
| DetailCurve | A detail curve. |
| SymbolicCurve | A symbolic curve. |
| ReferenceLine | A reference line. |
| SpaceSeparation | A space separation curve. |
| RoomSeparation | An room separation curve. |
| AreaSeparation | An area separation curve. |
| CurveByPoints | A curve created by connecting a set of points. |
| RepeatingDetail | The profile of a repeating detail set. |
| Insulation | A detail curve representing insulation. |
| Cloud | A portion of a revision cloud. |
| LoadAreaSeparation | A load area separation curve. |

# See Also
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 