#!/usr/bin/env python3
"""
项目目录结构清理和整理脚本

用法:
    python cleanup_structure.py --init      # 初始化目录结构
    python cleanup_structure.py --clean     # 清理并整理文件
    python cleanup_structure.py --clean --dry-run  # 预览模式
"""

import os
import shutil
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# 标准目录结构定义（简化版）
STANDARD_DIRS = {
    'materials': {
        'background': {
            'ppt': [],
            'pdf': [],
            'images': [],
            'docs': [],
            'txt': []  # 提取的文本文件
        },
        'references': [],
        'outputs': {
            'presentations': [],
            'documents': [],
            'reports': []
        },
        'temp': []
    },
    'tools': [],  # 简化为单一tools目录，不再细分
    'docs': {
        'requirements': [],
        'designs': [],
        'notes': []
    }
}

# 文件分类规则
FILE_CLASSIFICATION = {
    # 背景材料
    'ppt': ['.pptx', '.ppt'],
    'pdf': ['.pdf'],
    'images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.ico'],
    'docs': ['.docx', '.doc', '.md', '.rtf', '.odt'],  # 移除txt，单独分类
    'txt': ['.txt'],  # TXT文件单独分类到txt目录
    
    # 脚本文件（简化：所有脚本都放到tools/）
    'scripts': ['.py', '.sh', '.bash', '.zsh', '.js', '.ts', '.rb', '.pl', '.php', '.java'],
    
    # 输出文件
    'presentations': ['.pptx', '.ppt'],
    'documents': ['.docx', '.doc', '.md'],
    'reports': ['.pdf', '.html']
}

# 目标目录映射
TARGET_MAPPING = {
    # 背景材料
    'ppt': 'materials/background/ppt',
    'pdf': 'materials/background/pdf',
    'images': 'materials/background/images',
    'docs': 'materials/background/docs',
    'txt': 'materials/background/txt',  # TXT文件单独目录
    
    # 脚本（简化：所有脚本都放到tools/）
    'scripts': 'tools',
    
    # 输出（需要根据文件来源判断，这里先不自动移动）
}

# 忽略的文件和目录
IGNORE_PATTERNS = {
    '.git', '.gitignore', '.DS_Store', '__pycache__', 
    'venv', '.venv', 'node_modules', '.idea', '.vscode',
    'README.md', '.cursor', '.skill-mcp'
}


def create_directory_structure(base_path):
    """创建标准目录结构"""
    created_dirs = []
    
    def create_dirs(path, structure):
        if isinstance(structure, dict):
            for name, content in structure.items():
                dir_path = path / name
                if not dir_path.exists():
                    dir_path.mkdir(parents=True, exist_ok=True)
                    created_dirs.append(str(dir_path.relative_to(base_path)))
                if isinstance(content, dict):
                    create_dirs(dir_path, content)
        elif isinstance(structure, list):
            # 列表表示可以包含子目录，但标准结构中没有
            pass
    
    create_dirs(base_path, STANDARD_DIRS)
    return created_dirs


def get_file_category(file_path):
    """根据文件扩展名确定文件类别"""
    ext = file_path.suffix.lower()
    
    for category, extensions in FILE_CLASSIFICATION.items():
        if ext in extensions:
            return category
    return None


def should_ignore(path):
    """判断是否应该忽略该路径"""
    name = path.name
    if name in IGNORE_PATTERNS:
        return True
    if name.startswith('.'):
        return True
    if path.is_dir() and name in ['venv', '.venv', 'node_modules', '__pycache__']:
        return True
    return False


def find_files_to_move(root_path):
    """查找需要移动的文件"""
    files_to_move = defaultdict(list)
    
    # 只扫描根目录下的直接文件，不递归
    for item in root_path.iterdir():
        if should_ignore(item):
            continue
        
        if item.is_file():
            category = get_file_category(item)
            if category and category in TARGET_MAPPING:
                target_dir = TARGET_MAPPING[category]
                files_to_move[target_dir].append(item)
        # 不处理子目录中的文件，只处理根目录
    
    return files_to_move


def generate_unique_path(target_dir, filename):
    """生成唯一文件路径，处理重名冲突"""
    target_path = Path(target_dir) / filename
    
    if not target_path.exists():
        return target_path
    
    # 如果文件已存在，添加序号
    stem = target_path.stem
    suffix = target_path.suffix
    counter = 1
    
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_path = target_path.parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1


