

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
FamilyManager..::..AddParameter Method (ExternalDefinition, ForgeTypeId, Boolean)  
[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Add a new shared parameter to the family.

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)

# Syntax

C#  
---  
      
    
    public [FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.md) AddParameter(
    	[ExternalDefinition](a3e84415-b88e-a8e0-4e11-64795d92da0e.md) familyDefinition,
    	[ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md) groupTypeId,
    	bool isInstance
    )  
  
Visual Basic  
---  
      
    
    Public Function AddParameter ( _
    	familyDefinition As [ExternalDefinition](a3e84415-b88e-a8e0-4e11-64795d92da0e.md), _
    	groupTypeId As [ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md), _
    	isInstance As Boolean _
    ) As [FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.md)  
  
Visual C++  
---  
      
    
    public:
    [FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.md)^ AddParameter(
    	[ExternalDefinition](a3e84415-b88e-a8e0-4e11-64795d92da0e.md)^ familyDefinition, 
    	[ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md)^ groupTypeId, 
    	bool isInstance
    )  
  
#### Parameters

familyDefinition
    Type: [Autodesk.Revit.DB..::..ExternalDefinition](a3e84415-b88e-a8e0-4e11-64795d92da0e.md)The definition of the loaded shared parameter.

groupTypeId
    Type: [Autodesk.Revit.DB..::..ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.md) The identifier of the parameter group to which the family parameter belongs. 

isInstance
    Type: System..::..BooleanIndicates if the new parameter is instance or type.

#### Return Value

If creation was successful the new shared parameter is returned, otherwise an exception with failure information will be thrown.

# Remarks

This method can work even without any family type, but it cannot be assigned the value via FamilyManager.Set methods when there is no current type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | Thrown when the input parameter group cannot be assigned to the new parameter. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Thrown when the shared family parameter creation is not supported. Or trying to add an instance parameter of image type. |
  
# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.md)

[AddParameter Overload](fb4f8475-440f-6454-768f-777388a7fdd4.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)