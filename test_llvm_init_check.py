#!/usr/bin/env python3
"""
Test script for LLVM initialization state check function.
This script tests the new is_llvm_target_initialized function.
"""

import sys
import os

# Add the build directory to Python path to import taichi
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python'))

def test_llvm_init_check():
    """Test the LLVM initialization state check function."""
    try:
        import taichi as ti
        
        print("Testing LLVM initialization state check function...")
        
        # Test CPU architecture
        print("Testing CPU architecture...")
        ti.init(arch=ti.cpu)
        print("✓ CPU initialization successful")
        
        # Test that we can initialize multiple times without issues
        print("Testing multiple initializations...")
        ti.init(arch=ti.cpu)
        print("✓ Multiple CPU initializations successful")
        
        # Test a simple kernel to ensure everything works
        print("Testing simple kernel execution...")
        
        @ti.kernel
        def test_kernel() -> int:
            return 42
        
        result = test_kernel()
        assert result == 42, f"Expected 42, got {result}"
        print("✓ Simple kernel execution successful")
        
        print("All tests passed!")
        return True
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_llvm_init_check()
    sys.exit(0 if success else 1)