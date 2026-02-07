def main():
    colors: list[str] = ["black", "brown", "red", "orange",
                         "yellow", "green", "blue", "violet", "grey", "white"]

    input_colors: list[str] = []
    for _ in range(3):
        input_colors.append(input())

    value1: int = colors.index(input_colors[0])
    value2: int = colors.index(input_colors[1])

    mul: int = 10 ** colors.index(input_colors[2])
    result = int(f'{value1}{value2}') * mul
    print(result)


if __name__ == "__main__":
    main()