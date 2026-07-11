# ==========================================
# Project Alpha
# Sprint 2 - Project Directory Structure
# ==========================================

Write-Host ""
Write-Host "==========================================="
Write-Host " Project Alpha - Sprint 2 Setup"
Write-Host "==========================================="
Write-Host ""

# Create top-level folders
$folders = @(
    "charts",
    "config",
    "data",
    "docs",
    "logs",
    "reports",
    "src",
    "tests",

    "src\backtest",
    "src\broker",
    "src\config",
    "src\data",
    "src\indicators",
    "src\risk",
    "src\sessions",
    "src\strategy",
    "src\utils",
    "src\visualization"
)

foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "[Created] $folder"
    }
    else {
        Write-Host "[Exists ] $folder"
    }
}

# Create __init__.py files
$initFiles = @(
    "src\__init__.py",
    "src\backtest\__init__.py",
    "src\broker\__init__.py",
    "src\config\__init__.py",
    "src\data\__init__.py",
    "src\indicators\__init__.py",
    "src\risk\__init__.py",
    "src\sessions\__init__.py",
    "src\strategy\__init__.py",
    "src\utils\__init__.py",
    "src\visualization\__init__.py"
)

foreach ($file in $initFiles) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "[Created] $file"
    }
    else {
        Write-Host "[Exists ] $file"
    }
}

Write-Host ""
Write-Host "==========================================="
Write-Host " Sprint 2 setup completed successfully."
Write-Host "==========================================="