"""Generate XLSX parser configurations."""
from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, FileUrl, create_model, validator
import yaml


# XLS parser configuration
class WorkbookField(BaseModel):
    header: str
    range: str
    type: str
    regexp: Optional[str] = None
    unique: bool = False


class Workbook(BaseModel):
    workbook: FileUrl
    sheet: str
    data_range: str
    data: BaseModel

    @validator("workbook", pre=True)
    def convert_path_to_uri(value: str) -> str:
        """Convert a pathlib.Path to a URI."""
        if Path(value).resolve().exists and not value.startswith("file://"):
            return Path(value).resolve().as_uri()
        return str(value)


def create_config(filename: Union[str, Path]) -> Workbook:
    config = yaml.safe_load(Path(filename).resolve().read_text(encoding="utf8"))
    return create_model(
        "XLSConfig",
        data=(
            create_model(
                "XLSConfigData", **{}.fromkeys(config["data"], (WorkbookField, ...))
            ),
            ...,
        ),
        __base__ = Workbook,
    )(**config)
