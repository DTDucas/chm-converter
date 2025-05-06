# Set(FieldType) Method (Field, FieldType) (2023)

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2023 API  
---  
Entity..::..Set<(Of <(<'FieldType>)>)> Method (Field, FieldType)  
[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.md "Entity Class") See Also  
---  
Stores the value of the field in the entity. 
**Namespace:** [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.md "Autodesk.Revit.DB.ExtensibleStorage Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public void Set<FieldType>(
	Field field,
	FieldType value
)

```
  
Visual Basic  
---  
```text
Public Sub Set(Of FieldType) ( _
	field As Field, _
	value As FieldType _
)
```
  
Visual C++  
---  
```text
public:
generic<typename FieldType>
void Set(
	Field^ field, 
	FieldType value
)
```
  
# ### Parameters
field
    Type: [Autodesk.Revit.DB.ExtensibleStorage..::..Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.md "Field Class") The field to update. 
value
    Type: FieldType
# Type Parameters
FieldType
     The type of the field 
# Remarks
The template parameter must match the type of the field (specified when creating the Schema) exactly; this method does not perform data type conversions. The types for containers are IList for arrays and IDictionary for maps. 
Note that when string values are specified as map keys, they are case-insensitive. 
This method only modifies your copy of the Entity. Store the Entity in an element or another Entity to save the new value. Write access check is not performed on each call to Set. Instead, write access is checked when you try to save the Entity in an Element or another Entity. 
# Exceptions
| Exception | Condition |
| --- | --- |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md "ArgumentNullException Class") | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md "InvalidOperationException Class") | The Field belongs to a different Schema from this Entity, or this Entity is invalid. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Requested type does not match the field type. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | For floating-point fields, use the overload taking a ForgeTypeId parameter. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | This field's subschema prevents writing. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | Invalid floating-point value. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md "ArgumentException Class") | String is too long; exceeds max length of 16mb characters. |

# See Also
[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.md "Entity Class")
[Set Overload](ca7fbcad-94aa-40a0-f77d-1f78c5ecf705.md "Set Method")
[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.md "Autodesk.Revit.DB.ExtensibleStorage Namespace")
Send comments on this topic to 