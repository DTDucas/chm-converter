# DownloadParameterOptions Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ParameterUtils..::..DownloadParameterOptions Method   
[ParameterUtils Class](df5da06e-35c6-e32e-53c0-9fd68d3ab142.md "ParameterUtils Class") See Also  
---  
Retrieves settings associated with the given parameter from the Parameters Service. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 
# Syntax
C#  
---  
```text
public static ParameterDownloadOptions DownloadParameterOptions(
	ForgeTypeId parameterTypeId
)
```
  
Visual Basic  
---  
```text
Public Shared Function DownloadParameterOptions ( _
	parameterTypeId As ForgeTypeId _
) As ParameterDownloadOptions
```
  
Visual C++  
---  
```text
public:
static ParameterDownloadOptions^ DownloadParameterOptions(
	ForgeTypeId^ parameterTypeId
)
```
  
# ### Parameters
parameterTypeId
    Type: [Autodesk.Revit.DB..::..ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md "ForgeTypeId Class") Parameter identifier. 
# ### Return Value
Settings associated with a parameter. 
# Remarks
The settings associated with a parameter definition are accessible only to an authorized user. To retrieve them, the user must be signed in. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..AccessDeniedException](f280ddf5-9f59-eca8-634e-ace30de1f4bb.md "AccessDeniedException Class") | Thrown when the user is not authorized to access the requested information. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Thrown when the given parameter identifier is empty. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was null |
| [!:Autodesk::Revit::Exceptions::NetworkCommunicationError] | Thrown when communication with the Parameters Service is unsuccessful. |
| [Autodesk.Revit.Exceptions..::..ResourceNotFoundException](4ef7bcee-5831-e2c9-ee4a-06a0dd6c255f.md "ResourceNotFoundException Class") | Thrown when the requested parameter is not found. |
| [Autodesk.Revit.Exceptions..::..ServerInternalException](dea21550-dd2d-e9d1-4f2f-5f18e0e58bc4.md "ServerInternalException Class") | Thrown when the Parameters Service reports an internal error. |
| [Autodesk.Revit.Exceptions..::..UnauthenticatedException](e94e82b6-4345-48ca-7be9-fd8393b0ff7f.md "UnauthenticatedException Class") | Thrown when the user is not signed in. |

# See Also
[ParameterUtils Class](df5da06e-35c6-e32e-53c0-9fd68d3ab142.md "ParameterUtils Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)