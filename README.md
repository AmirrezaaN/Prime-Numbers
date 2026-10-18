# Prime Number Checker

A simple Python script that checks whether the numbers you enter are prime.

## What is a prime number?

A prime number is a whole number greater than 1 that can only be divided evenly by 1 and itself.

```
Prime:      2, 3, 5, 7, 11, 13, 17, 19, ...
Not prime:  4, 6, 8, 9, 10, 12, 14, 15, ...
```

## Requirements

- Python 3.x
- No external libraries needed (uses Python's built-in `math` module)

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Run the script:
   ```bash
   python prime_checker.py
   ```

3. Enter how many numbers you want to check, then enter them one by one.

## Example

```
How many numbers do you want to enter for the diagnosis?4
[INPUT] Enter your numbers one by one :7
[INPUT] Enter your numbers one by one :12
[INPUT] Enter your numbers one by one :1
[ERROR] 0 and 1 are neither prime nor not prime.
[INPUT] Enter your numbers one by one :29
[INFO] The number 7 is prime.
[INFO] The number 12 is not prime.
[INFO] The number 29 is prime.
```

## How It Works

1. The script asks how many numbers you want to check.
2. It collects each number. `0` and `1` are rejected with an error message, since they aren't prime.
3. For each number `x`, it checks for divisors starting at the square root of `x` and counting down to 2.
   - If any of these divides `x` evenly, the number is **not prime**.
   - If none do, the number is **prime**.

### Why only check up to the square root?

If a number has a divisor larger than its square root, it must also have a matching divisor smaller than its square root. So checking up to √x is enough, which makes the script much faster for large numbers.

## Code

```python
import math

inputs_number = int(input("How many numbers do you want to enter for the diagnosis?"))
numbers = []
for i in range(inputs_number):
    number = int(input("[INPUT] Enter your numbers one by one :"))
    if number == 0 or number == 1:
        print("[ERROR] 0 and 1 are neither prime nor not prime.")
    else:
        numbers.append(number)


for x in numbers:
    y = int(math.sqrt(x))
    while y > 1:
        if x % y == 0:
            print(f"[INFO] The number {x} is not prime.")
            break
        y -= 1

    if y == 1:
        print(f"[INFO] The number {x} is prime.")
```

## Known Limitations

- Negative numbers cause an error, because `math.sqrt()` can't handle them.
- Entering a non-number (like text or a decimal) will crash the script.
- Results are shown only after all numbers have been entered.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
