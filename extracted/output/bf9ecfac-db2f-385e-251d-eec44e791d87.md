

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
ElectricalSystem..::..Create Method (Connector, ElectricalSystemType)  
[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Creates a new MEP Electrical System element from an unused Connector. 

**Namespace:** [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2018 

# Syntax

C#  
---  
      
    
    public static [ElectricalSystem](158b4be3-bbe5-11eb-cccc-788edd3a7590.md) Create(
    	[Connector](11e07082-b3f2-26a1-de79-16535f44716c.md) connector,
    	[ElectricalSystemType](90f62108-9cd1-a66a-a123-8372307f4e7f.md) elecSysType
    )  
  
Visual Basic  
---  
      
    
    Public Shared Function Create ( _
    	connector As [Connector](11e07082-b3f2-26a1-de79-16535f44716c.md), _
    	elecSysType As [ElectricalSystemType](90f62108-9cd1-a66a-a123-8372307f4e7f.md) _
    ) As [ElectricalSystem](158b4be3-bbe5-11eb-cccc-788edd3a7590.md)  
  
Visual C++  
---  
      
    
    public:
    static [ElectricalSystem](158b4be3-bbe5-11eb-cccc-788edd3a7590.md)^ Create(
    	[Connector](11e07082-b3f2-26a1-de79-16535f44716c.md)^ connector, 
    	[ElectricalSystemType](90f62108-9cd1-a66a-a123-8372307f4e7f.md) elecSysType
    )  
  
#### Parameters

connector
    Type: [Autodesk.Revit.DB..::..Connector](11e07082-b3f2-26a1-de79-16535f44716c.md) The Connector to create this Electrical System. 

elecSysType
    Type: [Autodesk.Revit.DB.Electrical..::..ElectricalSystemType](90f62108-9cd1-a66a-a123-8372307f4e7f.md) The System Type of electrical system. 

#### Return Value

If successful a new MEP Electrical System element within the project, otherwise nullNothingnullptra null reference (Nothing in Visual Basic). 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md) | None of the following disciplines is enabled: Mechanical Electrical Piping. |
  
# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.md)

[Create Overload](b3ea7251-7230-ac0a-d5cc-0806b0c0ec1e.md)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)