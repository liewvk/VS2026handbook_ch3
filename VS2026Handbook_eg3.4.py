raw_values = ['14', 'oops', '27']
for raw in raw_values:
    try:
        print('Parsed:', int(raw))
    except ValueError:
        print('Skipped invalid value:', raw)


