

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ElectricalSystem..::..SelectPanel Method   
[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Set the panel for the Electrical System. 

**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2011 

# Syntax

C#  
---  
      
    
    public void SelectPanel(
    	[FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md) panel
    )  
  
Visual Basic  
---  
      
    
    Public Sub SelectPanel ( _
    	panel As [FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md) _
    )  
  
Visual C++  
---  
      
    
    public:
    void SelectPanel(
    	[FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md)^ panel
    )  
  
#### Parameters

panel
    Type: [Autodesk.Revit.DB..::..FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.md) The panel of the electrical system. 

# Remarks

If successful, the panel will be set for the system. Otherwise the exception will be thrown. This method will only function with the Autodesk Revit MEP application. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md) | None of the following disciplines is enabled: Mechanical Electrical Piping. |
| [Autodesk.Revit.Exceptions..::..InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.md) | The panel does not have enough slots and Feed Through Lugs is unchecked or already in use. -or- Thrown when the panel cannot be set for the electrical system. |
  
# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)