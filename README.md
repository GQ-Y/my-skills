# My Skills - Skills-MCP 技能库

这是一个包含多个 AI 技能的仓库，用于扩展 Cursor、Claude Code 和 Gemini CLI 等工具的能力。

## 📦 仓库信息

- **仓库地址**: https://github.com/GQ-Y/my-skills.git
- **技能数量**: 18 个技能
- **总文件数**: 281 个文件

## 🚀 快速开始

### 从远程仓库初始化技能

#### 方法一：使用 Git Clone（推荐）

```bash
# 克隆仓库到本地
git clone https://github.com/GQ-Y/my-skills.git ~/.skill-mcp/skills

# 或者克隆到其他位置
git clone https://github.com/GQ-Y/my-skills.git /path/to/your/skills
```

#### 方法二：如果已有本地技能目录

```bash
# 进入现有技能目录
cd ~/.skill-mcp/skills

# 添加远程仓库
git remote add origin https://github.com/GQ-Y/my-skills.git

# 拉取技能
git pull origin main
```

## ⚙️ 配置 MCP 服务器

### Cursor 配置

1. **打开 Cursor 设置**
   - macOS: `Cmd + ,` 或 `Cursor > Settings`
   - Windows/Linux: `Ctrl + ,`

2. **找到 MCP 设置**
   - 在设置中搜索 "MCP" 或 "Model Context Protocol"
   - 或者直接编辑配置文件：`~/.cursor/mcp.json` 或 `~/.cursor/settings.json`

3. **添加 skills-mcp 配置**

   在 MCP 配置文件中添加以下配置：

   ```json
   {
     "mcpServers": {
       "skill-mcp": {
         "command": "npx",
         "args": [
           "-y",
           "skills-mcp",
           "-s",
           "/Users/your-username/.skill-mcp/skills"
         ]
       }
     }
   }
   ```

   **注意**: 
   - 将 `/Users/your-username/.skill-mcp/skills` 替换为您的实际技能目录路径（使用绝对路径）
   - 或者使用环境变量：`"$HOME/.skill-mcp/skills"`（某些工具可能不支持）

4. **重启 Cursor**
   - 完全退出并重新启动 Cursor 以使配置生效

### Claude Code 配置

1. **找到配置文件位置**
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. **编辑配置文件**

   添加以下 MCP 服务器配置：

   ```json
   {
     "mcpServers": {
       "skill-mcp": {
         "command": "npx",
         "args": [
           "-y",
           "skills-mcp",
           "-s",
           "/Users/your-username/.skill-mcp/skills"
         ]
       }
     }
   }
   ```

   **注意**: 将路径替换为您的实际技能目录绝对路径

3. **重启 Claude Code**
   - 完全退出并重新启动 Claude Code

### Gemini CLI 配置

1. **找到配置文件**
   - 配置文件通常位于：`~/.config/gemini/mcp.json` 或 `~/.gemini/mcp.json`

2. **编辑配置文件**

   添加以下配置：

   ```json
   {
     "mcpServers": {
       "skill-mcp": {
         "command": "npx",
         "args": [
           "-y",
           "skills-mcp",
           "-s",
           "/Users/your-username/.skill-mcp/skills"
         ]
       }
     }
   }
   ```

   **注意**: 将路径替换为您的实际技能目录绝对路径

3. **重启 Gemini CLI**

## 📋 技能列表

本仓库包含以下 18 个技能：

1. **algorithmic-art** - 算法艺术生成器
2. **brand-guidelines** - 品牌指南
3. **canvas-design** - Canvas 设计工具（包含 54 个字体文件）
4. **doc-coauthoring** - 文档协作
5. **docx** - Word 文档处理（包含 OOXML schema）
6. **frontend-design** - 前端设计
7. **internal-comms** - 内部通讯
8. **mcp-builder** - MCP 构建器
9. **pdf** - PDF 处理工具
10. **pptx** - PowerPoint 处理（包含 OOXML schema）
11. **project-structure-manager** - 项目结构管理器
12. **skill-creator** - 技能创建器
13. **slack-gif-creator** - Slack GIF 创建器
14. **theme-factory** - 主题工厂
15. **web-artifacts-builder** - Web 工件构建器
16. **webapp-testing** - Web 应用测试
17. **xlsx** - Excel 处理

## 🔧 配置说明

### 技能目录路径

在配置文件中，必须使用**绝对路径**指定技能目录：

- ✅ **正确**: `/Users/username/.skill-mcp/skills`
- ❌ **错误**: `~/.skill-mcp/skills`（某些工具不支持波浪号展开）
- ❌ **错误**: `$HOME/.skill-mcp/skills`（某些工具不支持环境变量）

### 获取绝对路径

在终端中运行以下命令获取您的技能目录绝对路径：

```bash
# macOS/Linux
realpath ~/.skill-mcp/skills
# 或者
cd ~/.skill-mcp/skills && pwd

# 如果目录不存在，先创建
mkdir -p ~/.skill-mcp/skills
cd ~/.skill-mcp/skills && pwd
```

## 📝 验证配置

配置完成后，您可以通过以下方式验证：

1. **检查技能目录**
   ```bash
   ls ~/.skill-mcp/skills
   ```

2. **查看技能列表**
   在 Cursor/Claude Code/Gemini CLI 中，MCP 服务器应该能够列出所有可用的技能。

3. **测试技能**
   尝试使用某个技能，例如询问 AI 助手关于某个技能的功能。

## 🔄 更新技能

当远程仓库有更新时，可以通过以下方式更新本地技能：

```bash
cd ~/.skill-mcp/skills
git pull origin main
```

## 📚 技能结构

每个技能目录通常包含：

```
skill-name/
├── SKILL.md          # 技能说明文档（必需）
├── LICENSE.txt       # 许可证文件
├── scripts/          # 可执行脚本
├── references/       # 参考文档
└── assets/           # 资源文件（字体、模板等）
```

## 🐛 故障排除

### 问题：MCP 服务器无法连接

1. **检查技能目录路径**
   - 确保配置中使用的是**绝对路径**（不是 `~` 或相对路径）
   - 确保目录存在且包含技能文件
   - 验证路径是否正确：`ls /path/to/your/skills`

2. **检查 Node.js 和 npx**
   ```bash
   node --version
   npx --version
   ```

3. **检查配置文件格式**
   - 确保 JSON 格式正确
   - 检查是否有语法错误

### 问题：技能未显示

1. **检查技能目录**
   ```bash
   ls ~/.skill-mcp/skills
   ```

2. **检查 SKILL.md 文件**
   每个技能目录必须包含有效的 `SKILL.md` 文件

3. **重启应用程序**
   完全退出并重新启动 Cursor/Claude Code/Gemini CLI

### 问题：权限错误

如果遇到权限问题：

```bash
# 检查目录权限
ls -la ~/.skill-mcp/skills

# 如果需要，修改权限
chmod -R 755 ~/.skill-mcp/skills
```

## 📖 更多信息

- **MCP 协议文档**: https://modelcontextprotocol.io
- **技能创建指南**: 查看 `skill-creator/SKILL.md`
- **仓库 Issues**: https://github.com/GQ-Y/my-skills/issues

## 📄 许可证

各个技能可能有不同的许可证，请查看每个技能目录中的 `LICENSE.txt` 文件。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**最后更新**: 2025-01-13
