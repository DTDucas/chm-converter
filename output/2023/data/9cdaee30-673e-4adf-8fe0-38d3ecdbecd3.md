# SetSketchyLines Method (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
View..::..SetSketchyLines Method   
[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.md "View Class") See Also  
---  
Sets the sketchy lines settings for the view. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
public void SetSketchyLines(
	ViewDisplaySketchyLines sketchyLines
)
```
  
Visual Basic  
---  
```text
Public Sub SetSketchyLines ( _
	sketchyLines As ViewDisplaySketchyLines _
)
```
  
Visual C++  
---  
```text
public:
void SetSketchyLines(
	ViewDisplaySketchyLines^ sketchyLines
)
```
  
# ### Parameters
sketchyLines
    Type: [Autodesk.Revit.DB..::..ViewDisplaySketchyLines](c92b463b-1b59-695d-f06b-a76dacfaf2f0.md "ViewDisplaySketchyLines Class") Sketchy Lines settings to set. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | This view does not contain display-related properties. |

# See Also
[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.md "View Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 