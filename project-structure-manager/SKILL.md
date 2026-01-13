---
name: project-structure-manager
description: 标准化项目目录结构管理和清理工具。当用户需要整理项目目录、清理文件结构、规范背景材料存放位置，或进行方案设计前的目录结构准备时使用。自动将文件按类型分类到指定目录（背景PPT、PDF、图片、TXT文本等），并提供PPT和Word文档的文本提取功能。
---

# 项目目录结构管理

标准化项目目录结构管理技能，用于规范项目文件组织，确保背景材料、脚本和输出文件有序存放。支持将PPT、Word等文档提取为TXT文本，方便AI大模型读取。

## 标准目录结构

### 项目根目录结构

```
项目根目录/
├── materials/              # 项目资料目录
│   ├── background/        # 背景材料目录
│   │   ├── ppt/          # 背景PPT文件
│   │   ├── pdf/          # 背景PDF文件
│   │   ├── images/       # 背景图片
│   │   ├── docs/         # 背景文档（Word、Markdown等）
│   │   └── txt/          # 提取的文本文件（PPT/Word转TXT）
│   ├── references/        # 参考资料目录
│   ├── outputs/           # 输出文件目录
│   │   ├── presentations/ # 生成的PPT
│   │   ├── documents/     # 生成的文档
│   │   └── reports/       # 生成的报告
│   └── temp/              # 临时文件目录
├── tools/                 # 项目特定工具脚本（仅项目专用脚本）
├── docs/                  # 项目文档目录
│   ├── requirements/     # 需求文档
│   ├── designs/          # 设计方案
│   └── notes/            # 笔记和草稿
└── README.md             # 项目说明
```

## 目录用途说明

