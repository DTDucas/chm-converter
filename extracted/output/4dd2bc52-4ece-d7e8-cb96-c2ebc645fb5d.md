# ImageResolution Property

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ImageExportOptions..::..ImageResolution Property   
[ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.md "ImageExportOptions Class") See Also  
---  
The image resolution in dots per inch. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public ImageResolution ImageResolution { get; set; }
```
  
Visual Basic  
---  
```text
Public Property ImageResolution As ImageResolution
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ImageResolution ImageResolution {
	ImageResolution get ();
	void set (ImageResolution value);
}
```
  
# Remarks
The default is DPI_72. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.md "ImageExportOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)