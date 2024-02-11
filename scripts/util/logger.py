class PromptLogger():
    """プロンプト等様々な情報を記録・出力するロガー"""
    def __init__(self) -> None:
        self.message_list = []

    def append(self, message: str) -> str:
        """ログリストに追加"""
        self.message_list.append(message)
        return message

    def get_log_newlines(self) -> str:
        """改行文字で結合したログ内容を返す"""
        return '\n'.join(self.message_list)
    