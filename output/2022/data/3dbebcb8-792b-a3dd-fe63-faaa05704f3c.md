# StorageType Enumeration (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
StorageType Enumeration  
See Also  
---  
An enumerated type listing all of the internal parameter data storage types that Autodesk Revit supports. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)
# Syntax
C#  
---  
```text
public enum StorageType
```
  
Visual Basic  
---  
```text
Public Enumeration StorageType
```
  
Visual C++  
---  
```text
public enum class StorageType
```
  
# Members
| Member name | Description |
| --- | --- |
| --- | --- |
| None | None represents an invalid storage type. This value should not be used. |
| Integer | The internal data is stored in the form of a signed 32 bit integer. |
| Double | The data will be stored internally in the form of an 8 byte floating point number. |
| String | The internal data will be stored in the form of a string of characters. |
| ElementId | The data type represents an element and is stored as the id of the element. |

# See Also
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 