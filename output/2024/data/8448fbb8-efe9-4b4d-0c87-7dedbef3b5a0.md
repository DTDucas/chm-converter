# TextQualifier Property (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ViewScheduleExportOptions..::..TextQualifier Property   
[ViewScheduleExportOptions Class](f0bde7ea-ceab-820d-7c55-b09819f21607.md "ViewScheduleExportOptions Class") See Also  
---  
How to qualify text fields. Default is DoubleQuote. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 
# Syntax
C#  
---  
```text
public ExportTextQualifier TextQualifier { get; set; }
```
  
Visual Basic  
---  
```text
Public Property TextQualifier As ExportTextQualifier
	Get
	Set
```
  
Visual C++  
---  
```text
public:
property ExportTextQualifier TextQualifier {
	ExportTextQualifier get ();
	void set (ExportTextQualifier value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[ViewScheduleExportOptions Class](f0bde7ea-ceab-820d-7c55-b09819f21607.md "ViewScheduleExportOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 