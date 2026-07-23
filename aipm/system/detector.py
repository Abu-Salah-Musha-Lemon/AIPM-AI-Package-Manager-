"""
System detector for AIPM.
"""

from __future__ import annotations

import platform
import shutil
import sys

import psutil

from aipm.system.gpu import (
    detect_cuda_version,
    detect_nvidia_gpu,
)

from aipm.system.models import (
    CPUInfo,
    DiskInfo,
    GPUInfo,
    MemoryInfo,
    SystemInfo,
)


def get_cpu_info() -> CPUInfo:
    """
    Collect CPU information.
    """

    return CPUInfo(
        name=platform.processor() or "Unknown",
        cores=psutil.cpu_count(logical=False) or 0,
        threads=psutil.cpu_count(logical=True) or 0,
    )


def get_memory_info() -> MemoryInfo:
    """
    Collect RAM information.
    """

    memory = psutil.virtual_memory()

    return MemoryInfo(
        total=f"{memory.total / (1024**3):.2f} GB",
        available=f"{memory.available / (1024**3):.2f} GB",
    )


def get_disk_info() -> DiskInfo:
    """
    Collect disk information.
    """

    drive = "C:\\" if platform.system() == "Windows" else "/"

    usage = shutil.disk_usage(drive)

    return DiskInfo(
        total=f"{usage.total / (1024**3):.2f} GB",
        free=f"{usage.free / (1024**3):.2f} GB",
    )


def get_gpu_info() -> GPUInfo:
    """
    Detect GPU information.
    """

    gpu = detect_nvidia_gpu()

    cuda_version = detect_cuda_version()

    gpu.cuda_version = cuda_version
    gpu.cuda_available = (
        cuda_version != "Unavailable"
    )

    return gpu


def detect_system() -> SystemInfo:
    """
    Detect complete system information.
    """

    return SystemInfo(
        operating_system=platform.system(),
        release=platform.release(),
        architecture=platform.machine(),
        python_version=sys.version.split()[0],
        cpu=get_cpu_info(),
        memory=get_memory_info(),
        gpu=get_gpu_info(),
        disk=get_disk_info(),
    )