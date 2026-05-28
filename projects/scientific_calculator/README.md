# Scientific Calculator

An upgraded version of the basic calculator — built with a continuous loop,
error handling and extended mathematical operations using Python's `math` module.

## Features

| Option | Operation |
|--------|-----------|
| 1 | Addition |
| 2 | Subtraction |
| 3 | Multiplication |
| 4 | Division |
| 5 | Square Root |
| 6 | Sine |
| 7 | Cosine |
| 8 | Tangent |
| 9 | View History |
| 10 | Clear History |
| 11 | Exit |

## How it works
- Press `0` anytime to view the menu
- Trig functions (sin, cos, tan) accept input in degrees
- All operations are logged to history and can be cleared
- Invalid inputs and division by zero are handled gracefully

## Key Concepts
- `math` module for advanced operations
- Continuous `while True` loop with clean exit
- `try/except` for error handling
- `enumerate()` for formatted history display
- Separation of single and double argument operations
- History tracking with a list