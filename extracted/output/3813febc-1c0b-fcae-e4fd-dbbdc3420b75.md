

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Entity..::..Get<(Of <(<'FieldType>)>)> Method (Field)  
[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Retrieves the value of the field in the entity. 

**Namespace:** [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 

# Syntax

C#  
---  
      
    
    public FieldType Get<FieldType>(
    	[Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.md) field
    )
      
  
Visual Basic  
---  
      
    
    Public Function Get(Of FieldType) ( _
    	field As [Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.md) _
    ) As FieldType  
  
Visual C++  
---  
      
    
    public:
    generic<typename FieldType>
    FieldType Get(
    	[Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.md)^ field
    )  
  
#### Parameters

field
    Type: [Autodesk.Revit.DB.ExtensibleStorage..::..Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.md) The field to retrieve. 

# Type Parameters

FieldType
     The type of the field 

# Remarks

The template parameter must match the type of the field (specified when creating the Schema) exactly; this method does not perform data type conversions. The types for containers are IList for arrays and IDictionary for maps. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | The Field belongs to a different Schema from this Entity, or this Entity is invalid. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | Requested type does not match the field type. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | For floating-point fields, use the overload taking a ForgeTypeId parameter. |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | This field's subschema prevents reading. |
  
# See Also

[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.md)

[Get Overload](08a1c6b1-4635-dd3a-e18a-c4ca56bb7a8b.md)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)