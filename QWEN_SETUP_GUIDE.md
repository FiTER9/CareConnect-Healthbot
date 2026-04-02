# 通义千问（Qwen）模型配置指南

## 🌟 关于 Qwen

**通义千问（Qwen）** 是阿里巴巴开发的大语言模型，具有以下特点：
- ✅ 中文能力极强
- ✅ 支持长文本（最高 32K tokens）
- ✅ 推理能力优秀
- ✅ 适合医疗、法律等专业领域

## 📦 可用的 Qwen 模型

### 1. Qwen-7B-Chat（推荐）
- **参数量：** 7B
- **大小：** 约 14GB（完整版）/ 4-7GB（量化版）
- **HuggingFace：** `Qwen/Qwen-7B-Chat`
- **量化版本：** `Qwen/Qwen-7B-Chat-Int4`

### 2. Qwen-1.8B-Chat（轻量版）
- **参数量：** 1.8B
- **大小：** 约 3.5GB（完整版）/ 1-2GB（量化版）
- **HuggingFace：** `Qwen/Qwen-1_8B-Chat`
- **适合：** 内存较小的设备

### 3. Qwen-14B-Chat（高性能版）
- **参数量：** 14B
- **大小：** 约 28GB（完整版）/ 8-14GB（量化版）
- **HuggingFace：** `Qwen/Qwen-14B-Chat`
- **适合：** 高性能需求

## 🔧 配置方法

### 方法 1：使用 Transformers（推荐）

由于 Qwen 模型不支持 CTransformers，我们需要使用 transformers 库。

#### 步骤 1：安装依赖
```bash
pip install transformers>=4.32.0
pip install accelerate
pip install tiktoken
pip install transformers_stream_generator
```

#### 步骤 2：修改代码
需要修改 `chainlit_app.py` 中的 LLM 加载部分。

### 方法 2：使用 GGUF 格式（轻量）

使用社区量化的 GGUF 版本，兼容 llama.cpp。

```bash
pip install llama-cpp-python
```

## ⚙️ 系统要求

### Qwen-7B-Chat
- **最低配置：**
  - RAM: 16GB
  - 磁盘: 15GB
  - CPU: 8核心

- **推荐配置：**
  - RAM: 32GB
  - GPU: NVIDIA GPU (8GB+ VRAM)
  - 磁盘: 20GB

### Qwen-1.8B-Chat（轻量版）
- **最低配置：**
  - RAM: 8GB
  - 磁盘: 5GB
  - CPU: 4核心

## 🚀 快速开始

我将帮你配置 Qwen-7B-Chat 模型。

---

**准备好了吗？我现在就开始配置！** 🎉
