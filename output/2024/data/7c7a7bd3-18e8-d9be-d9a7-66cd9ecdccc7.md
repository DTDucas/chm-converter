# FindByName Method (2024)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
GlobalParametersManager..::..FindByName Method   
[GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.md "GlobalParametersManager Class") Example See Also  
---  
Finds whether a global parameter with the given name exists in the input document. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2016 Subscription Update 
# Syntax
C#  
---  
```text
public static ElementId FindByName(
	Document document,
	string name
)
```
  
Visual Basic  
---  
```text
Public Shared Function FindByName ( _
	document As Document, _
	name As String _
) As ElementId
```
  
Visual C++  
---  
```text
public:
static ElementId^ FindByName(
	Document^ document, 
	String^ name
)
```
  
# ### Parameters
document
    Type: [Autodesk.Revit.DB..::..Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.md "Document Class") The document expected to contain the global parameter. 
name
    Type: System..::..String Name of the global parameter 
# ### Return Value
ElementId of the parameter element, or InvalidElementId if it was not found. 
# Remarks
No exception is thrown when no parameter with such a name exists in the document; instead, the method returns an ElementId.InvalidElementId. 
# Examples
CopyC#
```text
/// <summary>
/// Tries to find a global parameter by its name. 
/// </summary>
/// <param name="document">Revit project document.</param>
/// <param name="name">Name of a global parameter.</param>
/// <returns>An Element Id of the global parameter, or InvalidElementId if none found</returns>
public ElementId GetGlobalParameterByName(Document document, String name)
{
    // Global parameters are not available in all documents.
    // They are available in projects, but not in families.
    if (GlobalParametersManager.AreGlobalParametersAllowed(document))
    {
        return GlobalParametersManager.FindByName(document, name);
    }

    // return an empty set if global parameters are not available in the document
    return ElementId.InvalidElementId;
}
```

CopyVB.NET
```text
' <summary>
' Tries to find a global parameter by its name. 
' </summary>
' <param name="document">Revit project document.</param>
' <param name="name">Name of a global parameter.</param>
' <returns>An Element Id of the global parameter, or InvalidElementId if none found</returns>
Public Function GetGlobalParameterByName(document As Document, name As [String]) As ElementId
    ' Global parameters are not available in all documents.
    ' They are available in projects, but not in families.
    If GlobalParametersManager.AreGlobalParametersAllowed(document) Then
        Return GlobalParametersManager.FindByName(document, name)
    End If

    ' return an empty set if global parameters are not available in the document
    Return ElementId.InvalidElementId
End Function
```

# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |

# See Also
[GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.md "GlobalParametersManager Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 