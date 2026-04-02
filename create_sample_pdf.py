
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
import os

# Create data directory if not exists
if not os.path.exists('data'):
    os.makedirs('data')

# Register a Chinese font (Microsoft YaHei is usually available on Windows)
try:
    pdfmetrics.registerFont(TTFont('YaHei', 'msyh.ttc'))
    FONT_NAME = 'YaHei'
except:
    try:
        pdfmetrics.registerFont(TTFont('SimSun', 'simsun.ttc'))
        FONT_NAME = 'SimSun'
    except:
        print("Warning: Could not load Chinese font. Using default font (Chinese characters may not display correctly).")
        FONT_NAME = 'Helvetica'

def create_pdf(filename, title, content):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # Title
    c.setFont(FONT_NAME, 24)
    c.drawString(50, height - 50, title)
    
    # Content
    c.setFont(FONT_NAME, 12)
    y_position = height - 100
    for line in content.split('\n'):
        if line.strip():
            # Simple text wrapping could be added here, but for this demo we'll keep lines short
            c.drawString(50, y_position, line.strip())
            y_position -= 20
            
    c.save()
    print(f"Created {filename}")

# Sample 1: Common Cold Guide
cold_content = """
感冒（普通感冒）是一种常见的上呼吸道病毒性感染。
症状：
1. 鼻塞、流鼻涕
2. 喉咙痛、咳嗽
3. 轻微发热、头痛
4. 全身乏力

治疗与护理：
1. 多休息，保证充足睡眠。
2. 多喝水，保持身体水分。
3. 对症用药：如使用退烧药（布洛芬、对乙酰氨基酚）缓解发热和疼痛。
4. 通常在7-10天内会自行康复。

预防：
1. 勤洗手，避免触摸眼口鼻。
2. 避免与感冒患者密切接触。
"""
create_pdf('data/感冒健康指南.pdf', '普通感冒健康指南', cold_content)

# Sample 2: Hypertension Guide
bp_content = """
高血压（Hypertension）是指血液在血管中流动时对血管壁压力持续高于正常的现象。
诊断标准：
收缩压（高压）≥140 mmHg 和/或 舒张压（低压）≥90 mmHg。

生活方式干预：
1. 低盐饮食：每日食盐摄入量不超过5克。
2. 控制体重：BMI控制在18.5-23.9之间。
3. 规律运动：每周至少进行150分钟中等强度有氧运动。
4. 戒烟限酒。

药物治疗：
必须在医生指导下按时服用降压药，不可擅自停药。
"""
create_pdf('data/高血压管理指南.pdf', '高血压管理指南', bp_content)

# Sample 3: Diabetes Guide
diabetes_content = """
糖尿病是一种以高血糖为特征的代谢性疾病。
典型症状（三多一少）：
1. 多饮
2. 多食
3. 多尿
4. 体重减少

饮食建议：
1. 控制总热量摄入。
2. 少吃高糖、高脂肪食物。
3. 多吃蔬菜、全谷物等富含膳食纤维的食物。
4. 定时定量进餐。

血糖监测：
定期监测空腹血糖和餐后2小时血糖，记录数值以便医生调整治疗方案。
"""
create_pdf('data/糖尿病饮食指南.pdf', '糖尿病饮食指南', diabetes_content)
