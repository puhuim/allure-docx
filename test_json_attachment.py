#!/usr/bin/env python3
"""
Test script to verify JSON attachment handling
"""

import os
import json
import tempfile
from src.allure_docx.report_builder import ReportBuilder
from src.allure_docx.config import ReportConfig

def create_test_json_attachment():
    """Create a test JSON attachment"""
    # Create a temporary directory for test
    test_dir = tempfile.mkdtemp()
    
    # Create a test JSON file
    test_data = {
        "test_name": "JSON Attachment Test",
        "status": "passed",
        "data": {
            "key1": "value1",
            "key2": "value2",
            "nested": {
                "inner_key": "inner_value"
            }
        },
        "timestamp": "2024-01-01T12:00:00Z"
    }
    
    json_file_path = os.path.join(test_dir, "test-attachment.json")
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, indent=2)
    
    # Create a test result JSON
    test_result = {
        "name": "Test with JSON attachment",
        "status": "passed",
        "attachments": [
            {
                "name": "Test Data",
                "source": "test-attachment.json",
                "type": "application/json"
            }
        ],
        "start": 1673462593561,
        "stop": 1673462593562
    }
    
    result_file_path = os.path.join(test_dir, "test-result.json")
    with open(result_file_path, 'w', encoding='utf-8') as f:
        json.dump(test_result, f)
    
    return test_dir

def test_json_attachment():
    """Test JSON attachment processing"""
    test_dir = create_test_json_attachment()
    
    try:
        # Create report config
        config = ReportConfig()
        
        # Create report builder
        builder = ReportBuilder(allure_dir=test_dir, config=config)
        
        # Save report
        output_path = os.path.join(test_dir, "test_report.docx")
        builder.save_report(output_path)
        
        print(f"✅ Test completed successfully!")
        print(f"📁 Test directory: {test_dir}")
        print(f"📄 Report generated: {output_path}")
        
        # Check if files exist
        if os.path.exists(output_path):
            print(f"✅ Report file created successfully")
        else:
            print(f"❌ Report file not found")
            
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        # Clean up
        import shutil
        shutil.rmtree(test_dir)

if __name__ == "__main__":
    test_json_attachment() 