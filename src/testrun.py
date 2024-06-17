class ExampleClass:
    colors = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
        "bold": 1,
        "underline": 4
    }

    def centered(self, text, color, end=False):
        if color not in self.colors:
            raise ValueError(f"Color '{color}' is not valid. Choose from {', '.join(self.colors.keys())}.")
        
        if color == "underline":
            t = f"\33[4m{text}\33[0m"
        else:
            t = f"\33[{self.colors[color]}m{text}\33[0m"
        
        formatted_text = '{:^115}'.format(t)
        
        if end:
            print(formatted_text, end="")
        else:
            print(formatted_text)

# Example usage:
example = ExampleClass()
example.centered("(1) Sign-Up", "yellow", end=True)
example.centered("\t(2) Log-In", "yellow")
