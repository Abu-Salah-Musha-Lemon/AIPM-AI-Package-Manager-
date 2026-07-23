"""
GPU detection utilities for AIPM.
"""

from __future__ import annotations

import subprocess

from aipm.system.models import GPUInfo


def detect_nvidia_gpu() -> GPUInfo:
    """
    Detect NVIDIA GPU using nvidia-smi.
    """

    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total,driver_version",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=5,
        )

        if result.returncode != 0:
            return GPUInfo()

        output = result.stdout.strip()

        if not output:
            return GPUInfo()

        data = output.split(",")

        return GPUInfo(
            name=data[0].strip(),
            vendor="NVIDIA",
            memory=f"{data[1].strip()} MB",
            driver=data[2].strip(),
        )

    except (
        FileNotFoundError,
        subprocess.TimeoutExpired,
    ):
        return GPUInfo()


def detect_cuda_version() -> str:
    """
    Detect CUDA version using nvidia-smi.
    """

    try:
        result = subprocess.run(
            [
                "nvidia-smi",
            ],
            capture_output=True,
            text=True,
            timeout=5,
        )

        if result.returncode != 0:
            return "Unavailable"

        output = result.stdout

        for line in output.splitlines():

            if "CUDA Version" in line:

                return (
                    line.split("CUDA Version:")[1]
                    .split()[0]
                    .strip()
                )

    except (
        FileNotFoundError,
        subprocess.TimeoutExpired,
    ):
        pass

    return "Unavailable"