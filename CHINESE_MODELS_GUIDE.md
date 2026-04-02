# 🇨🇳 支持中文的开源 LLM 模型推荐

## 推荐模型列表

### 1. ChatGLM3-6B ⭐⭐⭐⭐⭐ (最推荐)
- **开发者：** 清华大学 KEG 实验室
- **大小：** 6B 参数
- **优势：**
  - 专门针对中文优化
  - 中英文双语能力强
  - 对话质量高
  - 支持 GGML 格式
- **HuggingFace：** `THUDM/chatglm3-6b`
- **量化版本：** `TheBloke/chatglm3-6B-GGML`

### 2. Qwen-7B-Chat ⭐⭐⭐⭐⭐
- **开发者：** 阿里巴巴
- **大小：** 7B 参数
- **优势：**
  - 中文能力极强
  - 支持长文本
  - 推理能力好
- **HuggingFace：** `Qwen/Qwen-7B-Chat`
- **量化版本：** `TheBloke/Qwen-7B-Chat-GGML`

### 3. Baichuan2-7B-Chat ⭐⭐⭐⭐
- **开发者：** 百川智能
- **大小：** 7B 参数
- **优势：**
  - 中文理解能力强
  - 开源免费
  - 医疗领域表现好
- **HuggingFace：** `baichuan-inc/Baichuan2-7B-Chat`

### 4. Chinese-LLaMA-2-7B ⭐⭐⭐⭐
- **开发者：** 中文 LLaMA 社区
- **大小：** 7B 参数
- **优势：**
  - 基于 Llama-2 的中文增强版
  - 兼容性好
- **HuggingFace：** `hfl/chinese-llama-2-7b`

### 5. InternLM-Chat-7B ⭐⭐⭐⭐
- **开发者：** 上海人工智能实验室
- **大小：** 7B 参数
- **优势：**
  - 中英文双语
  - 推理能力强
- **HuggingFace：** `internlm/internlm-chat-7b`

---

## 🔧 如何更换模型

### 方法 1：修改配置文件

编辑 `chainlit_app.py`，修改以下行：

```python
# 当前配置（英文模型）
MODEL_NAME = "TheBloke/Llama-2-7B-Chat-GGML"
MODEL_FILE = "llama-2-7b-chat.ggmlv3.q2_K.bin"

# 更换为中文模型（示例：ChatGLM3）
MODEL_NAME = "TheBloke/chatglm3-6B-GGML"
MODEL_FILE = "chatglm3-6b.ggmlv3.q4_0.bin"
```

### 方法 2：使用 HuggingFace Transformers

如果模型不支持 GGML 格式，可以使用 transformers 库：

```python
from transformers import AutoTokenizer, AutoModel

model_name = "THUDM/chatglm3-6b"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True).half().cuda()
```

---

## ⚖️ 模型对比

| 模型 | 中文能力 | 英文能力 | 大小 | 速度 | 推荐度 |
|------|---------|---------|------|------|--------|
| Llama-2-7B (当前) | ⭐⭐ | ⭐⭐⭐⭐⭐ | 2.5GB | 快 | ⭐⭐ |
| ChatGLM3-6B | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 3-6GB | 中 | ⭐⭐⭐⭐⭐ |
| Qwen-7B-Chat | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 4-7GB | 中 | ⭐⭐⭐⭐⭐ |
| Baichuan2-7B | ⭐⭐⭐⭐ | ⭐⭐⭐ | 4-7GB | 中 | ⭐⭐⭐⭐ |
| Chinese-LLaMA-2 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 4-7GB | 中 | ⭐⭐⭐⭐ |

---

## 💾 系统要求

### 最低配置（量化模型）
- **RAM：** 8GB
- **磁盘：** 5-10GB
- **CPU：** 4核心以上

### 推荐配置
- **RAM：** 16GB+
- **GPU：** NVIDIA GPU (4GB+ VRAM)
- **磁盘：** 20GB+

---

## 🚀 快速更换步骤

### 使用 ChatGLM3（推荐）

1. **停止当前应用**
   ```bash
   # 按 Ctrl+C
   ```

2. **修改模型配置**
   编辑 `chainlit_app.py`：
   ```python
   MODEL_NAME = "THUDM/chatglm3-6b"
   MODEL_TYPE = "chatglm"
   ```

3. **安装额外依赖**
   ```bash
   pip install transformers>=4.30.0
   pip install cpm_kernels
   ```

4. **重启应用**
   ```bash
   chainlit run chainlit_app.py
   ```

---

## ⚠️ 注意事项

1. **首次下载**
   - 中文模型通常 4-7GB
   - 下载时间取决于网速
   - 需要稳定的网络连接

2. **性能考虑**
   - 更大的模型需要更多内存
   - CPU 运行会比较慢
   - 建议使用 GPU 加速

3. **兼容性**
   - 某些模型可能需要特定的库版本
   - 建议查看模型的官方文档

---

## 📚 参考资源

- **ChatGLM3：** https://github.com/THUDM/ChatGLM3
- **Qwen：** https://github.com/QwenLM/Qwen
- **Baichuan2：** https://github.com/baichuan-inc/Baichuan2
- **HuggingFace 模型库：** https://huggingface.co/models

---

**需要我帮你更换为中文模型吗？** 🤔