### materials/background/ - 背景材料
存放用于方案设计的背景材料，按文件类型分类：
- **ppt/**: 背景演示文稿（.pptx, .ppt）
- **pdf/**: 背景PDF文档（.pdf）
- **images/**: 背景图片（.png, .jpg, .jpeg, .gif, .svg等）
- **docs/**: 背景文档（.docx, .doc, .md等）
- **txt/**: 提取的文本文件（从PPT、Word提取的TXT，方便AI读取）

### materials/references/ - 参考资料
存放项目相关的参考资料，可按项目或主题创建子目录。

### materials/outputs/ - 输出文件
存放方案设计过程中生成的文件：
- **presentations/**: 生成的PPT演示文稿
- **documents/**: 生成的文档（Word、Markdown等）
- **reports/**: 生成的报告

### tools/ - 项目特定工具脚本
**仅存放项目专用的工具脚本**。通用工具脚本已内置在技能中，无需复制到项目目录。

### docs/ - 项目文档
存放项目相关的文档：
- **requirements/**: 需求文档
- **designs/**: 设计方案文档
- **notes/**: 笔记和草稿

## 使用工作流程

### 1. 初始化项目结构

在开始新方案设计前，运行清理脚本初始化目录结构：

```bash
python ~/.skill-mcp/skills/project-structure-manager/scripts/cleanup_structure.py --init
```

或者如果脚本已复制到项目：

```bash
python tools/cleanup_structure.py --init
```

这将：
- 创建所有标准目录（包括txt目录）
- 检查现有文件并提示分类
- 生成或更新 README.md

### 2. 清理现有项目

整理现有项目的文件结构：

```bash
python ~/.skill-mcp/skills/project-structure-manager/scripts/cleanup_structure.py --clean
```

脚本将：
- 扫描项目根目录
- 按文件类型自动分类
- 移动文件到对应目录
- 生成整理报告

### 3. 提取文档文本（重要功能）

将PPT、Word文档提取为TXT文本，方便AI大模型读取：

```bash
# 提取单个文件
python ~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py materials/background/ppt/演示文稿.pptx

# 批量提取PPT目录下的所有文件
python ~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py materials/background/ppt/ --batch

# 批量提取Word文档
python ~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py materials/background/docs/ --batch
```

提取的TXT文件将自动保存到 `materials/background/txt/` 目录，文件名与原文件相同（扩展名改为.txt）。

### 4. 添加背景材料

添加背景材料时，直接放入对应目录：
- PPT文件 → `materials/background/ppt/`
- PDF文件 → `materials/background/pdf/`
- 图片文件 → `materials/background/images/`
- 文档文件 → `materials/background/docs/`
- **提取的TXT文件** → `materials/background/txt/`（自动生成）

### 5. 生成输出文件

方案设计过程中生成的文件应存放在：
- 生成的PPT → `materials/outputs/presentations/`
- 生成的文档 → `materials/outputs/documents/`
- 生成的报告 → `materials/outputs/reports/`

## 工具脚本说明

### 通用工具（位于技能目录）

以下工具脚本位于技能目录，可在任何项目中使用，无需复制：

1. **cleanup_structure.py** - 目录结构清理和整理
   - 位置：`~/.skill-mcp/skills/project-structure-manager/scripts/cleanup_structure.py`
   - 功能：初始化目录、清理文件、分类整理

2. **extract_text.py** - 文档文本提取工具
   - 位置：`~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py`
   - 功能：从PPT、Word文档提取文本为TXT格式

### 项目特定工具（位于项目tools目录）

只有项目专用的、非通用的工具脚本才放在项目的 `tools/` 目录下。

## 文件分类规则

### 背景材料分类

| 文件类型 | 扩展名 | 目标目录 |
|---------|-------|---------|
| PPT | .pptx, .ppt | materials/background/ppt/ |
| PDF | .pdf | materials/background/pdf/ |
| 图片 | .png, .jpg, .jpeg, .gif, .svg, .bmp, .webp | materials/background/images/ |
| 文档 | .docx, .doc, .md, .rtf | materials/background/docs/ |
| **文本** | **.txt** | **materials/background/txt/** |

### 脚本分类

| 文件类型 | 扩展名 | 目标目录 |
|---------|-------|---------|
| 项目脚本 | .py, .sh, .js等 | tools/ |

**注意**：通用工具脚本应使用技能目录中的脚本，不要复制到项目tools目录。

### 输出文件分类

| 文件类型 | 扩展名 | 目标目录 |
|---------|-------|---------|
| PPT输出 | .pptx, .ppt | materials/outputs/presentations/ |
| 文档输出 | .docx, .doc, .md | materials/outputs/documents/ |
| 报告输出 | .pdf, .html | materials/outputs/reports/ |

## 文本提取功能

### 为什么需要文本提取？

PPT和Word文档是二进制格式，AI大模型直接读取效率低。提取为TXT文本后：
- ✅ 读取速度快
- ✅ 内容清晰，无格式干扰
- ✅ 便于AI理解和分析
- ✅ 文件体积小

### 使用方法

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

# 指定输出目录
python ~/.skill-mcp/skills/project-structure-manager/scripts/extract_text.py \
    materials/background/ppt/演示文稿.pptx \
    --output materials/background/txt/
```

### 提取规则

- PPT文件：提取所有幻灯片的文本内容
- Word文档：提取所有段落文本，保留基本结构
- 输出格式：纯文本TXT，UTF-8编码
- 文件命名：原文件名.txt（如：演示文稿.pptx → 演示文稿.txt）

## 最佳实践

1. **方案设计前**：
   - 运行 `--init` 初始化目录结构
   - 将背景材料放入对应目录
   - 运行文本提取工具，将PPT/Word转为TXT

2. **添加文件后**：定期运行 `--clean` 保持目录整洁

3. **背景材料处理流程**：
   ```
   原始文件 → materials/background/ppt/ 或 docs/
        ↓
   提取文本 → materials/background/txt/
        ↓
   AI读取TXT文件进行分析
   ```

4. **工具脚本使用**：
   - 通用工具：使用技能目录中的脚本（无需复制）
   - 项目特定工具：放在项目 `tools/` 目录

5. **临时文件**：使用 `materials/temp/` 存放，定期清理

## 注意事项

- 清理脚本会移动文件，建议先使用 `--dry-run` 预览
- 同名文件冲突时会自动重命名（添加序号）
- 系统文件和隐藏文件（如 .DS_Store）会被忽略
- Git 仓库文件不会被移动
- 虚拟环境目录（venv/, .venv/）会被保留
- **文本提取需要安装依赖**：`pip install python-pptx python-docx`
