# ServerPath Class (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ServerPath Class  
[Members](7f5161f8-d12d-7caf-a903-cd30f99f6b52.md "ServerPath Members") See Also  
---  
This class represents a path to a Revit Server location, rather than a location on disk or a network drive. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public class ServerPath : ModelPath
```
  
Visual Basic  
---  
```text
Public Class ServerPath _
	Inherits ModelPath
```
  
Visual C++  
---  
```text
public ref class ServerPath : public ModelPath
```
  
# Remarks
ServerPaths must refer to Revit models.
ServerPaths are relative to the central server location, and are of the form "RSN://{HostNodeName}/{model_path}".
The {model_path} portion is a relative path to a Revit model. For example, the following are valid server paths:
  * RSN://EXS/hospital.rvt
  * RSN://EXS.autodesk.com/Old Files/hotel2.rvt
  * RSN://EXS.autodesk.com/Old Files/Last Week/Tuesday\hotel2.rvt

The following would not be valid server paths: 
  * //EXS/Old Files/.rvt
  * EXS/hospital

# Inheritance Hierarchy
System..::..Object [Autodesk.Revit.DB..::..ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.md "ModelPath Class") Autodesk.Revit.DB..::..ServerPath
# See Also
[ServerPath Members](7f5161f8-d12d-7caf-a903-cd30f99f6b52.md "ServerPath Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 