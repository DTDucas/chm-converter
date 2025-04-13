

Collapse AllExpand All Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
  
C#Visual BasicVisual C++

Revit 2024 API  
---  
RoutingPreferenceManager..::..AddRule Method (RoutingPreferenceRuleGroupType, RoutingPreferenceRule, Int32)  
[RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.md) See Also [Send Feedback](javascript:SubmitFeedback\('revitapifeedback@autodesk.com','Revit 2024 API','','','','%0\\dYour%20feedback%20is%20used%20to%20improve%20the%20documentation%20and%20the%20product.%20Your%20e-mail%20address%20will%20not%20be%20used%20for%20any%20other%20purpose%20and%20is%20disposed%20of%20after%20the%20issue%20you%20report%20is%20resolved.%20%20While%20working%20to%20resolve%20the%20issue%20that%20you%20report,%20you%20may%20be%20contacted%20via%20e-mail%20to%20get%20further%20details%20or%20clarification%20on%20the%20feedback%20you%20sent.%20After%20the%20issue%20you%20report%20has%20been%20addressed,%20you%20may%20receive%20an%20e-mail%20to%20let%20you%20know%20that%20your%20feedback%20has%20been%20addressed.%0\\A%0\\d','Customer%20Feedback'\);)  
---  
  
Adds a new routing preference rule to the specified position in the rule group. 

**Namespace:** [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)**Since:** 2013 

# Syntax

C#  
---  
      
    
    public void AddRule(
    	[RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.md) groupType,
    	[RoutingPreferenceRule](28dd1a35-5115-c0fb-26e3-7bce14893b89.md) rule,
    	int index
    )  
  
Visual Basic  
---  
      
    
    Public Sub AddRule ( _
    	groupType As [RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.md), _
    	rule As [RoutingPreferenceRule](28dd1a35-5115-c0fb-26e3-7bce14893b89.md), _
    	index As Integer _
    )  
  
Visual C++  
---  
      
    
    public:
    void AddRule(
    	[RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.md) groupType, 
    	[RoutingPreferenceRule](28dd1a35-5115-c0fb-26e3-7bce14893b89.md)^ rule, 
    	int index
    )  
  
#### Parameters

groupType
    Type: [Autodesk.Revit.DB..::..RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.md) The routing preference group type in which the rule should be added. 

rule
    Type: [Autodesk.Revit.DB..::..RoutingPreferenceRule](28dd1a35-5115-c0fb-26e3-7bce14893b89.md) The new rule to be added. 

index
    Type: System..::..Int32 The zero-based index position where the new rule will be added. 

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions..::..ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.md) | index is not a valid zero-based index within groupType. -or- The rule cannot be added to the groupType. -or- Thrown if the index is out of bounds, or the rule is not valid for this group (e.g. an elbow may not be added to the junction group). |
| [Autodesk.Revit.Exceptions..::..ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.md) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions..::..ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.md) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions..::..DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.md) | None of the following disciplines is enabled: Mechanical Electrical Piping. |
  
# See Also

[RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.md)

[AddRule Overload](06817419-419d-35bf-8538-3584e415a1c4.md)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.md)

Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)