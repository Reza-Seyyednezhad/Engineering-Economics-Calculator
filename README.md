# Engineering Economics Calculator 🧮

A comprehensive desktop application built with Python and Tkinter for performing engineering economics and financial analysis calculations. This tool implements standard time-value-of-money formulas and economic decision-making methodologies used in engineering project evaluation.

## ✨ Features

- **Graphical User Interface**: User-friendly Tkinter-based interface with dark theme
- **Multiple Analysis Methods**:
  - Basic time-value calculations (P/F, F/P, A/F, F/A, P/A, A/P, P/G, A/G)
  - Present Worth Method (NPW calculation)
  - Annual Worth Method (EUAC/NAW calculation)
  - Payback Period Method (PBPV analysis)
- **Batch Calculations**: Support for multiple time periods and cash flow series
- **Flexible Input**: Handle both single calculations and complex multi-period scenarios

## 📁 Project Structure

```
Economic-Project/
├── Application.py          # Main GUI application (Tkinter)
├── formulas.py            # Core financial calculation functions
├── Backend.py             # Command-line interface version
├── Methods/
│   └── Present Worth Method.py  # NPW calculation module
└── requirements.txt       # Python dependencies
```

## 🚀 Installation & Usage

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Quick Start
1. Clone the repository:
```bash
git clone https://github.com/PyRezaSeyyednezhad/Economic-Project.git
cd Economic-Project
```

2. Run the application:
```bash
python Application.py
```

### Alternative Usage
- **Command-line version**: Run `python Backend.py` for terminal-based calculations
- **Import formulas**: Use `from formulas import *` to access calculation functions in your own projects

## 📊 Available Calculation Methods

### Time-Value of Money Factors
| Method | Formula | Description |
|--------|---------|-------------|
| **P/F** | Present Worth Factor | Converts future amount to present worth |
| **F/P** | Future Worth Factor | Converts present amount to future worth |
| **P/A** | Present Worth of Annuity | Converts uniform series to present worth |
| **A/P** | Capital Recovery Factor | Converts present worth to uniform series |
| **F/A** | Future Worth of Annuity | Converts uniform series to future worth |
| **A/F** | Sinking Fund Factor | Converts future worth to uniform series |
| **P/G** | Present Worth Gradient | Handles arithmetic gradient series |
| **A/G** | Uniform Gradient Series | Converts gradient to uniform series |

### Economic Decision Methods
1. **Present Worth Method (PWM)**
   - Net Present Worth (NPW) calculation
   - Cost vs. Income analysis
   - Multiple cash flow period support

2. **Annual Worth Method (NAW)**
   - Equivalent Uniform Annual Cost (EUAC)
   - Net Annual Worth (NAW) = EUAB - EUAC
   - Three calculation approaches available

3. **Payback Period Method (PBPV)**
   - Discounted payback period calculation
   - Minimum Attractive Payback Period (MAPP) comparison
   - Project approval/rejection recommendation

## 🔧 Technical Implementation

### Core Formulas (`formulas.py`)
The module implements standard engineering economics formulas:
- All functions accept `i` (interest rate %), `n` (periods), and optional cash flow amounts
- Each function returns both the factor value and calculated amount
- Interest rates are automatically converted from percentage to decimal

Example usage:
```python
from formulas import F_A, P_A

# Calculate future worth of annuity
factor, amount = F_A(5, 10, 1000)  # i=5%, n=10, A=1000

# Calculate present worth of annuity
factor, amount = P_A(8, 20, 500)   # i=8%, n=20, A=500
```

### Application Architecture (`Application.py`)
- **Tabbed Interface**: Organized by calculation methodology
- **Data Validation**: Input checking and error handling
- **Batch Processing**: Support for multiple cash flow entries
- **Result Logging**: Detailed calculation history

## 📈 Example Calculations

### Basic Factor Calculation
1. Select calculation method (e.g., F/A)
2. Enter interest rate (i%) and number of periods (n)
3. Enter cash flow amount (A, F, or P)
4. Get factor value and calculated amount

### Present Worth Analysis
1. Add multiple cash flows with their timing
2. Specify whether each is income or cost
3. Enter initial investment
4. Calculate Net Present Worth (NPW)

### Payback Period Determination
1. Enter initial investment (P) and MAPP threshold
2. Specify first year income and annual increase
3. Calculate discounted payback period
4. Compare with MAPP for project decision

## 🛠️ Development

### Adding New Features
1. Extend `formulas.py` with new calculation functions
2. Add new tabs or sections in `Application.py`
3. Follow existing patterns for GUI consistency

### Code Style
- Functions use descriptive names with parameter types
- GUI uses consistent dark theme colors
- Error handling with informative messages

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Standard engineering economics formulas from textbooks
- Python Tkinter community for GUI examples
- Engineering economics principles for project evaluation

## 📚 Learning Resources

- Engineering Economy textbooks (Blank, Tarquin)
- Time Value of Money concepts
- Capital budgeting techniques

---

**Note**: This tool is designed for educational and professional engineering economics analysis. Always verify critical calculations with multiple methods and consult financial professionals for important decisions.
