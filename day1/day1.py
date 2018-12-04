def main():

    with open('./input.txt') as f:
        data = [int(line.strip()) for line in f]

    print(part_one(data.copy()))
    print(part_two(data.copy()))


def part_one(data):
    return sum(data)


def part_two(data):
    seen = set()
    current_freq = 0

    while True:
        for delta in data:
            current_freq += delta

            if current_freq in seen:
                return current_freq

            seen.add(current_freq)


if __name__ == '__main__':
    main()
