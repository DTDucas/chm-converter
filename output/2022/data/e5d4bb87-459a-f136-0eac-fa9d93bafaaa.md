# SetupEnergySimulationDialog Class (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
SetupEnergySimulationDialog Class  
[Members](c8311700-1fa3-430d-9c03-93bada186005.md "SetupEnergySimulationDialog Members") See Also  
---  
The Revit dialog which typically precedes invocation of an Energy Simulation run on the Green Building Studio server. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2016 
# Syntax
C#  
---  
```text
public class SetupEnergySimulationDialog : IDisposable
```
  
Visual Basic  
---  
```text
Public Class SetupEnergySimulationDialog _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class SetupEnergySimulationDialog : IDisposable
```
  
# Remarks
Add-ins can invoke this dialog to collect the name and id of a Green Building Studio project and the name of an analysis run from the user. When the user chooses these values and opts to Continue, control returns the add-in to use the values the user has selected. No Green Building Studio run is automatically invoked by the user's actions in the dialog when it is prompted by the add-in.
This class can be instantiated only when the user is logged in to their Autodesk account. 
# Inheritance Hierarchy
System..::..Object Autodesk.Revit.UI..::..SetupEnergySimulationDialog
# See Also
[SetupEnergySimulationDialog Members](c8311700-1fa3-430d-9c03-93bada186005.md "SetupEnergySimulationDialog Members")
[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.md "Autodesk.Revit.UI Namespace")
Send comments on this topic to 