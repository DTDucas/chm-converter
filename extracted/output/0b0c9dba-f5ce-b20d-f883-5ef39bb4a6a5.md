# Category Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Subelement..::..Category Property   
[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.md "Subelement Class") See Also  
---  
Retrieves a Category object that represents the category or sub category of the subelement.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public Category Category { get; }
```
  
Visual Basic  
---  
```text
Public ReadOnly Property Category As Category
	Get
```
  
Visual C++  
---  
```text
public:
property Category^ Category {
	Category^ get ();
}
```
  
# Remarks
All category objects can be retrieved from the application by using the Categories property of the Application.Settings object.
# See Also
[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.md "Subelement Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)