# 🚀 快速启动指南 (Quick Start Guide)

本指南将帮助你快速设置和运行基于 **DeepSeek + Ollama** 的 CareConnect 医疗健康助手。

---

## ⚡ 极速启动 (Windows)

如果您已经配置好环境，只需在终端运行以下命令即可一键启动：

```powershell
.\run.ps1
```

该脚本会自动检测环境、启动 Ollama 服务并打开聊天界面。

---

## 📋 详细安装步骤

### 1️⃣ 安装必要工具

1.  **安装 Python 3.9+**: 请确保您的电脑已安装 Python。
2.  **安装 Ollama**: 用于运行大语言模型。
    *   访问 [Ollama 官网](https://ollama.com/) 下载并安装。
    *   或者在 Windows 终端运行: `winget install Ollama.Ollama`

### 2️⃣ 下载 DeepSeek 模型

在终端运行以下命令来下载 DeepSeek 模型 (约 5GB):

```powershell
ollama pull deepseek-r1:8b
```

> **提示**: 下载速度取决于您的网络状况，请耐心等待。

### 3️⃣ 安装项目依赖

我们建议使用 Conda 或虚拟环境来管理依赖。

**使用 Conda (推荐):**
```powershell
# 假设您已创建并激活了 Conda 环境
pip install -r requirements.txt
```

**或者使用 Python venv:**
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 4️⃣ 准备知识库 (医疗 PDF)

1.  将您的医疗 PDF 文档放入项目的 `data/` 目录中。
    *   *没有 PDF?* 运行 `python create_sample_pdf.py` 生成一些测试文档。
2.  运行以下命令来构建向量数据库：

```powershell
python ingest.py
```

> 此步骤会将 PDF 内容转化为向量并存储在 `vectorstore/db_faiss` 中。

### 5️⃣ 启动应用

一切准备就绪后，运行以下命令启动聊天机器人：

```powershell
chainlit run chainlit_app.py -w
```

或者直接使用我们提供的快捷脚本：
```powershell
.\run.ps1
```

浏览器会自动打开 `http://localhost:8000`，您可以开始提问了！

---

## ❓ 常见问题

**Q: 启动时报错 "Connection refused"？**
A: 请检查 Ollama 是否正在运行。您可以在终端输入 `ollama list` 来检查。如果未运行，请先启动 Ollama 应用或在终端运行 `ollama serve`。

**Q: 机器人回答 "我无法找到答案"？**
A: 这说明在您的 PDF 知识库中没有找到相关信息。请尝试：
1. 添加更多相关的 PDF 到 `data/` 目录。
2. 重新运行 `python ingest.py` 更新知识库。

**Q: 如何切换其他模型？**
A: 修改 `chainlit_app.py` 文件中的 `MODEL_NAME` 变量 (例如改为 `deepseek-r1:7b` 或 `qwen:4b`)，并确保您已通过 Ollama 下载了对应模型。
