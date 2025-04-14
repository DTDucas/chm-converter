# GetStructuralAsset Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
PropertySetElement..::..GetStructuralAsset Method   
[PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.md "PropertySetElement Class") Example See Also  
---  
Gets a copy of the StructuralAsset. 
**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2012 
# Syntax
C#  
---  
```text
public StructuralAsset GetStructuralAsset()
```
  
Visual Basic  
---  
```text
Public Function GetStructuralAsset As StructuralAsset
```
  
Visual C++  
---  
```text
public:
StructuralAsset^ GetStructuralAsset()
```
  
# Examples
CopyC#
```text
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
```

CopyVB.NET
```text
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
```

# See Also
[PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.md "PropertySetElement Class")
[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md "Autodesk.Revit.DB Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)