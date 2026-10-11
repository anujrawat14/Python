# Python `time` Module

## 1. Introduction

* The `time` module is a built-in Python module used to work with time.
* It provides functions to get the current time, pause program execution, measure execution time, and format time.

```python
import time
```

## 2. `time.time()`

* Returns the current time as a floating-point number.
* The value represents the number of seconds since the Unix Epoch: January 1, 1970, at 00:00:00 UTC.

```python
import time

current_time = time.time()

print(current_time)
# Output: A floating-point timestamp, such as 1791712345.123
# The exact value depends on when the program runs.
```

## 3. `time.sleep()`

* Pauses the execution of the current thread for the specified number of seconds.
* It accepts fractional seconds too.

```python
import time

print("Hello")

time.sleep(2)  # Pause execution for approximately 2 seconds.

print("World")
```

**Output:**

```text
Hello
World
```

The word `World` is printed after the pause.

```python
time.sleep(0.5)  # Pause for approximately half a second.
```

## 4. `time.ctime()`

* Converts a timestamp into a readable local date and time string.
* If no timestamp is supplied, it uses the current time.

```python
import time

print(time.ctime())
# Output: A readable representation of the current local date and time.

timestamp = time.time()
print(time.ctime(timestamp))
# Converts the timestamp into a readable local date and time.
```

## 5. `time.localtime()`

* Converts a timestamp into a `struct_time` object representing local time.
* If no timestamp is supplied, it uses the current time.

```python
import time

current = time.localtime()

print(current)
print(current.tm_year)   # Year
print(current.tm_mon)    # Month (1-12)
print(current.tm_mday)   # Day of the month
print(current.tm_hour)   # Hour (0-23)
print(current.tm_min)    # Minute (0-59)
print(current.tm_sec)    # Second (0-60)
print(current.tm_wday)   # Weekday (Monday = 0)
print(current.tm_yday)   # Day of the year (1-366)
```

## 6. `time.gmtime()`

* Converts a timestamp into a `struct_time` object representing UTC time.
* Unlike `localtime()`, it uses UTC rather than the computer's local time zone.

```python
import time

print(time.gmtime())
# Current time in UTC.

print(time.gmtime().tm_year)
# Current year in UTC.
```

### Difference: `localtime()` vs `gmtime()`

| Function           | Time representation |
| ------------------ | ------------------- |
| `time.localtime()` | Local time zone     |
| `time.gmtime()`    | UTC                 |

## 7. `time.strftime()`

* Converts a time tuple or `struct_time` object into a formatted string.
* Use format codes to decide how the date and time should appear.

```python
import time

current = time.localtime()

print(time.strftime("%Y-%m-%d", current))
# Output format: YYYY-MM-DD

print(time.strftime("%H:%M:%S", current))
# Output format: HH:MM:SS

print(time.strftime("%d/%m/%Y %I:%M %p", current))
# Example format: 11/10/2026 11:30 AM
# The actual output depends on the current local time.
```

### Common format codes

| Code | Meaning                | Example   |
| ---- | ---------------------- | --------- |
| `%Y` | Four-digit year        | `2026`    |
| `%y` | Two-digit year         | `26`      |
| `%m` | Month (01-12)          | `10`      |
| `%d` | Day (01-31)            | `11`      |
| `%H` | Hour in 24-hour format | `14`      |
| `%I` | Hour in 12-hour format | `02`      |
| `%M` | Minute                 | `30`      |
| `%S` | Second                 | `45`      |
| `%p` | AM or PM               | `PM`      |
| `%A` | Full weekday name      | `Sunday`  |
| `%a` | Abbreviated weekday    | `Sun`     |
| `%B` | Full month name        | `October` |
| `%b` | Abbreviated month      | `Oct`     |
| `%j` | Day of the year        | `284`     |
| `%w` | Weekday (Sunday = 0)   | `0`       |

## 8. `time.strptime()`

* Parses a string representing a date or time into a `struct_time` object.
* The format must match the input string.

```python
import time

date_string = "11-10-2026"

parsed_time = time.strptime(date_string, "%d-%m-%Y")

print(parsed_time)
print(parsed_time.tm_year)  # Output: 2026
print(parsed_time.tm_mon)   # Output: 10
print(parsed_time.tm_mday)  # Output: 11
```

**Remember:**

* `strftime()` converts time into a formatted string.
* `strptime()` parses a string into a time object.

## 9. `time.perf_counter()`

* Returns a high-resolution performance counter.
* It is useful for measuring elapsed time, such as how long a function or piece of code takes to run.
* Its absolute starting value is not meaningful; compare two readings.

```python
import time

start = time.perf_counter()

# Code whose execution time we want to measure.
total = sum(range(1_000_000))

end = time.perf_counter()

elapsed = end - start

print("Execution time:", elapsed, "seconds")
```

**Important:** Use `perf_counter()` for measuring elapsed time instead of subtracting two `time.time()` values.

## 10. `time.monotonic()`

* Returns a clock that cannot go backward due to changes to the system clock.
* It is useful for measuring elapsed time and timeouts.
* Its starting value is undefined, so only differences between readings are meaningful.

```python
import time

start = time.monotonic()

time.sleep(1)

end = time.monotonic()

print("Elapsed time:", end - start, "seconds")
```

## 11. `time.mktime()`

* Converts a local `struct_time` object into a timestamp.
* It is essentially the reverse of `time.localtime()`.

```python
import time

local_time = time.localtime()

timestamp = time.mktime(local_time)

print(timestamp)
```

## 12. Complete Example

```python
import time

# Get the current timestamp.
timestamp = time.time()
print("Timestamp:", timestamp)

# Display the current local time.
current = time.localtime()
print("Local time:", current)

# Format the current date and time.
formatted = time.strftime("%d-%m-%Y %H:%M:%S", current)
print("Formatted time:", formatted)

# Pause the program.
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done!")

# Measure execution time.
start = time.perf_counter()

total = sum(range(1_000_000))

end = time.perf_counter()

print("Total:", total)
print("Execution time:", end - start, "seconds")
```

## 13. Quick Revision

| Function              | Purpose                                             |
| --------------------- | --------------------------------------------------- |
| `time.time()`         | Get the current Unix timestamp                      |
| `time.sleep(seconds)` | Pause execution                                     |
| `time.ctime()`        | Convert a timestamp to a readable local time string |
| `time.localtime()`    | Get local time as `struct_time`                     |
| `time.gmtime()`       | Get UTC time as `struct_time`                       |
| `time.strftime()`     | Format time into a string                           |
| `time.strptime()`     | Parse a string into `struct_time`                   |
| `time.perf_counter()` | Measure elapsed execution time accurately           |
| `time.monotonic()`    | Measure elapsed time using a non-decreasing clock   |
| `time.mktime()`       | Convert local `struct_time` into a timestamp        |

### Important Interview Points

1. `time` is a built-in Python module; no separate installation is required.
2. `time.time()` returns seconds since the Unix Epoch.
3. `time.sleep()` pauses the current thread; it does not pause the entire computer.
4. `strftime()` formats a time object into a string, while `strptime()` parses a string into a time object.
5. Use `perf_counter()` to benchmark code execution.
6. Use `monotonic()` when measuring elapsed time or handling timeouts.
7. The `time` module works with timestamps and clock-based operations. For more convenient date arithmetic and time-zone-aware dates, Python also provides the `datetime` module.
