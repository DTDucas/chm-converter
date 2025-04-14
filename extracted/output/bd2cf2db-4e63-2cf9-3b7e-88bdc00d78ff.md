# OnOpenConflict Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
DefaultOpenFromCloudCallback..::..OnOpenConflict Method   
[DefaultOpenFromCloudCallback Class](6269ec13-f36e-64fd-f173-aa7c358912f9.md "DefaultOpenFromCloudCallback Class") See Also  
---  
A method called when the conflict is happen during the model opening. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2019 
# Syntax
C#  
---  
```text
public virtual OpenConflictResult OnOpenConflict(
	OpenConflictScenario scenario
)
```
  
Visual Basic  
---  
```text
Public Overridable Function OnOpenConflict ( _
	scenario As OpenConflictScenario _
) As OpenConflictResult
```
  
Visual C++  
---  
```text
public:
virtual OpenConflictResult OnOpenConflict(
	OpenConflictScenario scenario
)
```
  
# ### Parameters
scenario
    Type: [Autodesk.Revit.DB..::..OpenConflictScenario](7db711fa-cfb1-39da-a184-5aaf4230b660.md "OpenConflictScenario Enumeration") The scenario of the conflict. 
# ### Return Value
Returns the result to indicate whether to keep the unsynchronized change, or open the latest version or cancel the open action. 
# ### Implements
[IOpenFromCloudCallback..::..OnOpenConflict(OpenConflictScenario)](21c8169e-9a58-3a6f-9060-e42975f39b16.md "OnOpenConflict Method")
# See Also
[DefaultOpenFromCloudCallback Class](6269ec13-f36e-64fd-f173-aa7c358912f9.md "DefaultOpenFromCloudCallback Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)