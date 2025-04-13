

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
TessellatedShapeBuilder..::..AreTargetAndFallbackCompatible Method   
[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Checks whether this combination of fallback and target parameters can be used as a valid combination of inputs. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2015 

# Syntax

C#  
---  
      
    
    public bool AreTargetAndFallbackCompatible(
    	[TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.md) target,
    	[TessellatedShapeBuilderFallback](ce755fa3-8727-2cd3-dbc3-c952bdc83a17.md) fallback
    )  
  
Visual Basic  
---  
      
    
    Public Function AreTargetAndFallbackCompatible ( _
    	target As [TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.md), _
    	fallback As [TessellatedShapeBuilderFallback](ce755fa3-8727-2cd3-dbc3-c952bdc83a17.md) _
    ) As Boolean  
  
Visual C++  
---  
      
    
    public:
    bool AreTargetAndFallbackCompatible(
    	[TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.md) target, 
    	[TessellatedShapeBuilderFallback](ce755fa3-8727-2cd3-dbc3-c952bdc83a17.md) fallback
    )  
  
#### Parameters

target
    Type: [Autodesk.Revit.DB..::..TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.md) What kind of geometrical objects should be built. 

fallback
    Type: [Autodesk.Revit.DB..::..TessellatedShapeBuilderFallback](ce755fa3-8727-2cd3-dbc3-c952bdc83a17.md) What should be done if a geometrical object described by 'target' parameter cannot be built using all data from all stored face sets. 

#### Return Value

True if the combination of fallback and target are a valid combination, false otherwise. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | A value passed for an enumeration argument is not a member of that enumeration |
  
# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)