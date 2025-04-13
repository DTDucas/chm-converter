

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ExternalResourceUIBrowseResultType Enumeration  
See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Describes the type of external resource browsing result. 

Describes the type of external resource browsing result. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 **Since:** 2015 

# Syntax

C#  
---  
      
    
    public enum ExternalResourceUIBrowseResultType  
  
Visual Basic  
---  
      
    
    Public Enumeration ExternalResourceUIBrowseResultType  
  
Visual C++  
---  
      
    
    public enum class ExternalResourceUIBrowseResultType  
  
# Members

| Member name | Description |
| --- | --- |
| Success | There is no predefined error happened during this browse operation. The DB server can store any errors itself in this case. |
| FolderNotFound | The specified external resource folder cannot be found by external resource server. |
| ResourceNotFound | The specified external resource cannot be found by external resource server. |
  
# Remarks

This enum is used to describe the type of external resources browsing operation result ( the browsing operation include list folders and resources of an external server or a folder, or open an external resource in browsing dialog.) The meaning of each enum value: 

  * There is no predefined error happened during this browse operation. The DB server can store any errors itself in this case. 
  * FolderNotFound means the external resource folder want to browse could not be founded in external server.
  * ResourceNotFound means the external resource want to open could not be founded in external server.



# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)