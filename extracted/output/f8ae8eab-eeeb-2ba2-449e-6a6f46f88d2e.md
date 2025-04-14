# RemoveAllTriggers Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
UpdaterRegistry..::..RemoveAllTriggers Method   
[UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.md "UpdaterRegistry Class") See Also  
---  
Removes all triggers associated with Updater with specified UpdaterId. Does not unregister updater. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public static void RemoveAllTriggers(
	UpdaterId id
)
```
  
Visual Basic  
---  
```text
Public Shared Sub RemoveAllTriggers ( _
	id As UpdaterId _
)
```
  
Visual C++  
---  
```text
public:
static void RemoveAllTriggers(
	UpdaterId^ id
)
```
  
# ### Parameters
id
    Type: [Autodesk.Revit.DB..::..UpdaterId](16a9604f-51bd-ce34-f145-17ae06b7c1cf.md "UpdaterId Class") Id of specified updater 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The updater's owner's AddIn does not match the currently active AddIn. -or- RemoveAllTriggers called while executing an updater. |

# See Also
[UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.md "UpdaterRegistry Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)