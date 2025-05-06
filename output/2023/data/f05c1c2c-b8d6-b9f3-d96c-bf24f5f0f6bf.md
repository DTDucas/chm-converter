# ViewPlacementOnSheetStatus Enumeration (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
ViewPlacementOnSheetStatus Enumeration  
See Also  
---  
Indicates whether the View is placed on a Sheet. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2023 
# Syntax
C#  
---  
```text
public enum ViewPlacementOnSheetStatus
```
  
Visual Basic  
---  
```text
Public Enumeration ViewPlacementOnSheetStatus
```
  
Visual C++  
---  
```text
public enum class ViewPlacementOnSheetStatus
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| NotApplicable | The View cannot be placed on Sheet. |
| NotPlaced | The View is not placed on a Sheet. |
| PartiallyPlaced | The View is partially placed on a Sheet. |
| CompletelyPlaced | The View is completely placed on a Sheet. |

# Remarks
Some Views can be placed on one or more Sheets completely or partially. For example, a Schedule divided in segments, and only some of them are placed on Sheets. 
# See Also
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 