# SetRenderingQualitySettings Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
RenderingSettings..::..SetRenderingQualitySettings Method   
[RenderingSettings Class](7ba669f3-bd38-464b-f3f7-8a0b4e513a0a.md "RenderingSettings Class") See Also  
---  
Change rendering quality settings. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public void SetRenderingQualitySettings(
	RenderingQualitySettings settings
)
```
  
Visual Basic  
---  
```text
Public Sub SetRenderingQualitySettings ( _
	settings As RenderingQualitySettings _
)
```
  
Visual C++  
---  
```text
public:
void SetRenderingQualitySettings(
	RenderingQualitySettings^ settings
)
```
  
# ### Parameters
settings
    Type: [Autodesk.Revit.DB..::..RenderingQualitySettings](400738fc-3791-666c-10f3-ec46c771d6d5.md "RenderingQualitySettings Class") An instance of the new rendering quality settings. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[RenderingSettings Class](7ba669f3-bd38-464b-f3f7-8a0b4e513a0a.md "RenderingSettings Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 