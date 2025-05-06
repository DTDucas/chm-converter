# GetSunrise Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
SunAndShadowSettings..::..GetSunrise Method   
[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.md "SunAndShadowSettings Class") See Also  
---  
Identifies the sunrise time for the SunAndShadowSettings element at its current location and indicated date. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public DateTime GetSunrise(
	DateTime date
)
```
  
Visual Basic  
---  
```text
Public Function GetSunrise ( _
	date As DateTime _
) As DateTime
```
  
Visual C++  
---  
```text
public:
DateTime GetSunrise(
	DateTime date
)
```
  
# ### Parameters
date
    Type: System..::..DateTime The date for which to determine sunrise time. 
# ### Return Value
The date and time. The value will be in Coordinated Universal Time (UTC). 
# Remarks
The value returned is affected by the value of the [UsesDST](34284848-ddf6-1fda-d1d2-43f8c2e2ad78.md "UsesDST Property") flag set for the current location. If this value is true, the sunrise value will be adjusted for Daylight Savings Time, regardless of the value of the input date. 
# See Also
[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.md "SunAndShadowSettings Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 