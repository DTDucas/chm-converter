

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
MEPAnalyticalModelData..::..GetNodeByIndex Method   
[MEPAnalyticalModelData Class](9bb95365-04a3-6c28-5f72-477facd80cbc.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Gets the specified analytical node. 

**Namespace:** [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2024 

# Syntax

C#  
---  
      
    
    public [MEPAnalyticalNode](d542aa13-f6a7-087c-9660-b0698d303a0c.md) GetNodeByIndex(
    	int index
    )  
  
Visual Basic  
---  
      
    
    Public Function GetNodeByIndex ( _
    	index As Integer _
    ) As [MEPAnalyticalNode](d542aa13-f6a7-087c-9660-b0698d303a0c.md)  
  
Visual C++  
---  
      
    
    public:
    [MEPAnalyticalNode](d542aa13-f6a7-087c-9660-b0698d303a0c.md)^ GetNodeByIndex(
    	int index
    )  
  
#### Parameters

index
    Type: System..::..Int32 The node index number by their storing sequence, starting from 0. 

#### Return Value

The returned analytical node. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | The index must range from 0 to GetNumberOfNodes()-1. |
  
# See Also

[MEPAnalyticalModelData Class](9bb95365-04a3-6c28-5f72-477facd80cbc.md)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)