def move_files(files_to_move, dry_run=False):
    """移动文件到目标目录"""
    moved_files = []
    errors = []
    
    for target_dir, files in files_to_move.items():
        target_path = Path(target_dir)
        if not dry_run:
            target_path.mkdir(parents=True, exist_ok=True)
        
        for file_path in files:
            try:
                unique_path = generate_unique_path(target_dir, file_path.name)
                
                if dry_run:
                    print(f"[预览] {file_path} -> {unique_path}")
                else:
                    shutil.move(str(file_path), str(unique_path))
                    print(f"[移动] {file_path.name} -> {unique_path}")
                
                moved_files.append({
                    'source': str(file_path),
                    'target': str(unique_path)
                })
            except Exception as e:
                error_msg = f"移动 {file_path} 时出错: {str(e)}"
                errors.append(error_msg)
                print(f"[错误] {error_msg}")
    
    return moved_files, errors


def generate_report(created_dirs, moved_files, errors, dry_run=False):
    """生成整理报告"""
    report = []
    report.append("=" * 60)
    report.append("项目目录结构整理报告")
    report.append("=" * 60)
    report.append(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"模式: {'预览模式（未实际移动文件）' if dry_run else '执行模式'}")
    report.append("")
    
    if created_dirs:
        report.append(f"创建的目录 ({len(created_dirs)} 个):")
        for dir_path in sorted(created_dirs):
            report.append(f"  + {dir_path}/")
        report.append("")
    
    if moved_files:
        report.append(f"移动的文件 ({len(moved_files)} 个):")
        for item in moved_files:
            report.append(f"  {item['source']} -> {item['target']}")
        report.append("")
    
    if errors:
        report.append(f"错误 ({len(errors)} 个):")
        for error in errors:
            report.append(f"  ✗ {error}")
        report.append("")
    
    if not created_dirs and not moved_files and not errors:
        report.append("没有需要执行的操作。")
        report.append("")
    
    report.append("=" * 60)
    
    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description='项目目录结构清理和整理工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --init              # 初始化目录结构
  %(prog)s --clean             # 清理并整理文件
  %(prog)s --clean --dry-run   # 预览模式，不实际移动文件
        """
    )
    
    parser.add_argument(
        '--init',
        action='store_true',
        help='初始化标准目录结构'
    )
    
    parser.add_argument(
        '--clean',
        action='store_true',
        help='清理并整理现有文件'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='预览模式，不实际移动文件'
    )
    
    parser.add_argument(
        '--target',
        type=str,
        help='仅处理指定目录（如 materials）'
    )
    
    args = parser.parse_args()
    
    # 确定项目根目录（脚本所在目录的父目录，或当前工作目录）
    script_dir = Path(__file__).parent
    # 如果脚本在 tools/python/ 下，项目根目录是上两级
    if script_dir.name == 'python' and script_dir.parent.name == 'tools':
        project_root = script_dir.parent.parent
    else:
        project_root = Path.cwd()
    
    print(f"项目根目录: {project_root}")
    print()
    
    created_dirs = []
    moved_files = []
    errors = []
    
    # 初始化目录结构
    if args.init:
        print("正在创建标准目录结构...")
        created_dirs = create_directory_structure(project_root)
        if created_dirs:
            print(f"已创建 {len(created_dirs)} 个目录")
        else:
            print("所有标准目录已存在")
        print()
    
    # 清理和整理文件
    if args.clean:
        print("正在扫描需要移动的文件...")
        files_to_move = find_files_to_move(project_root)
        
        if files_to_move:
            total_files = sum(len(files) for files in files_to_move.values())
            print(f"找到 {total_files} 个需要移动的文件")
            print()
            
            moved_files, errors = move_files(files_to_move, dry_run=args.dry_run)
        else:
            print("没有找到需要移动的文件")
            print()
    
    # 生成报告
    if args.init or args.clean:
        report = generate_report(created_dirs, moved_files, errors, dry_run=args.dry_run)
        print(report)
        
        # 保存报告到文件
        report_file = project_root / 'materials' / 'temp' / f'cleanup_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        if not args.dry_run:
            report_file.parent.mkdir(parents=True, exist_ok=True)
            report_file.write_text(report, encoding='utf-8')
            print(f"\n报告已保存到: {report_file}")
    
    if not args.init and not args.clean:
        parser.print_help()


if __name__ == '__main__':
    main()
