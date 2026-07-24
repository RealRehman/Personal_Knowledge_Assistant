def chunk_text(text):
    lines = text.splitlines()

    chunk_size = 2

    for i in range(0, len(lines), chunk_size):

        chunk = lines[i:i + chunk_size]

        print("----- Chunk -----")

        print("\n".join(chunk))

        print()