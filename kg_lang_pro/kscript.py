import os
import sys
import argparse
from pathlib import Path


def get_file_icon(filename):
    """Определяет иконку для типа файла"""
    ext = os.path.splitext(filename)[1].lower()

    icon_map = {
        # Текстовые файлы и код
        '.txt': '📄', '.md': '📄', '.rst': '📄', '.log': '📄',
        '.py': '🐍', '.js': '📜', '.jsx': '📜', '.ts': '📜', '.tsx': '📜',
        '.html': '🌐', '.htm': '🌐', '.css': '🎨', '.scss': '🎨', '.sass': '🎨',
        '.json': '🔧', '.xml': '🔧', '.php': '🐘', '.java': '☕',
        '.cpp': '⚙️', '.c': '⚙️', '.h': '⚙️', '.hpp': '⚙️', '.cs': '🔷',
        '.rb': '💎', '.go': '🐹', '.rs': '🦀', '.sql': '🗃️', '.swift': '🐦',

        # Конфигурационные файлы
        '.yml': '⚙️', '.yaml': '⚙️', '.ini': '⚙️', '.cfg': '⚙️', '.conf': '⚙️', '.toml': '⚙️',

        # Изображения
        '.jpg': '🖼️', '.jpeg': '🖼️', '.png': '🖼️', '.gif': '🖼️', '.bmp': '🖼️',
        '.tiff': '🖼️', '.tif': '🖼️', '.svg': '📐', '.ico': '🎯', '.webp': '🖼️',

        # Аудио и видео
        '.mp3': '🎵', '.wav': '🎵', '.ogg': '🎵', '.flac': '🎵', '.aac': '🎵',
        '.mp4': '🎥', '.avi': '🎥', '.mov': '🎥', '.mkv': '🎥', '.flv': '🎥',

        # Документы
        '.pdf': '📕', '.doc': '📘', '.docx': '📘', '.ppt': '📊', '.pptx': '📊',
        '.xls': '📈', '.xlsx': '📈',

        # Архивы
        '.zip': '📦', '.rar': '📦', '.tar': '📦', '.gz': '📦', '.7z': '📦', '.bz2': '📦',

        # Исполняемые файлы
        '.exe': '⚡', '.msi': '⚡', '.sh': '🐚', '.bash': '🐚', '.bat': '💻', '.cmd': '💻',

        # Другие
        '.gitignore': '🔒', '.gitattributes': '🔒', '.dockerfile': '🐳', '.env': '🔑'
    }

    return icon_map.get(ext, '📄')


def should_ignore_folder(folder_name):
    """Проверяет, нужно ли игнорировать папку"""
    ignore_folders = {
        '__pycache__', '.git', 'node_modules', '.idea', '.vscode',
        'venv', 'env', '.env', 'dist', 'build', 'target', 'out',
        'tmp', 'temp', 'cache', 'logs', '__MACOSX', '.pytest_cache',
        '.coverage', 'htmlcov', '.tox', '.mypy_cache', '.DS_Store',
        'thumbs.db', '.Spotlight-V100', '.Trashes', '.github',
        '.gitlab', '.svn', '.hg', '.cache', '.npm', '.yarn'
    }
    return folder_name in ignore_folders


def should_ignore_file(file_path, script_name):
    """Проверяет, нужно ли игнорировать файл"""
    filename = os.path.basename(file_path)

    # Игнорируем сам скрипт
    if filename == script_name:
        return True

    # Игнорируем выходные файлы структуры
    if filename.endswith('_structure.txt') or filename == 'project_structure.txt':
        return True

    return False


