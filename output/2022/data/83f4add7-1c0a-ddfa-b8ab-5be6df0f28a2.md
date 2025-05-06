# Unload Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
RevitLinkType..::..Unload Method   
[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md "RevitLinkType Class") See Also  
---  
Unloads the Revit link. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2014 
# Syntax
C#  
---  
```text
public void Unload(
	ISaveSharedCoordinatesCallback callback
)
```
  
Visual Basic  
---  
```text
Public Sub Unload ( _
	callback As ISaveSharedCoordinatesCallback _
)
```
  
Visual C++  
---  
```text
public:
void Unload(
	ISaveSharedCoordinatesCallback^ callback
)
```
  
# ### Parameters
callback
    Type: [Autodesk.Revit.DB..::..ISaveSharedCoordinatesCallback](ed4eac2a-d482-7760-2ae7-855611d09c46.md "ISaveSharedCoordinatesCallback Interface") A callback indicating what to do if Revit encounters links which have changes in shared coordinates. If nullNothingnullptra null reference (Nothing in Visual Basic), Revit will not save any shared coordinates changes to the link before unloading. 
# Remarks
This function regenerates the document.
The document's Undo history will be cleared by this command. As a result, this command and others executed before it cannot be undone. All transaction phases (e.g. transactions transaction groups and sub-transaction) that were explicitly started must be finished prior to calling this method.
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.md "ForbiddenForDynamicUpdateException Class") | The function is not permitted during dynamic update. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | This RevitLinkType is not a top-level link. -or- The element "this RevitLinkType" is in a closed workset. -or- Revit could not save shared coordinates changes to the link or one of its nested links. -or- There is a transaction phase left open (such as a transaction, sub-transaction of transaction group) at the time of invoking this method. -or- The document is read-only. It cannot be modified. -or- The document is in an edit mode or is in family mode. -or- Revit cannot link a cloud model to non-cloud model |
| [Autodesk.Revit.Exceptions..::..RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.md "RevitServerInternalException Class") | Could be for any of the reasons that failed on service side. |
| [Autodesk.Revit.Exceptions..::..RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.md "RevitServerUnauthenticatedUserException Class") | User is not signed in with Autodesk id. |
| [Autodesk.Revit.Exceptions..::..RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.md "RevitServerUnauthorizedException Class") | User is not authorized to access the specified cloud model. |

# See Also
[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md "RevitLinkType Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 