from pydantic.dataclasses import dataclass

# Setup all of the parameters
@dataclass
class P_Type:
    value: str
    spec_version: str

@dataclass
class P_String:
    fixed: str
    required: bool

@dataclass
class P_ID:
    value: str

@dataclass
class P_Temporal:
    default: str 
    precision: str
    precision_contraint: str
    
@dataclass
class P_Reference:
    valid_types: str
    spec_version: str

@dataclass
class P_Boolean:
    default: str

@dataclass
class P_Integer:
    mind: int




# Setup all of the properties
@dataclass
class Property:
    name: str
    type: str

class StringProperty(Property):
    parameters: P_String

class TmestampProperty(Property):
    parameters: P_Temporal

class TypeProperty(Property):
    parameters: P_Type




