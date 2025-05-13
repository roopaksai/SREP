from dataclasses import dataclass, field
from werkzeug.datastructures import FileStorage


@dataclass
class AboutInput:
    pass


@dataclass
class FlashcardsInput:
    file: FileStorage


@dataclass
class Output:
    output_message: str = field(default_factory=lambda: '')
    output_details: dict = field(default_factory=lambda: {})
    output_status: str = field(default_factory=lambda: 'SUCCESS')
