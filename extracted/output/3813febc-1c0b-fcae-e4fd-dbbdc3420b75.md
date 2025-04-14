# Get(FieldType) Method (Field)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
Entity..::..Get<(Of <(<'FieldType>)>)> Method (Field)  
[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.md "Entity Class") See Also  
---  
Retrieves the value of the field in the entity. 
**Namespace:** [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.md "Autodesk.Revit.DB.ExtensibleStorage Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public FieldType Get<FieldType>(
	Field field
)

```
  
Visual Basic  
---  
```text
Public Function Get(Of FieldType) ( _
	field As Field _
) As FieldType
```
  
Visual C++  
---  
```text
public:
generic<typename FieldType>
FieldType Get(
	Field^ field
)
```
  
# ### Parameters
field
    Type: [Autodesk.Revit.DB.ExtensibleStorage..::..Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.md "Field Class") The field to retrieve. 
# Type Parameters
FieldType
     The type of the field 
# Remarks
The template parameter must match the type of the field (specified when creating the Schema) exactly; this method does not perform data type conversions. The types for containers are IList for arrays and IDictionary for maps. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The Field belongs to a different Schema from this Entity, or this Entity is invalid. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Requested type does not match the field type. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | For floating-point fields, use the overload taking a ForgeTypeId parameter. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | This field's subschema prevents reading. |

# See Also
[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.md "Entity Class")
[Get Overload](08a1c6b1-4635-dd3a-e18a-c4ca56bb7a8b.md "Get Method")
[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.md "Autodesk.Revit.DB.ExtensibleStorage Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)