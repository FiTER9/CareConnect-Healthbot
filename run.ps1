# CareConnect 启动脚本

# 尝试使用 Conda 环境 CareConnect-Healthbot
$EnvName = "CareConnect-Healthbot"
$CondaEnvPath = "E:\1.APPLICATION\miniconda\envs\$EnvName"
$PythonExe = "$CondaEnvPath\python.exe"
$ChainlitExe = "$CondaEnvPath\Scripts\chainlit.exe"

if (Test-Path $PythonExe) {
    Write-Host "已检测到 Conda 环境: $EnvName" -ForegroundColor Green
    
    # 检查 Ollama 是否在运行
    if (Get-Process "ollama" -ErrorAction SilentlyContinue) {
        Write-Host "Ollama 正在运行。" -ForegroundColor Green
    } else {
        Write-Host "警告: 未检测到 Ollama 进程。请确保 Ollama 已启动。" -ForegroundColor Red
        Write-Host "尝试启动 Ollama..." -ForegroundColor Yellow
        Start-Process "ollama" "serve" -WindowStyle Hidden
        Start-Sleep -Seconds 3
    }

    # 检查向量数据库是否存在，如果不存在则自动创建
    if (-not (Test-Path "vectorstore\db_faiss")) {
        Write-Host "未检测到向量数据库，正在构建..." -ForegroundColor Yellow
        & $PythonExe ingest.py
    }

    # 运行应用
    Write-Host "正在启动 CareConnect 医疗助手..." -ForegroundColor Cyan
    & $ChainlitExe run chainlit_app.py -w
    exit
} else {
    Write-Host "未找到 Conda 环境 $EnvName，尝试使用 .venv..." -ForegroundColor Yellow
}

# 检查是否存在虚拟环境 (.venv) - 备用方案
if (Test-Path ".venv") {
    Write-Host "正在激活虚拟环境..." -ForegroundColor Green
    . .venv\Scripts\Activate.ps1
} else {
    Write-Host "未检测到虚拟环境，正在创建..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "正在安装依赖..." -ForegroundColor Yellow
    .venv\Scripts\pip install -r requirements.txt
    . .venv\Scripts\Activate.ps1
}

# 检查 Ollama 是否在运行
if (Get-Process "ollama" -ErrorAction SilentlyContinue) {
    Write-Host "Ollama 正在运行。" -ForegroundColor Green
} else {
    Write-Host "警告: 未检测到 Ollama 进程。请确保 Ollama 已启动。" -ForegroundColor Red
    Write-Host "尝试启动 Ollama..." -ForegroundColor Yellow
    Start-Process "ollama" "serve" -WindowStyle Hidden
}

# 运行应用
Write-Host "正在启动 CareConnect 医疗助手..." -ForegroundColor Cyan
chainlit run chainlit_app.py -w
