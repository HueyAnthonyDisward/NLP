def cky_parse(words, grammar):
    """
    Hàm CKY để kiểm tra xem một chuỗi có thể được sinh ra từ ngữ pháp CNF hay không.

    :param words: Danh sách các từ trong câu cần phân tích.
    :param grammar: Một danh sách chứa các quy tắc ngữ pháp ở dạng CNF.
                    Định dạng: { "Non-terminal": [(X, Y), "terminal", ...] }
    :return: Bảng parse table chứa các non-terminals có thể sinh ra chuỗi.
    """
    n = len(words)

    # Khởi tạo bảng parse table (n x n)
    table = [[set() for _ in range(n + 1)] for _ in range(n)]

    # Bước 1: Xử lý các từ đơn (unary rules)
    for i, word in enumerate(words):
        for lhs, rhs in grammar.items():
            if word in rhs:  # Nếu từ là một terminal trong ngữ pháp
                table[i][i + 1].add(lhs)

    # Bước 2: Xử lý các quy tắc nhị phân (binary rules)
    for width in range(2, n + 1):  # Độ rộng của span (2 đến n)
        for start in range(n - width + 1):  # Điểm bắt đầu
            end = start + width  # Điểm kết thúc

            for mid in range(start + 1, end):  # Chia nhỏ câu
                for lhs, rhs in grammar.items():
                    for rule in rhs:
                        if isinstance(rule, tuple) and len(rule) == 2:
                            left, right = rule
                            if left in table[start][mid] and right in table[mid][end]:
                                table[start][end].add(lhs)

    # Kiểm tra xem ký hiệu bắt đầu (S) có trong ô (0, n) không
    return table, "S" in table[0][n]


# Định nghĩa ngữ pháp ở dạng CNF
grammar_cnf = {
    "S": [("NP", "VP")],
    "VP": [("V", "NP")],
    "NP": [("DT", "N")],
    "DT": ["the"],
    "N": ["cat", "dog"],
    "V": ["sees"]
}

# Câu đầu vào
sentence = ["the", "cat", "sees"]

# Chạy CKY Parser
parse_table, result = cky_parse(sentence, grammar_cnf)

# Hiển thị kết quả
print("Parse Table:")
for row in parse_table:
    print(row)
print("\nCâu hợp lệ theo ngữ pháp CNF?", "✅ YES" if result else "❌ NO")
