#!/usr/bin/env python3
import sys
import textwrap
import argparse
from pathlib import Path

def get_catfiles_dir():
    script_dir = Path(sys.argv[0]).parent
    cat_dir = script_dir / "catfiles"
    if cat_dir.exists() and cat_dir.is_dir():
        return cat_dir
    return None

def list_available_cats():
    cat_dir = get_catfiles_dir()
    if not cat_dir:
        print("Error: 'catfiles' directory not found next to the script.", file=sys.stderr)
        sys.exit(1)
    txt_files = sorted(cat_dir.glob("*.txt"))
    if not txt_files:
        print("No cat files found in 'catfiles' directory.", file=sys.stderr)
        sys.exit(1)
    
    print("Available cats:")
    for f in txt_files:
        print(f"  {f.stem}")
    print("\nUsage: catsay -c <catname> [message]")
    print("Example: catsay -c greeting Hello")

def load_cat_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().rstrip('\n')
    except FileNotFoundError:
        print(f"Error: cat file '{path}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{path}': {e}", file=sys.stderr)
        sys.exit(1)

def format_bubble(text):
    width = 40
    lines = textwrap.wrap(text, width=width)
    if not lines:
        lines = [""]
    max_len = max(len(line) for line in lines)
    top = " " + "_" * (max_len + 2)
    bottom = " " + "-" * (max_len + 2)
    bubble = [top]
    for i, line in enumerate(lines):
        if len(lines) == 1:
            bubble.append(f"< {line.ljust(max_len)} >")
        elif i == 0:
            bubble.append(f"/ {line.ljust(max_len)} \\")
        elif i == len(lines) - 1:
            bubble.append(f"\\ {line.ljust(max_len)} /")
        else:
            bubble.append(f"| {line.ljust(max_len)} |")
    bubble.append(bottom)
    return "\n".join(bubble)

def main():
    parser = argparse.ArgumentParser(
        description="catsay – A cat that speaks",
        epilog="""
Examples:
  catsay Hello world                     # uses catfiles/greeting.txt
  catsay -c example "Nice to meet you"   # uses catfiles/example.txt
  catsay -c /path/to/custom.txt "Hi"     # uses arbitrary file path
  catsay -l                              # list available cats and usage
  echo "Purr" | catsay
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('message', nargs='*', help='Message to say (optional)')
    parser.add_argument('-l', '--list', action='store_true',
                        help='List all available cat names from catfiles/ and show usage')
    parser.add_argument('-c', '--cat', metavar='NAME_OR_PATH',
                        help='Cat to use: NAME (looks for catfiles/NAME.txt) or full/relative file path')

    args = parser.parse_args()

    if args.list:
        list_available_cats()
        return

    if args.message:
        message = " ".join(args.message)
    elif sys.stdin.isatty():
        message = "Meow?"
    else:
        message = sys.stdin.read().strip()
        if not message:
            message = "Meow?"

    if args.cat:
        if '/' in args.cat or '\\' in args.cat:
            cat_path = args.cat
        else:
            cat_dir = get_catfiles_dir()
            if not cat_dir:
                print("Error: 'catfiles' directory not found next to the script.", file=sys.stderr)
                sys.exit(1)
            cat_path = cat_dir / f"{args.cat}.txt"
        cat_art = load_cat_file(cat_path)
    else:
        cat_dir = get_catfiles_dir()
        if not cat_dir:
            print("Error: 'catfiles' directory not found next to the script. Cannot load default greeting.txt", file=sys.stderr)
            sys.exit(1)
        cat_art = load_cat_file(cat_dir / "greeting.txt")

    bubble = format_bubble(message)
    print(bubble)
    print(cat_art)

if __name__ == "__main__":
    main()
