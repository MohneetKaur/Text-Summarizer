# Update Entity

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) # from config.yaml
class DataIngestionConfig:
    root_dir: Path #type
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list