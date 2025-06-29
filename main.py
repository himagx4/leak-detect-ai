from scanner import scan_text

def main():
    sample_data = "Leaked emails: test@example.com, admin@domain.com"
    found = scan_text(sample_data)
    if found:
        print("🔐 Leak detected:")
        for item in found:
            print(f"- {item}")
    else:
        print("✅ No leaks found.")

if __name__ == "__main__":
    main()

