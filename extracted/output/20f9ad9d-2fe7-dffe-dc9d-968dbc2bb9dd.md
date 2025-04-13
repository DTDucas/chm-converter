

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
PropertySetElement..::..GetStructuralAsset Method   
[PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.md) Example See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Gets a copy of the StructuralAsset. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 

# Syntax

C#  
---  
      
    
    public [StructuralAsset](39c2e2ad-474e-2514-bc15-07c24a989a61.md) GetStructuralAsset()  
  
Visual Basic  
---  
      
    
    Public Function GetStructuralAsset As [StructuralAsset](39c2e2ad-474e-2514-bc15-07c24a989a61.md)  
  
Visual C++  
---  
      
    
    public:
    [StructuralAsset](39c2e2ad-474e-2514-bc15-07c24a989a61.md)^ GetStructuralAsset()  
  
# Examples

CopyC#
    
    
    private void ReadMaterialProps(Document document, Material material)
    {
       ElementId strucAssetId = material.StructuralAssetId;
       if (strucAssetId != ElementId.InvalidElementId)
       {
          PropertySetElement pse = document.GetElement(strucAssetId) as PropertySetElement;
          if (pse != null)
          {
             StructuralAsset asset = pse.GetStructuralAsset();
    
             // Check the material behavior and only read if Isotropic
             if (asset.Behavior == StructuralBehavior.Isotropic)
             {
                // Get the class of material
                StructuralAssetClass assetClass = asset.StructuralAssetClass;
    
                // Get other material properties
                double poisson = asset.PoissonRatio.X;
                double youngMod = asset.YoungModulus.X;
                double thermCoeff = asset.ThermalExpansionCoefficient.X;
                double unitweight = asset.Density;
                double shearMod = asset.ShearModulus.X;
    
                if (assetClass == StructuralAssetClass.Metal)
                {
                   double dMinStress = asset.MinimumYieldStress;
                }
                else if (assetClass == StructuralAssetClass.Concrete)
                {
                   double dConcComp = asset.ConcreteCompression;
                }
             }
          }
       }
    }

CopyVB.NET
    
    
    Private Sub ReadMaterialProps(document As Document, material As Material)
        Dim strucAssetId As ElementId = material.StructuralAssetId
        If strucAssetId <> ElementId.InvalidElementId Then
            Dim pse As PropertySetElement = TryCast(document.GetElement(strucAssetId), PropertySetElement)
            If pse IsNot Nothing Then
                Dim asset As StructuralAsset = pse.GetStructuralAsset()
    
                ' Check the material behavior and only read if Isotropic
                If asset.Behavior = StructuralBehavior.Isotropic Then
                    ' Get the class of material
                    Dim assetClass As StructuralAssetClass = asset.StructuralAssetClass
    
                    ' Get other material properties
                    Dim poisson As Double = asset.PoissonRatio.X
                    Dim youngMod As Double = asset.YoungModulus.X
                    Dim thermCoeff As Double = asset.ThermalExpansionCoefficient.X
                    Dim unitweight As Double = asset.Density
                    Dim shearMod As Double = asset.ShearModulus.X
    
                    If assetClass = StructuralAssetClass.Metal Then
                        Dim dMinStress As Double = asset.MinimumYieldStress
                    ElseIf assetClass = StructuralAssetClass.Concrete Then
                        Dim dConcComp As Double = asset.ConcreteCompression
                    End If
                End If
            End If
        End If
    End Sub

# See Also

[PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)