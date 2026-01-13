# 项目目录结构管理技能

## 快速开始

### 1. 初始化项目结构

```bash
python ~/.skill-mcp/skills/project-structure-manager/scripts/cleanup_structure.py --init
```

### 2. 整理现有文件

```bash
# 预览模式
python ~/.skill-mcp/skills/project-structure-manager/scripts/cleanup_structure.py --clean --dry-run

# 实际执行
python ~/.skill-mcp/skills/project-structure-manager/scripts/cleanup_structure.py --clean
```

### 3. 提取文档文本

```bash
# 提取单个PPT文件
python ~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py \
    materials/background/ppt/演示文稿.pptx

# 批量提取PPT目录
python ~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py \
    materials/background/ppt/ --batch

# 批量提取Word文档
python ~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py \
    materials/background/docs/ --batch
```

## 目录结构

```
项目根目录/
├── materials/
│   ├── background/
│   │   ├── ppt/      # PPT文件
│   │   ├── pdf/      # PDF文件
│   │   ├── images/   # 图片文件
│   │   ├── docs/     # Word文档
│   │   └── txt/      # 提取的文本文件（重要！）
│   ├── references/   # 参考资料
│   ├── outputs/      # 输出文件
│   └── temp/         # 临时文件
├── tools/            # 项目特定工具（简化：不再细分）
└── docs/             # 项目文档
```

## 重要说明

### 通用工具 vs 项目特定工具

- **通用工具**：位于技能目录 `~/.skill-mcp/skills/project-structure-manager/scripts/`
  - `cleanup_structure.py` - 目录清理工具
  - `extract_text.py` - 文本提取工具
  - 这些工具可在任何项目中使用，**无需复制到项目目录**

- **项目特定工具**：放在项目的 `tools/` 目录
  - 只有项目专用的、非通用的脚本才放在这里
  - 不再细分 python/shell/other 子目录

### 文本提取的重要性

PPT和Word文档是二进制格式，AI大模型直接读取效率低。提取为TXT后：
- ✅ 读取速度快
- ✅ 内容清晰，无格式干扰
- ✅ 便于AI理解和分析

**工作流程**：
```
原始文件 → materials/background/ppt/ 或 docs/
    ↓
提取文本 → materials/background/txt/
    ↓
AI读取TXT文件进行分析
```

## 依赖安装

文本提取功能需要安装以下依赖：

```bash
pip install python-pptx python-docx
```

## 更多信息

详细说明请参考技能文档：`project-structure-manager` 技能
