# DisplayNodeNumbers Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DividedPath..::..DisplayNodeNumbers Property   
[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.md "DividedPath Class") See Also  
---  
Controls whether the node numbers are shown when the divided path is selected 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public bool DisplayNodeNumbers { get; set; }
```
  
Visual Basic  
---  
```text
Public Property DisplayNodeNumbers As Boolean
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property bool DisplayNodeNumbers {
	bool get ();
	void set (bool value);
}
```
  
# Remarks
If true the divided path will show the number of each node when the divided path is selected. If false the node numbers are hidden. 
# See Also
[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.md "DividedPath Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 