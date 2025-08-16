from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MixDesign:
    """Represents a concrete mix design."""
    name: str


@dataclass
class Project:
    """Represents a project with concrete mix designs."""
    name: str
    location: str
    mix_designs: List[MixDesign] = field(default_factory=list)
    default_mix_design: Optional[MixDesign] = None

    def add_mix_design(self, mix_design: MixDesign, *, is_default: bool = False) -> None:
        """Add a mix design to the project.

        The first mix design added becomes the default unless another default
        is explicitly specified.
        """
        self.mix_designs.append(mix_design)
        if is_default or len(self.mix_designs) == 1:
            self.default_mix_design = mix_design

    def set_default_mix_design(self, mix_design_name: str) -> None:
        """Set the default mix design by name.

        Raises:
            ValueError: If the mix design name does not exist in the project.
        """
        for md in self.mix_designs:
            if md.name == mix_design_name:
                self.default_mix_design = md
                return
        raise ValueError(f"Mix design '{mix_design_name}' not found.")


def create_project_from_input() -> Project:
    """Interactively create a project via command-line inputs."""
    name = input("Project name: ")
    location = input("Project location: ")
    project = Project(name=name, location=location)

    while True:
        add_mix = input("Add a mix design? (y/n): ").strip().lower()
        if add_mix != 'y':
            break
        mix_name = input("Mix design name: ").strip()
        project.add_mix_design(MixDesign(name=mix_name))

    if len(project.mix_designs) > 1:
        default_name = input("Select default mix design: ").strip()
        project.set_default_mix_design(default_name)

    print("\nCreated Project:")
    print(f"Name: {project.name}")
    print(f"Location: {project.location}")
    print("Mix Designs:")
    for md in project.mix_designs:
        default_marker = " (default)" if md == project.default_mix_design else ""
        print(f" - {md.name}{default_marker}")
    return project


if __name__ == "__main__":
    create_project_from_input()
