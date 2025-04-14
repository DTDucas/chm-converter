# MatchesFormat Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
EffectInstance..::..MatchesFormat Method   
[EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.md "EffectInstance Class") See Also  
---  
Tests whether the effect instance is appropriate for the given vertex format. 
**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2017 
# Syntax
C#  
---  
```text
public bool MatchesFormat(
	VertexFormat vertexFormat
)
```
  
Visual Basic  
---  
```text
Public Function MatchesFormat ( _
	vertexFormat As VertexFormat _
) As Boolean
```
  
Visual C++  
---  
```text
public:
bool MatchesFormat(
	VertexFormat^ vertexFormat
)
```
  
# ### Parameters
vertexFormat
    Type: [Autodesk.Revit.DB.DirectContext3D..::..VertexFormat](a946fa2b-bb1f-202c-38dc-8ae0307bedac.md "VertexFormat Class") A vertex format. 
# ### Return Value
True if the effect instance is valid for use with the specified vertex format. 
# Remarks
The vertex format may define vertex data that are not used by the effect instance. However, the effect instance can not reference vertex data that do not exist in the vertex format. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.md "EffectInstance Class")
[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.md "Autodesk.Revit.DB.DirectContext3D Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)