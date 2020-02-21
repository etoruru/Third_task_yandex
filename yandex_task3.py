def read_file():
    f = open('text.txt', 'r')
    text = f.readlines()
    text = [line.replace('\n', '') for line in text]
    return text


def find_min(lst):
    min = lst[0]
    for i in lst:
        if min >= i:
            min = i
    return min


def compare(sunbeds):
    min_xor = []
    sunbeds_list = sunbeds.split(' ')
    for i in range(len(sunbeds_list) - 1):
        x = int(sunbeds_list[i])^int(sunbeds_list[i+1])
        min_xor.append(x)
    return min_xor


def main(text):
    min = []
    num_of_tests = int(text[0])
    i = 0
    while i <= num_of_tests:
        i += 1
        num_of_sunbeds = int(text[i])
        row_sunbeds = text[i+1]
        xor_values = compare(row_sunbeds)
        min_xor = find_min(xor_values)
        min.append(min_xor)
        i += 1
    return min

if __name__ == '__main__':
    text = read_file()
    min = main(text)
    print(min)
