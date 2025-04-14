# GetObjectData Method

﻿
 Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++   
---  
C#Visual BasicVisual C++
Revit 2024 API  
---  
ObjectAccessException..::..GetObjectData Method   
[ObjectAccessException Class](7d69a00b-f531-c575-0e55-ea2f3858560d.md "ObjectAccessException Class") See Also  
---  
Retrieves data needed to serialize the target object.
**Namespace:** [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md "Autodesk.Revit.Exceptions Namespace")**Assembly:** RevitAPI (in RevitAPI.dll) Version: 24.0.0.0 (24.0.0.0)
# Syntax
C#  
---  
```text
public override void GetObjectData(
	SerializationInfo info,
	StreamingContext context
)
```
  
Visual Basic  
---  
```text
Public Overrides Sub GetObjectData ( _
	info As SerializationInfo, _
	context As StreamingContext _
)
```
  
Visual C++  
---  
```text
public:
virtual void GetObjectData(
	SerializationInfo^ info, 
	StreamingContext context
) override
```
  
# ### Parameters
info
    Type: System.Runtime.Serialization..::..SerializationInfo Data needed to serialize or deserialize the object. 
context
    Type: System.Runtime.Serialization..::..StreamingContext The destination of the serialized stream. 
# ### Implements
ISerializable..::..GetObjectData(SerializationInfo, StreamingContext)_Exception..::..GetObjectData(SerializationInfo, StreamingContext)
# See Also
[ObjectAccessException Class](7d69a00b-f531-c575-0e55-ea2f3858560d.md "ObjectAccessException Class")
[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.md "Autodesk.Revit.Exceptions Namespace")
Send comments on this topic to [Autodesk](mailto:revitapifeedback%40autodesk.com?Subject=Revit 2024 API)