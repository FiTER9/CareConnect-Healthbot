# 📥 医疗 PDF 下载指南

## 🎯 快速下载步骤

### 方法 1：WHO（世界卫生组织）- 最推荐 ⭐⭐⭐⭐⭐

1. **访问：** https://www.who.int/publications
2. **搜索主题：** 例如 "diabetes", "hypertension", "nutrition"
3. **筛选：** 选择 "PDF" 格式
4. **下载：** 点击下载按钮
5. **保存：** 保存到 `E:\CareConnect-Healthbot\data\` 目录

**推荐文档：**
- WHO Guidelines on Physical Activity
- Diabetes Prevention and Management
- Mental Health Guidelines
- Nutrition Guidelines

---

### 方法 2：CDC（美国疾控中心）⭐⭐⭐⭐

1. **访问：** https://www.cdc.gov/publications/
2. **浏览主题：** Health Topics
3. **选择：** 感兴趣的健康主题
4. **下载 PDF：** 大多数资源提供 PDF 下载
5. **保存到：** `E:\CareConnect-Healthbot\data\`

**推荐主题：**
- Chronic Disease Prevention
- Healthy Living
- Vaccines and Immunizations
- Emergency Preparedness

---

### 方法 3：PubMed Central（免费医学文献）⭐⭐⭐⭐

1. **访问：** https://www.ncbi.nlm.nih.gov/pmc/
2. **搜索：** 输入医学主题（英文）
3. **筛选：** 选择 "Free full text"
4. **下载 PDF：** 点击文章后选择 "Download PDF"
5. **保存到：** `E:\CareConnect-Healthbot\data\`

**搜索示例：**
- "diabetes management review"
- "hypertension treatment guidelines"
- "nutrition and health"

---

### 方法 4：NCBI Bookshelf（免费医学书籍）⭐⭐⭐⭐⭐

1. **访问：** https://www.ncbi.nlm.nih.gov/books/
2. **浏览：** Medical and Health Sciences
3. **选择书籍：** 点击感兴趣的书籍
4. **下载：** 点击 "Download PDF" 或 "Save as PDF"
5. **保存到：** `E:\CareConnect-Healthbot\data\`

**推荐书籍：**
- StatPearls (医学百科全书)
- Clinical Guidelines
- Medical Textbooks

---

## 🔍 具体下载示例

### 示例 1：下载 WHO 糖尿病指南

```
1. 打开浏览器访问：https://www.who.int/publications
2. 在搜索框输入：diabetes
3. 找到 "Global report on diabetes" 或类似文档
4. 点击文档标题
5. 点击 "Download" 或 "PDF" 按钮
6. 保存文件到：E:\CareConnect-Healthbot\data\who_diabetes_report.pdf
```

### 示例 2：下载 CDC 健康指南

```
1. 访问：https://www.cdc.gov/healthyliving/
2. 选择一个主题，例如 "Physical Activity"
3. 查找 PDF 资源链接
4. 下载并保存到：E:\CareConnect-Healthbot\data\cdc_physical_activity.pdf
```

### 示例 3：从 PubMed Central 下载文章

```
1. 访问：https://www.ncbi.nlm.nih.gov/pmc/
2. 搜索："diabetes prevention"
3. 点击任意免费全文文章
4. 点击右上角 "Download PDF"
5. 保存到：E:\CareConnect-Healthbot\data\
```

---

## 📋 推荐下载清单

建议下载 **10-20 个 PDF** 文件，涵盖以下主题：

### 基础健康（5个文档）
- [ ] 糖尿病指南
- [ ] 高血压管理
- [ ] 心脏健康
- [ ] 营养指南
- [ ] 运动与健康

### 疾病预防（3个文档）
- [ ] 疫苗接种指南
- [ ] 传染病预防
- [ ] 慢性病预防

### 急救和紧急护理（2个文档）
- [ ] 急救手册
- [ ] CPR 指南

### 心理健康（2个文档）
- [ ] 压力管理
- [ ] 心理健康指南

### 其他（3-5个文档）
- [ ] 药物信息
- [ ] 健康筛查指南
- [ ] 妇女健康
- [ ] 儿童健康
- [ ] 老年人健康

---

## ⚡ 快速下载链接

### 直接可下载的资源：

1. **WHO - Global Health Reports**
   - https://www.who.int/data/gho/publications/world-health-statistics

2. **CDC - Health Publications**
   - https://www.cdc.gov/publications/

3. **NIH - Health Information**
   - https://www.nih.gov/health-information

4. **MedlinePlus - Health Topics**
   - https://medlineplus.gov/healthtopics.html

---

## ✅ 下载后的步骤

### 1. 验证文件
```bash
# 检查 data 目录
cd E:\CareConnect-Healthbot
dir data\*.pdf
```

### 2. 运行帮助脚本确认
```bash
python setup_knowledge_base.py
```

### 3. 生成向量数据库
```bash
python ingest.py
```

### 4. 启动应用
```bash
chainlit run chainlit_app.py
```

---

## ⚠️ 重要提示

### 法律和版权
- ✅ 只下载明确标注为 "Open Access" 或 "Free" 的文档
- ✅ 优先选择政府和公共卫生组织的资源
- ✅ 遵守各网站的使用条款
- ❌ 不要下载有版权保护的商业医学教材

### 文件质量
- ✅ 确保 PDF 文件可以正常打开
- ✅ 文件内容清晰可读
- ✅ 文件大小合理（通常 1-50MB）
- ❌ 避免扫描质量差的文档
- ❌ 避免加密或受保护的 PDF

### 内容准确性
- ✅ 选择权威来源（WHO、CDC、NIH等）
- ✅ 选择最新发布的文档
- ✅ 验证信息的可信度
- ❌ 避免来源不明的文档
- ❌ 避免过时的医疗信息

---

## 🆘 需要帮助？

如果下载遇到问题：

1. **检查网络连接**
2. **尝试不同的浏览器**
3. **清除浏览器缓存**
4. **使用 VPN（如果网站被屏蔽）**
5. **查看网站的帮助文档**

---

## 📞 联系支持

如果仍有问题，请：
- 查看 README.md
- 查看 QUICKSTART.md
- 在 GitHub 上提交 Issue

---

**预计下载时间：** 30-60 分钟（取决于网速和文档数量）

**下载完成后，你就可以运行项目了！** 🎉
