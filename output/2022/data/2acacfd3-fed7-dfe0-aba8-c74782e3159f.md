# Type Property (2022)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2022 API  
---  
ExternalDefinitionCreationOptions..::..Type Property   
[ExternalDefinitionCreationOptions Class](1cd9e425-23a3-04f8-c130-4d4a799abd13.md "ExternalDefinitionCreationOptions Class") See Also  
---  
The type of the parameter definition to be created. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)**Since:** 2015 
# Syntax
C#  
---  
```text
[ObsoleteAttribute("This property is deprecated in Revit 2022 and may be removed in a future version of Revit. Please use the GetDataType() and SetDataType(ForgeTypeId) methods instead.")]
public ParameterType Type { get; set; }
```
  
Visual Basic  
---  
```text
<ObsoleteAttribute("This property is deprecated in Revit 2022 and may be removed in a future version of Revit. Please use the GetDataType() and SetDataType(ForgeTypeId) methods instead.")> _
Public Property Type As ParameterType
	Get
	Set
```
  
Visual C++  
---  
```text
[ObsoleteAttribute(L"This property is deprecated in Revit 2022 and may be removed in a future version of Revit. Please use the GetDataType() and SetDataType(ForgeTypeId) methods instead.")]
public:
property ParameterType Type {
	ParameterType get ();
	void set (ParameterType value);
}
```
  
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | When setting this property: e cannot be Invalid or FamilyType. |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md "ArgumentOutOfRangeException Class") | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also
[ExternalDefinitionCreationOptions Class](1cd9e425-23a3-04f8-c130-4d4a799abd13.md "ExternalDefinitionCreationOptions Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to 