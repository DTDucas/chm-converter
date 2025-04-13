

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
Document..::..SaveAsCloudModel Method   
[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Saves current non-workshared or workshared model as a cloud model or workshared cloud model in BIM 360 Docs or Autodesk Docs. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2021 

# Syntax

C#  
---  
      
    
    public void SaveAsCloudModel(
    	Guid accountId,
    	Guid projectId,
    	string folderId,
    	string modelName
    )  
  
Visual Basic  
---  
      
    
    Public Sub SaveAsCloudModel ( _
    	accountId As Guid, _
    	projectId As Guid, _
    	folderId As String, _
    	modelName As String _
    )  
  
Visual C++  
---  
      
    
    public:
    void SaveAsCloudModel(
    	Guid accountId, 
    	Guid projectId, 
    	String^ folderId, 
    	String^ modelName
    )  
  
#### Parameters

accountId
    Type: System..::..Guid The BIM 360 Docs or Autodesk Docs account Id. You can use one of the following methods to get this Id: 

  * If you get the hub Id with Forge Data Management API, remove the prefix "b." of the Id string and convert the rest to a Guid. 
  * If you get the account Id with Forge BIM 360 Docs or Autodesk Docs API, just convert the Id string to a Guid. 



projectId
    Type: System..::..Guid The BIM 360 Docs or Autodesk Docs project Id. You can use one of the following methods to get this Id: 

  * If you get the project Id with Forge Data Management API, remove the prefix "b." of the Id string and convert the rest to a Guid. 
  * If you get the project Id with Forge BIM 360 Docs or Autodesk Docs API, just convert the Id string to a Guid. 



folderId
    Type: System..::..String Folder identity in BIM 360 Docs or Autodesk Docs to save the model. You can use one of the following methods to get this Id: 

  * The folder Id string from Forge Data Management API. 
  * The folder Id string from Forge BIM 360 Docs or Autodesk Docs API. 



modelName
    Type: System..::..String Model name in BIM 360 Docs or Autodesk Docs to save the model. 

# Remarks

Assumes that user is currently signed in BIM 360 Docs or Autodesk Docs and has access to Autodesk cloud services. This operation will create a model on cloud and then create a local cache of the cloud model. This method cannot be used when current document is already in cloud. 

You can use one of the following methods to save a local model as a workshared cloud model in BIM 360 Docs or Autodesk Docs. 

  * If the local model is a workshared model, then it will be a workshared cloud model after you use this method successfully. 
  * If the local model is a non-workshared model, you can enable the workset with [EnableWorksharing(String, String)](7c29717e-1d8c-4e02-20ad-65c53ea8eaaa.md) and then save as a workshared cloud model. 
  * If the local model is a non-workshared model, and you have already saved it as a non-workshared cloud model in BIM 360 Docs or Autodesk Docs, you can still enable the workset with [EnableCloudWorksharing()()()()](4146e816-565e-85d8-ce94-93ec505a0924.md) to convert it to a workshared cloud model. 



You cannot save a local workshared model as a non-workshared cloud model in BIM 360 Docs or Autodesk Docs.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | folderId is an empty string. -or- modelName is an empty string. -or- The input file name "modelName" does not represent a valid file name. -or- Thrown when the input BIM 360 Docs or Autodesk Docs account Id or project Id is invalid or unmatched. |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.md) | SaveAs may not be called during dynamic update. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | Saving is not allowed in the current application mode. -or- This Document is not a project document. -or- This Document is in an edit mode. -or- This Document is not a primary document, it is a linked document. -or- SaveAs is temporarily disabled. -or- This Document is a cloud model, cannot be saved as a cloud model. -or- There is a transaction phase left open (such as a transaction, sub-transaction of transaction group) at the time of invoking this method. |
| [Autodesk.Revit.Exceptions..::..RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.md) | Could be for any of the reasons related to network. |
| [Autodesk.Revit.Exceptions..::..RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.md) | Could be for any of the reasons that saveAs fails with RevitServerInternalException. |
| [Autodesk.Revit.Exceptions..::..RevitServerModelAlreadyExistsException](a3ed0157-0a46-0b62-62db-08112e1645bd.md) | Failed due to there is a model with the same name already exists at the specified location. |
| [Autodesk.Revit.Exceptions..::..RevitServerModelNameBreaksConventionException](ec0e702a-f076-1b44-4277-feefd39045d4.md) | Failed due to the model name is breaking project naming convention. |
| [Autodesk.Revit.Exceptions..::..RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.md) | User is not signed in with Autodesk id. |
| [Autodesk.Revit.Exceptions..::..RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.md) | You don't have the entitlement to perform the operation to this this Document. -or- User is not authorized to access the specified cloud project. |
  
# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)