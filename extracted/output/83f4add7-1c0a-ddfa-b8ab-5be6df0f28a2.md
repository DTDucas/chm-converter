

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RevitLinkType..::..Unload Method   
[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Unloads the Revit link. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2014 

# Syntax

C#  
---  
      
    
    public void Unload(
    	[ISaveSharedCoordinatesCallback](ed4eac2a-d482-7760-2ae7-855611d09c46.md) callback
    )  
  
Visual Basic  
---  
      
    
    Public Sub Unload ( _
    	callback As [ISaveSharedCoordinatesCallback](ed4eac2a-d482-7760-2ae7-855611d09c46.md) _
    )  
  
Visual C++  
---  
      
    
    public:
    void Unload(
    	[ISaveSharedCoordinatesCallback](ed4eac2a-d482-7760-2ae7-855611d09c46.md)^ callback
    )  
  
#### Parameters

callback
    Type: [Autodesk.Revit.DB..::..ISaveSharedCoordinatesCallback](ed4eac2a-d482-7760-2ae7-855611d09c46.md) A callback indicating what to do if Revit encounters links which have changes in shared coordinates. If nullNothingnullptra null reference (Nothing in Visual Basic), Revit will not save any shared coordinates changes to the link before unloading. 

# Remarks

This function regenerates the document.

The document's Undo history will be cleared by this command. As a result, this command and others executed before it cannot be undone. All transaction phases (e.g. transactions transaction groups and sub-transaction) that were explicitly started must be finished prior to calling this method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.md) | The function is not permitted during dynamic update. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | This RevitLinkType is not a top-level link. -or- Revit could not save shared coordinates changes to the link or one of its nested links. -or- There is a transaction phase left open (such as a transaction, sub-transaction of transaction group) at the time of invoking this method. -or- The document is read-only. It cannot be modified. -or- The document is in an edit mode or is in family mode. -or- Revit cannot link a cloud model to non-cloud model |
| [Autodesk.Revit.Exceptions..::..RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.md) | Could be for any of the reasons that failed on service side. |
| [Autodesk.Revit.Exceptions..::..RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.md) | User is not signed in with Autodesk id. |
| [Autodesk.Revit.Exceptions..::..RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.md) | User is not authorized to access the specified cloud model. |
  
# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)