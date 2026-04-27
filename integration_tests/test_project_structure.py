from pathlib import Path

def test_project_structure_exists():
    # Resolves to the 'book-recommender/' root directory
    # assuming this file is book-recommender/integration_tests/test_structure.py
    project_root = Path(__file__).resolve().parents[1]

    # The newly defined project structure
    expected_paths = [
        ".dvc",
        ".github/workflows",
        "docs",
        "frontend/src",
        "frontend/tests",
        "backend/src",
        "backend/tests",
        "ml_pipeline/src",
        "ml_pipeline/tests",
        "experiments",
        "infrastructure",
        "integration_tests",
        "models",
        "data",
    ]

    missing_paths = [
        path for path in expected_paths if not (project_root / path).exists()
    ]

    # Will output a clean list of exactly which folders are missing if the test fails
    assert not missing_paths, f"Project structure is missing the following paths: {missing_paths}"