# SharesSettings Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
SunAndShadowSettings..::..SharesSettings Property   
[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.md "SunAndShadowSettings Class") See Also  
---  
Identifies whether settings are shared globally. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public bool SharesSettings { get; set; }
```
  
Visual Basic  
---  
```text
Public Property SharesSettings As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool SharesSettings {
	bool get ();
	void set (bool value);
}
```
  
# Remarks
Identifies whether the per-view SunAndShadowSettings element shares global settings. Global settings are a special case that allows multiple views to be associated together in order that a change in one view affects that same change in other views. There cannot be multiple such groups, and a SunAndShadowSettings element is either a global setting or not. 
# See Also
[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.md "SunAndShadowSettings Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 