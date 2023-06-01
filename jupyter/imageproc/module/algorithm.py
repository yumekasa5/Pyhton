def fibonacci(n):
    # メモ化用の配列を初期化
    memo = [None] * (n + 1)

    # フィボナッチ数列を再帰的に計算する関数
    def fibonacci_recursive(n):
        # ベースケース
        if n <= 1:
            return n

        # メモが存在する場合は計算結果を返す
        if memo[n] is not None:
            return memo[n]

        # メモが存在しない場合は再帰的に計算
        memo[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        return memo[n]

    # フィボナッチ数列の計算結果を返す
    return fibonacci_recursive(n)

# フィボナッチ数列の第10項を計算する例
result = fibonacci(10)
print(result)