def is_important_file(filename):
    """Проверяет, является ли файл важным для отображения (как в исходном проекте)"""
    important_extensions = {
        # Код
        '.py', '.js', '.jsx', '.ts', '.tsx', '.html', '.htm', '.css', '.scss', '.sass',
        '.php', '.rb', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.go', '.rs', '.swift',
        '.kt', '.scala', '.clj', '.hs', '.lua', '.pl', '.pm', '.r', '.m', '.mm',

        # Конфиги
        '.json', '.xml', '.yml', '.yaml', '.ini', '.cfg', '.conf', '.toml',

        # Документация
        '.txt', '.md', '.rst', '.tex', '.adoc', '.asciidoc',

        # Скрипты
        '.sh', '.bash', '.zsh', '.bat', '.cmd', '.ps1',

        # Данные
        '.csv', '.tsv', '.sql',

        # Другие важные
        '.gitignore', '.gitattributes', '.editorconfig', '.dockerignore',

        # Файлы проекта
        'LICENSE', 'README.md', 'requirements.txt', 'package.json', 'Dockerfile',
        'docker-compose.yml', '.env.example', 'Makefile', 'Procfile'
    }

    # Проверяем по расширению
    ext = os.path.splitext(filename)[1].lower()
    if ext in important_extensions:
        return True

    # Проверяем по имени (без расширения)
    name_without_ext = os.path.splitext(filename)[0].lower()
    important_names = {
        'license', 'readme', 'requirements', 'package', 'dockerfile',
        'docker-compose', 'makefile', 'procfile', '.env.example'
    }

    if name_without_ext in important_names:
        return True

    return False


def get_file_size_description(file_path):
    """Возвращает читаемое описание размера файла"""
    try:
        size = os.path.getsize(file_path)
        if size == 0:
            return " (пустой)"
        elif size < 1024:
            return f" ({size} B)"
        elif size < 1024 * 1024:
            return f" ({size // 1024} KB)"
        elif size < 1024 * 1024 * 1024:
            return f" ({size // (1024 * 1024)} MB)"
        else:
            return f" ({size // (1024 * 1024 * 1024)} GB)"
    except:
        return ""


def read_text_file_safe(file_path):
    """Безопасное чтение текстового файла с определением кодировки"""
    encodings = ['utf-8', 'utf-8-sig', 'cp1251', 'windows-1251', 'iso-8859-1', 'windows-1252', 'latin-1']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()

            # Проверяем на наличие NUL символов и других проблем
            if any(ord(c) == 0 for c in content):  # NUL character
                # Пробуем читать как бинарный и декодировать с обработкой ошибок
                with open(file_path, 'rb') as f:
                    binary_content = f.read()
                # Пробуем декодировать, игнорируя ошибки
                content = binary_content.decode('utf-8', errors='ignore')
                # Убираем NUL символы
                content = content.replace('\x00', '')

            return content, encoding
        except (UnicodeDecodeError, UnicodeError):
            continue

    # Если все кодировки не сработали, пробуем бинарное чтение с обработкой ошибок
    try:
        with open(file_path, 'rb') as f:
            binary_content = f.read()
        content = binary_content.decode('utf-8', errors='ignore')
        content = content.replace('\x00', '')  # Убираем NUL символы
        return content, 'binary_fallback'
    except:
        return None, None


def build_directory_tree(directory_path, script_name):
    """Строит дерево директорий и собирает информацию о файлах"""
    all_files = []
    important_files = []

    # Получаем имя корневой папки
    root_folder_name = os.path.basename(os.path.normpath(directory_path))
    if not root_folder_name or root_folder_name == '.':
        root_folder_name = os.path.basename(os.getcwd())

    # Создаем корневой узел с именем проекта
    tree = {root_folder_name: {}}

    for root, dirs, files in os.walk(directory_path):
        # Игнорируем технические папки
        dirs[:] = [d for d in dirs if not should_ignore_folder(d)]

        for file in files:
            file_path = os.path.join(root, file)

            # Игнорируем сам скрипт и неважные файлы
            if should_ignore_file(file_path, script_name) or not is_important_file(file):
                continue

            rel_path = os.path.relpath(file_path, directory_path)

            important_files.append((file_path, rel_path, file))
            all_files.append((file_path, rel_path, file))

            # Строим дерево относительно корневой папки
            dir_path = os.path.dirname(rel_path)
            if dir_path == '':
                dir_path = root_folder_name
            else:
                dir_path = os.path.join(root_folder_name, dir_path)

            current = tree
            parts = dir_path.split(os.sep)
            for part in parts:
                if part not in current:
                    current[part] = {}
                current = current[part]
            current[file] = {}

    return tree, all_files, important_files, root_folder_name


