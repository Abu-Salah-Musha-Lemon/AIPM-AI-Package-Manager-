"""
System information models for AIPM.
"""

from __future__ import annotations

from pydantic import BaseModel


class CPUInfo(BaseModel):
    """
    CPU information.
    """

    name: str
    cores: int
    threads: int


class MemoryInfo(BaseModel):
    """
    RAM information.
    """

    total: str
    available: str


class GPUInfo(BaseModel):
    """
    GPU information.
    """

    name: str = "Unknown"
    vendor: str = "Unknown"
    memory: str = "Unknown"
    driver: str = "Unknown"
    cuda_available: bool = False
    cuda_version: str = "Unavailable"


class DiskInfo(BaseModel):
    """
    Disk information.
    """

    total: str
    free: str


class SystemInfo(BaseModel):
    """
    Complete system information.
    """

    operating_system: str
    release: str
    architecture: str
    python_version: str

    cpu: CPUInfo
    memory: MemoryInfo
    gpu: GPUInfo
    disk: DiskInfo