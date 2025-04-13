

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
IPointCloudAccess..::..GetOffset Method   
[IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Implement this method to return the offset stored in the point cloud. 

**Namespace:** [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 

# Syntax

C#  
---  
      
    
    [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md) GetOffset()  
  
Visual Basic  
---  
      
    
    Function GetOffset As [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)  
  
Visual C++  
---  
      
    
    [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.md)^ GetOffset()  
  
#### Return Value

The offset vector of this point cloud's coordinate system. 

# Remarks

All points are assumed to be offset by the same offset vector. The offset should be expressed in the same units as used by the point coordinates (the scale conversion factor is not applied). The offset will be used by Revit if the user chooses to place an instance relative to another point cloud (the "Auto - Origin To Last Placed" placement option). 

# See Also

[IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.md)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)