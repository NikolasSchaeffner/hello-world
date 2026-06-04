#!/usr/bin/env python3
"""
Direct execution wrapper — imports and runs the converter.
Execute: python3 /home/user/hello-world/run_conversion.py
"""
import sys
sys.path.insert(0, '/home/user/hello-world')

# Execute the converter module directly
exec(open('/home/user/hello-world/convert_to_docx.py').read())
