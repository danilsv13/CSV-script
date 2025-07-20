import argparse
import csv
from tabulate import tabulate

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='CSV file to process')
    parser.add_argument('--where', help='Filtering condition in format column=value, column>value or column<value')
    parser.add_argument('--aggregate', help='Aggregate operation like rating=avg, price=max, etc.')
    return parser.parse_args()

def parse_condition(condition):
    for op in ['>=', '<=', '>', '<', '=']:
        if op in condition:
            col, val = condition.split(op)
            return col.strip(), op, val.strip()
    raise ValueError("Invalid condition format")

def apply_filter(rows, col, op, val):
    filtered = []
    for row in rows:
        cell = row[col]
        try:
            cell_val = float(cell)
            val_cast = float(val)
        except ValueError:
            cell_val = cell
            val_cast = val

        if op == '=' and cell_val == val_cast:
            filtered.append(row)
        elif op == '<' and cell_val < val_cast:
            filtered.append(row)
        elif op == '>' and cell_val > val_cast:
            filtered.append(row)
        elif op == '<=' and cell_val <= val_cast:
            filtered.append(row)
        elif op == '>=' and cell_val >= val_cast:
            filtered.append(row)
    return filtered

def apply_aggregation(rows, col, func):
    nums = [float(row[col]) for row in rows]
    if func == 'avg':
        return sum(nums) / len(nums)
    elif func == 'min':
        return min(nums)
    elif func == 'max':
        return max(nums)

def main():
    args = parse_args()

    with open(args.file, newline='') as csvfile:
        reader = list(csv.DictReader(csvfile))
        headers = reader[0].keys()

        if args.where:
            col, op, val = parse_condition(args.where)
            reader = apply_filter(reader, col, op, val)

        if args.aggregate:
            col, func = args.aggregate.split('=')
            result = apply_aggregation(reader, col, func)
            print(tabulate([[func, round(result, 2)]], headers=[func, 'value']))
        else:
            print(tabulate(reader, headers='keys', tablefmt='grid'))

if __name__ == '__main__':
    main()
