import json
import os
from pathlib import Path

def format_json_preview(data, max_lines=20):
    """Format JSON data with a preview of first few lines"""
    formatted = json.dumps(data, indent=2).split('\n')
    if len(formatted) > max_lines:
        return '\n'.join(formatted[:max_lines] + ['...', '}'])
    return '\n'.join(formatted)

def generate_summary():
    samples_dir = Path(__file__).parent / 'samples'
    output_file = Path(__file__).parent / 'betsapi_samples_summary.txt'
    
    summary = []
    summary.append("BetsAPI JSON Samples Summary")
    summary.append("=========================\n")
    
    # Get all JSON files and sort them
    json_files = sorted(samples_dir.glob('*.json'))
    
    for json_path in json_files:
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            # Add file header
            filename = json_path.name
            filesize = json_path.stat().st_size / 1024  # size in KB
            
            summary.append(f"\n{filename}")
            summary.append("=" * len(filename))
            summary.append(f"Size: {filesize:.2f} KB\n")
            
            # Add JSON preview
            summary.append("Content Preview:")
            summary.append("```json")
            summary.append(format_json_preview(data))
            summary.append("```")
            summary.append("-" * 80 + "\n")
            
        except Exception as e:
            summary.append(f"Error processing {filename}: {str(e)}\n")
    
    # Write the summary to a file
    with open(output_file, 'w') as f:
        f.write('\n'.join(summary))
    
    print(f"Summary generated at: {output_file}")

if __name__ == "__main__":
    generate_summary()
