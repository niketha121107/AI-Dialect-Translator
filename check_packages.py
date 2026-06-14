import argostranslate

# List all available modules
print("Available argostranslate modules:")
print(dir(argostranslate))

# Check what's actually available for downloading
try:
    from argostranslate import package_manager
    print("\nPackage manager available")
except ImportError:
    print("\nPackage manager not available")

# Try alternate import
try:
    import argostranslatefiles
    print("argostranslatefiles available")
except ImportError:
    print("argostranslatefiles not available")
