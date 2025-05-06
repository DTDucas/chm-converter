# GetParameters Method (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
Element..::..GetParameters Method   
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class") See Also  
---  
Retrieves the parameters from the element via the given name.
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015
# Syntax
C#  
---  
```text
public IList<Parameter> GetParameters(
	string name
)
```
  
Visual Basic  
---  
```text
Public Function GetParameters ( _
	name As String _
) As IList(Of Parameter)
```
  
Visual C++  
---  
```text
public:
IList<Parameter^>^ GetParameters(
	String^ name
)
```
  
# ### Parameters
name
    Type: System..::..StringThe name of the parameter to be retrieved.
# ### Return Value
A collection containing the parameters having the same given parameter name. 
# Remarks
Multiple matches of parameters with the same name can occur because shared parameters or project parameters can be bound to an element category even if there is a built-in parameter with the same name already. 
If this method is used to find built-in parameters the code will not be portable to other languages of Revit (because built-in parameter names are translated, and this method matches the translation).
For the reasons above this method should be used sparingly and when portability across multiple languages is not a requirement.
Safer approaches include:
  * get_Parameter(Guid) to get a shared parameter by stored guid.
  * get_Parameter(BuiltInParameter) to find a built-in parameter in a language-independent way.

# See Also
[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.md "Element Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 