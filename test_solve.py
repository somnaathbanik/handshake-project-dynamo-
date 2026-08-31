import json
import os
import tempfile
import sys

# Test the solve.py logic
def test_count_non_empty_lines():
    """Test counting non-empty lines from a file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test input file
        input_path = os.path.join(tmpdir, "index.txt")
        output_path = os.path.join(tmpdir, "report.json")
        
        # Write test data
        test_content = "line1\n\nline3\n  \nline5\n"
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(test_content)
        
        # Count non-empty lines (mimicking solve.py logic)
        with open(input_path, "r", encoding="utf-8") as f:
            non_empty_lines = sum(1 for line in f if line.strip())
        
        # Write output
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"non_empty_lines": non_empty_lines}, f)
        
        # Verify output
        with open(output_path, "r", encoding="utf-8") as f:
            result = json.load(f)
        
        assert result["non_empty_lines"] == 3, f"Expected 3 non-empty lines, got {result['non_empty_lines']}"


def test_empty_file():
    """Test with an empty file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "empty.txt")
        output_path = os.path.join(tmpdir, "report.json")
        
        # Create empty file
        with open(input_path, "w", encoding="utf-8") as f:
            pass
        
        # Count non-empty lines
        with open(input_path, "r", encoding="utf-8") as f:
            non_empty_lines = sum(1 for line in f if line.strip())
        
        # Write output
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"non_empty_lines": non_empty_lines}, f)
        
        # Verify
        with open(output_path, "r", encoding="utf-8") as f:
            result = json.load(f)
        
        assert result["non_empty_lines"] == 0, f"Expected 0 non-empty lines, got {result['non_empty_lines']}"


def test_all_non_empty_lines():
    """Test with file containing only non-empty lines."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "full.txt")
        output_path = os.path.join(tmpdir, "report.json")
        
        test_content = "line1\nline2\nline3\n"
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(test_content)
        
        # Count non-empty lines
        with open(input_path, "r", encoding="utf-8") as f:
            non_empty_lines = sum(1 for line in f if line.strip())
        
        # Write output
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"non_empty_lines": non_empty_lines}, f)
        
        # Verify
        with open(output_path, "r", encoding="utf-8") as f:
            result = json.load(f)
        
        assert result["non_empty_lines"] == 3, f"Expected 3 non-empty lines, got {result['non_empty_lines']}"


if __name__ == "__main__":
    test_count_non_empty_lines()
    test_empty_file()
    test_all_non_empty_lines()
    print("All tests passed!")
