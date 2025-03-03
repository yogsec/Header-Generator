import argparse
import art

VERSION = "v1.0"
DEFAULT_GITHUB = "https://github.com/yogsec"
DEFAULT_DONATE = "https://buymeacoffee.com/yogsec"

HEADER_ART = """
 _     _ _______ _______ ______  _______  ______       ______ _______ __   _ _______  ______ _______ _______  _____   ______
|_____| |______ |_____| |     \ |______ |_____/      |  ____ |______ | \  | |______ |_____/ |_____|    |    |     | |_____/
|     | |______ |     | |_____/ |______ |    \_      |_____| |______ |  \_| |______ |    \_ |     |    |    |_____| |    \_

"""

def generate_header(word):
    return art.text2art(word, font="cyberlarge")

def main():
    parser = argparse.ArgumentParser(description="Beautiful Header Generator Tool")

    parser.add_argument("-u", "--text", required=True, help="Text to convert to header (wrap in double quotes)")
    parser.add_argument("-s", "--save", action="store_true", help="Save output to file")
    parser.add_argument("-v", "--version", action="store_true", help="Show version and exit")
    parser.add_argument("-g", "--github", default=DEFAULT_GITHUB, help="Custom GitHub URL (optional)")
    parser.add_argument("-d", "--donate", default=DEFAULT_DONATE, help="Custom Donate URL (optional)")

    args = parser.parse_args()

    if args.version:
        print(f"Header Tool - Version {VERSION}")
        return

    text = args.text

    if not all(c.isalnum() or c.isspace() for c in text):
        print("❌ Only alphabets, numbers, and spaces allowed in text.")
        return

    # First print the fixed header
    print(HEADER_ART)

    # Then generate and print the custom header text
    header = generate_header(text)
    print(header)

    # Finally, print GitHub and Donate links
    print(f"GitHub - {args.github}")
    print(f"Donate ❤️‍🩹 - {args.donate}")

    # Save to file if needed
    if args.save:
        filename = f"{text.replace(' ', '_')}_header.txt"
        with open(filename, "w") as file:
            file.write(HEADER_ART)
            file.write(header)
            file.write(f"\nGitHub - {args.github}\n")
            file.write(f"Donate ❤️‍🩹 - {args.donate}\n")

        print(f"✅ Header saved to {filename}")

if __name__ == "__main__":
    main()

