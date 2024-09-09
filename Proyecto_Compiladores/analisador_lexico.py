import re

TOKENS_PATTERNS = {
    'HEADER': r'^\s*(#{1,6})\s',  # Encabezados con # (de H1 a H6)
    'PARAGRAPH': r'^\s*\*\s',  # Identificación de párrafos con *
    'LIST_ITEM': r'^\s*-\s',  # Identificación de ítems de lista con -
    'TEXT': r'[a-zA-Z0-9]+',  # Texto normal o palabras clave
    'NEWLINE': r'\n',  # Saltos de línea
    'UNKNOWN': r'.+'  # Cualquier otro símbolo desconocido
}


class Lexer:
    def __init__(self, input_text):
        self.text = input_text
        self.position = 0
        self.tokens = []

    def get_next_token(self):
        if self.position >= len(self.text):
            return None  # Si hemos llegado al final del texto

        while self.position < len(self.text) and self.text[self.position] == ' ':
            self.position += 1

        for token_type, pattern in TOKENS_PATTERNS.items():
            regex = re.compile(pattern)
            match = regex.match(self.text, self.position)

            if match:
                token_value = match.group(0)
                self.position += len(token_value)  # Movemos la posición según el largo del token
                return (token_type, token_value)

        return None

    def tokenize(self):
        while self.position < len(self.text):
            token = self.get_next_token()
            if token:
                self.tokens.append(token)
            else:
                self.position += 1
        return self.tokens


def read_markdown_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    file_path = 'test_tokens.md'  # Nombre del archivo Markdown
    markdown_text = read_markdown_file(file_path)

    lexer = Lexer(markdown_text)
    tokens = lexer.tokenize()

    for token in tokens:
        print(f'Tipo de token: {token[0]}, Valor del token: {token[1]}')


if __name__ == '__main__':
    main()
