# OOPs with Python 🐍

A comprehensive guide and practical implementation of Object-Oriented Programming concepts in Python. This repository contains a detailed Jupyter Notebook that transitions from fundamental concepts to advanced system design patterns.

## Overview
The core of this project is the `OOPs in Python.ipynb` notebook, which serves as a living document of learning. It includes theoretical explanations, memory-address analysis, and hands-on code for real-world scenarios.

## Key Concepts Covered

### 1. Fundamentals
- **Class vs. Object**: Understanding blueprints and instances.
- **Methods vs. Functions**: Distinguishing class-specific behavior from global utility.
- **Constructors (`__init__`)**: Automatic initialization and the role of magic methods.

### 2. The Pillars of OOP
- **Encapsulation**: Data hiding using private variables (`__variable`) and implementing **Getters and Setters** to maintain data integrity.
- **Inheritance**: 
  - **Types**: Single-level, Multi-level, Hierarchical, and Multiple Inheritance.
  - **Method Overriding**: Providing specialized behavior in child classes.
  - **Super Keyword**: Accessing parent constructors and methods without duplication.
- **Polymorphism**: 
  - **Method Overloading**: Handling variable arguments using default values and `*args`.
  - **Operator Overloading**: Customizing standard operators (e.g., `+`, `-`, `*`) using Dunder methods like `__add__` and `__str__`.

### 3. Advanced Relationships & Logic
- **Aggregation**: Building "HAS-A" relationships between classes (e.g., Customer has an Address).
- **MRO (Method Resolution Order)**: Analyzing the C3 Linearization search path in multiple inheritance.
- **Pass by Reference**: Understanding how objects and mutable types behave when passed to functions.

## 🛠️ Practical Implementations
- **ATM System**: A functional ATM class with PIN security, balance tracking, and transaction logic.
- **Fraction Datatype**: A custom numeric type capable of performing arithmetic operations on fractions.

## 💻 Usage
To explore the concepts, open the Jupyter Notebook:
```bash
jupyter notebook "OOPs in Python.ipynb"