def print_tree_to_file(tree, output, all_files, level=0, prefix='', is_last=True):
    """Рекурсивно записывает дерево в файл"""
    keys = list(tree.keys())
    keys.sort()

    for i, key in enumerate(keys):
        is_last_item = i == len(keys) - 1
        connector = '└── ' if is_last_item else '├── '

        if tree[key]:  # Это папка
            output.write(f"{prefix}{connector}📁 {key}/\n")
            new_prefix = prefix + ('    ' if is_last_item else '│   ')
            print_tree_to_file(tree[key], output, all_files, level + 1, new_prefix, is_last_item)
        else:  # Это файл
            icon = get_file_icon(key)
            # Находим полный путь к файлу для получения размера
            file_info = next((f for f in all_files if f[2] == key), None)
            size_desc = ""
            if file_info:
                size_desc = get_file_size_description(file_info[0])
            output.write(f"{prefix}{connector}{icon} {key}{size_desc}\n")


def process_directory(directory_path, output_path, script_name):
    """Основная функция обработки директории"""
    print(f"🔍 Анализируем структуру проекта: {directory_path}")

    tree, all_files, important_files, root_folder_name = build_directory_tree(directory_path, script_name)

    with open(output_path, 'w', encoding='utf-8') as output:
        # Записываем структуру проекта
        output.write("📁 СТРУКТУРА ПРОЕКТА (ВСЕ ФАЙЛЫ И ПАПКИ):\n\n")
        output.write("💡 Игнорируются только технические папки (__pycache__, .git, node_modules и т.д.)\n\n")

        print_tree_to_file(tree, output, all_files)

        # Записываем содержимое важных файлов
        output.write("\n\n" + "=" * 80 + "\n")
        output.write("СОДЕРЖИМОЕ ТЕКСТОВЫХ ФАЙЛОВ:\n")
        output.write("💡 Показывается содержимое только текстовых файлов\n")
        output.write("=" * 80 + "\n\n")

        if important_files:
            for file_path, rel_path, filename in important_files:
                # Пропускаем сам скрипт
                if should_ignore_file(file_path, script_name):
                    continue

                content, encoding = read_text_file_safe(file_path)
                if content is not None:
                    # Ограничиваем размер очень больших файлов
                    if len(content) > 1000000:  # 1MB
                        content = content[:1000000] + f"\n\n[ФАЙЛ ОБРЕЗАН, РАЗМЕР ПРЕВЫШАЕТ 1MB]\n"

                    # Добавляем имя корневой папки к относительному пути
                    full_rel_path = os.path.join(root_folder_name, rel_path) if rel_path != '.' else root_folder_name
                    output.write(f"--- {full_rel_path} ---\n{content}\n" + "-" * 40 + "\n\n")
                else:
                    full_rel_path = os.path.join(root_folder_name, rel_path) if rel_path != '.' else root_folder_name
                    output.write(f"--- {full_rel_path} ---\n[ФАЙЛ НЕ МОЖЕТ БЫТЬ ПРОЧИТАН КАК ТЕКСТ]\n\n")
        else:
            output.write("Важные файлы не найдены\n\n")


def main():
    parser = argparse.ArgumentParser(description='Создает текстовую структуру проекта')
    parser.add_argument('directory', nargs='?', default='.',
                        help='Директория для анализа (по умолчанию: текущая директория)')
    parser.add_argument('-o', '--output',
                        help='Имя выходного файла (по умолчанию: <имя_проекта>.txt)')

    args = parser.parse_args()

    directory_path = os.path.abspath(args.directory)

    # Получаем имя текущего скрипта
    script_name = os.path.basename(__file__)

    # Получаем имя корневой папки для имени файла
    root_folder_name = os.path.basename(os.path.normpath(directory_path))
    if not root_folder_name or root_folder_name == '.':
        root_folder_name = os.path.basename(os.getcwd())

    # Определяем имя выходного файла
    if args.output:
        output_path = args.output
    else:
        output_path = f"{root_folder_name}.txt"

    if not os.path.exists(directory_path):
        print(f"❌ Ошибка: Директория '{directory_path}' не существует")
        sys.exit(1)

    if not os.path.isdir(directory_path):
        print(f"❌ Ошибка: '{directory_path}' не является директорией")
        sys.exit(1)

    try:
        process_directory(directory_path, output_path, script_name)
        print(f"✅ Текстовая структура успешно создана: {output_path}")
    except Exception as e:
        print(f"❌ Ошибка при создании структуры: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()