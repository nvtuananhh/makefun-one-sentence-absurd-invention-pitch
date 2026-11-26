# One-Sentence Absurd Invention Pitch — entry v1
# Writes a single sentence pitching a ridiculous invention
# that fixes a tiny everyday annoyance.
import os

ENTRY = "My doorbell files a formal noise complaint against anyone who rings it twice, and it has already sued the postman three times."

# The pitch: the doorbell turns the tables — it punishes the ringer
# instead of announcing them. One sentence, one twist at the end.
assert 1 <= len(ENTRY) <= 220
assert ENTRY.count(".") == 1 and ENTRY.endswith(".")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
