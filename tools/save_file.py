import os

def save_output(content, filename):

    os.makedirs(
        os.path.dirname(filename),
        exist_ok=True
    )

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Saved: {filename}")