import os

def analyze_code():
    suggestions = []

    # Simple AI-like static analysis (our custom logic for now)
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                    if "print(" in code:
                        suggestions.append(f"[{file}] Consider replacing print statements with logging module.")

                    if "add(" in code and "return" in code:
                        suggestions.append(f"[{file}] Function 'add' looks fine but try adding type hints.")

    return suggestions

if __name__ == "__main__":
    results = analyze_code()
    print("\n=== AI Code Review Suggestions ===")
    if results:
        for r in results:
            print(" -", r)
    else:
        print("No issues found. Good job!")
