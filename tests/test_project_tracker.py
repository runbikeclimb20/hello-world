import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from project_tracker import Project, MixDesign

def test_single_mix_design_becomes_default():
    project = Project(name="Test Project", location="Location")
    project.add_mix_design(MixDesign("Mix A"))
    assert project.default_mix_design.name == "Mix A"

def test_set_default_mix_design_when_multiple():
    project = Project(name="Test Project", location="Location")
    project.add_mix_design(MixDesign("Mix A"))
    project.add_mix_design(MixDesign("Mix B"))
    project.set_default_mix_design("Mix B")
    assert project.default_mix_design.name == "Mix B"
