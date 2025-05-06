# FailureDefinitionId Class (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
FailureDefinitionId Class  
[Members](57ee1d47-c340-ce31-a736-548b3aa912e3.md "FailureDefinitionId Members") See Also  
---  
The unique identifier of a FailureDefinition. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 
# Syntax
C#  
---  
```text
public class FailureDefinitionId : GuidEnum
```
  
Visual Basic  
---  
```text
Public Class FailureDefinitionId _
	Inherits GuidEnum
```
  
Visual C++  
---  
```text
public ref class FailureDefinitionId : public GuidEnum
```
  
# Remarks
Each possible failure in Revit must be defined and registered during Revit application startup by creating a FailureDefinition object. Unique FailureDefinitionId must be used as a key to register FailureDefinition. Those unique FailureDefinitionId should be created using GUID generation tool. Later FailureDefinitionId can be used to lookup FailureDefinition in FailureDefinitionRegistry, and create and post FailureMessages. 
# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB..::..GuidEnum](36623d19-ba65-63c0-337a-f43c593a9931.md "GuidEnum Class") Autodesk.Revit.DB..::..FailureDefinitionId
# See Also
[FailureDefinitionId Members](57ee1d47-c340-ce31-a736-548b3aa912e3.md "FailureDefinitionId Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 