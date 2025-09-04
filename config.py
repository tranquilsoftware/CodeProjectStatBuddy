# List of directories to exclude from counting stats
EXCLUDE_DIRS = [
    # TypeScript / Web dev
    'node_modules',
    'dist',
    'build',
    '.next',
    '.nuxt',
    'coverage',
    
    # Python
    '__pycache__',
    '.venv',
    'venv',
    'env',
    '.pytest_cache',
    '.tox',
    'site-packages',
    
    # C++
    'build',
    'libs',
    'bin',
    'obj',
    'Debug',
    'Release',
    
    # Java
    'target',
    'out',
    
    # .NET
    'bin',
    'obj',
    'packages',
    
    # Git
    '.git',
    
    # IDE
    '.idea',
    '.vscode',
    '.vs',
    '.eclipse',
    
    # OS
    '.DS_Store',
    'Thumbs.db',
    
    # Other
    'tmp',
    'temp',
    'cache',
    '.cache',
]