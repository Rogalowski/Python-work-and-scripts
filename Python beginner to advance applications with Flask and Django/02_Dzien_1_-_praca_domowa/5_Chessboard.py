def chessboard(n=8):
    lines = []
    for i in range(n):
        if i % 2 == 0:
            # print(((n // 2) * "# ")) - bez lines
            lines.append((n // 2) * "# ")
        else:
            lines.append((n // 2) * " #")
            # print(((n // 2) * " #"))    - bez lines
    return "\n".join(lines)

c = chessboard()
print(c)