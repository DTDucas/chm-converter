

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++  Members: Show All Members: Filtered Members: Filtered Members: Filtered   
---  
  
C#Visual BasicVisual C++

Include Protected MembersInclude Inherited Members

Revit 2024 API  
---  
Subelement Members  
[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.md) Methods Properties See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
The [Subelement](2d15bb45-70af-5f84-e899-322742591251.md) type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
|  | [CanHaveTypeAssigned](dec0c104-7808-4f07-9eb4-c9247cc3a65a.md) | Identifies if the subelement can have a type assigned. |
|  | [ChangeTypeId](4d8ab108-1a74-c4c9-1d84-ef323d246fe1.md) | Changes the type of the subelement. |
|  | [Create](2df166ab-238b-1690-bd3e-2033778b9542.md) | Creates an object representing element or subelement. |
|  | [Dispose](4e7a26fc-f9ec-e77b-cfdf-0f2c009bfb50.md) | Releases all resources used by the [Subelement](2d15bb45-70af-5f84-e899-322742591251.md) |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | [GetAllParameters](f7ee81cc-3a1c-08c8-b495-c562968010cd.md) | Returns all parameters of this subelement. |
|  | [GetBoundingBox](32e76eb1-e305-ead5-0b3b-9eb15891c957.md) | Retrieves a box that circumscribes all geometry of the subelement. |
|  | [GetGeometryObject](be23471b-e6ba-472f-f960-06d7e3dce56a.md) | Retrieve one geometric primitive representing given subelement. |
|  | GetHashCode | Serves as a hash function for a particular type.  (Inherited from Object.) |
|  | [GetParameterValue](c1af0433-3e94-6e40-429b-ad77aaeaff73.md) | Obtains the current parameter value of this subelement given a parameter id. |
|  | [GetReference](62e0779b-25c1-b83a-0a13-ed2bf9cececc.md) | Obtains the reference to this subelement. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | [GetValidTypes](e39919d5-4bca-bdf4-4e24-c73e03cf147a.md) | Obtains a set of types that are valid for this subelement. |
|  | [HasParameter](5725cdbe-5482-b403-f72f-936443e50e83.md) | Checks if this subelement have given parameter. |
|  | [IsParameterModifiable](82d6f753-6e14-3bd1-1fb2-caa284bf4686.md) | Checks if given parameter of this subelement is modifiable. |
|  | [IsValidSubelementReference](89deea46-e7ab-6e7a-a363-665a2eb4b012.md) | Checks if given Reference identifies either a valid element or subelement. |
|  | [IsValidType](b9ab1dbf-2b7b-398a-6682-e2cce94e4352.md) | Checks if given type is valid for this subelement. |
|  | [SetParameterValue](b391bde2-d940-c022-8ab0-a86c7a083b64.md) | Sets a new parameter value of this subelement given a parameter id. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
  
# Properties

|  | Name | Description |
| --- | --- | --- |
|  | [Category](0b0c9dba-f5ce-b20d-f883-5ef39bb4a6a5.md) | Retrieves a Category object that represents the category or sub category of the subelement. |
|  | [Document](5606267f-30e4-bd6c-8e06-43ad1f495585.md) | The document in which the subelement resides. |
|  | [Element](507946d2-87d1-ccc4-d174-7f5e789ceadd.md) | The element in which the subelement resides. |
|  | [IsValidObject](d1cfc136-56e5-614b-8d23-6b5ef2c7c874.md) | Specifies whether the .NET object represents a valid Revit entity. |
|  | [TypeId](3480a4eb-8b80-c694-6a9b-9c5559cac920.md) | The identifier of this subelement's type. |
|  | [UniqueId](2dd5798c-a4cd-edf1-b8c3-52f6cfc7e186.md) | A stable unique identifier for this subelement within the document. |
  
# See Also

[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)