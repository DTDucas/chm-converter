# ParameterValue Class (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ParameterValue Class  
[Members](fc18964a-0df5-d477-ca0a-fb0c69d3f152.md "ParameterValue Members") See Also  
---  
A class that holds a value of a parameter element. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2016 Subscription Update 
# Syntax
C#  
---  
```text
public class ParameterValue : IDisposable
```
  
Visual Basic  
---  
```text
Public Class ParameterValue _
	Implements IDisposable
```
  
Visual C++  
---  
```text
public ref class ParameterValue : IDisposable
```
  
# Remarks
This is a non-instantiable base class. Classes that actually store a value of a certain type are all derived from this base class, once class per each value type. 
# Inheritance Hierarchy
System..::..Object Autodesk.Revit.DB..::..ParameterValue [Autodesk.Revit.DB..::..DoubleParameterValue](561ef32b-c3bc-3847-ef2a-27f4a011e650.md "DoubleParameterValue Class") [Autodesk.Revit.DB..::..ElementIdParameterValue](7de25c99-4f85-ef1d-7f64-74092f963c98.md "ElementIdParameterValue Class") [Autodesk.Revit.DB..::..IntegerParameterValue](14c16038-74bf-205b-ac93-6ffa6274c034.md "IntegerParameterValue Class") [Autodesk.Revit.DB..::..NullParameterValue](fe10010f-e127-7248-1f17-8c1ee0d41ea0.md "NullParameterValue Class") [Autodesk.Revit.DB..::..StringParameterValue](2f79fff4-9773-471a-83f8-5636459bdbe5.md "StringParameterValue Class")
# See Also
[ParameterValue Members](fc18964a-0df5-d477-ca0a-fb0c69d3f152.md "ParameterValue Members")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 