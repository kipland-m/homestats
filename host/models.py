from pydantic import BaseModel, Field, field_validator 
from datetime import datetime

# request models
class HardwareInfo(BaseModel):
  cpu_cores: int = Field(..., gt=0)
  cpu_threads: int = Field(..., gt=0)
  cpu_percent: float = Field(..., ge=0, le=100)
  memory_gb: float = Field(..., gt=0)
  disk_gb: float = Field(..., gt=0)

class NetworkInfo(BaseModel):
  ip_address: str
  mac_address: str
  bytes_sent: int = Field(..., gt=0)
  bytes_recv: int = Field(..., gt=0)

  @field_validator('ip_address')
  def validate_ip(cls, v):
    # some ip validation
    parts = v.split('.')
    if len(parts) != 4:
      raise ValueError("IP not valid")
    return v

class AgentData(BaseModel):
  hardware: HardwareInfo
  network: NetworkInfo

class AgentResponse(BaseModel):
   id: int
   timestamp: datetime
   ip_address: str
   mac_address: str
   cpu_cores: int
   cpu_threads: int
   cpu_percent: float
   memory_gb: float
   disk_gb: float
   bytes_sent: int
   bytes_recv: int

class StatsResponse(BaseModel):
   agents: list[AgentResponse] # python 3.9+
   count: int
