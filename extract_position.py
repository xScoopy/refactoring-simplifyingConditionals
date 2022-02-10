# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):
    if not line:
        return None
    if 'debug' in line or 'error' in line:
        return None
    if 'x:' in line:
        start_index = line.find('x:') + 2
        return line[start_index:]  # from start_index to the end.
    return None


if __name__ == "__main__":
    result1 = extract_position(
        '|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position(
        '|update| the positron location in the particle accelerator is x:21.432')
    print(result2)
