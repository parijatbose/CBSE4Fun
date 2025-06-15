# 🧠 CBSE Math Solver

A comprehensive, modular mathematics problem solver designed specifically for CBSE Class 10 curriculum with step-by-step solutions, knowledge base, and practice tests.

## 🌟 Features

- **📚 Complete CBSE Coverage**: All 14 chapters from Class 10 NCERT Mathematics
- **🎯 Step-by-Step Solutions**: Detailed explanations for every problem
- **📊 Interactive Visualizations**: Graphs and plots for better understanding
- **📝 Knowledge Base**: MCQs, short answers, and long answer questions
- **🧪 Practice Tests**: Auto-generated chapter-wise tests
- **🏗️ Modular Architecture**: Clean, maintainable code structure

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install streamlit matplotlib sympy numpy
   ```

2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

3. **Access the App**: Open your browser to `http://localhost:8501`

## 📚 Available Chapters

### ✅ Ready Now
- **Chapter 1**: Real Numbers (Irrationality proofs, HCF/LCM)
- **Chapter 2**: Polynomials (Factoring, zeroes, construction)
- **Chapter 3**: Linear Equations (4 CBSE solution methods)
- **Chapter 6**: Triangles (Properties, similarity)

### 🚧 Coming Soon
- **Chapter 4**: Quadratic Equations
- **Chapter 5**: Arithmetic Progressions
- **Chapter 7**: Coordinate Geometry
- **Chapter 8**: Trigonometry
- **Chapter 9**: Circles
- **Chapter 10**: Constructions
- **Chapter 11**: Areas Related to Circles
- **Chapter 12**: Surface Areas and Volumes
- **Chapter 13**: Statistics
- **Chapter 14**: Probability

## 🏗️ Project Structure

```
cbse_math_solver/
├── app.py                     # Main Streamlit application
├── config/                    # Configuration files
├── knowledge_base/            # Question bank and search engine
├── chapters/                  # Chapter-wise modules
│   ├── chapter1_real_numbers/
│   ├── chapter2_polynomials/
│   ├── chapter3_linear_equations/
│   └── ...
```

## 🎯 Usage Examples

### Linear Equations
```python
# Example queries:
"Solve x + y = 5 and 2x - y = 1"
"Use substitution method: 2x + 3y = 7 and x - y = 1"
"Find graphical solution of 3x + 2y = 6 and x - y = 2"
```

### Polynomials
```python
# Example queries:
"Factor x^2 + 5x + 6"
"Relationship between zeroes and coefficients of x^2 - 3x + 2"
"Construct quadratic with roots 2 and 3"
```

### Real Numbers
```python
# Example queries:
"Prove root 2 is irrational"
"Find HCF and LCM of 24 and 36"
"Apply Euclid's division algorithm to 867 and 255"
```

## 🔧 Development

### Adding New Chapters
1. Create chapter directory structure
2. Implement chapter-specific solvers
3. Add configuration files
4. Update main router

### Knowledge Base Integration
Each chapter includes:
- MCQ questions with explanations
- Short answer questions with step-by-step solutions
- Long answer questions with detailed solutions
- Practice tests with automatic grading

## 📊 Architecture Benefits

- **🧩 Modular Design**: Each chapter is completely independent
- **📈 Scalable**: Easy to add new chapters and features
- **🔍 Debuggable**: Small, focused modules for easy troubleshooting
- **📚 Educational**: Structure matches CBSE textbook organization
- **🔄 Maintainable**: Clean separation of concerns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests and documentation
5. Submit a pull request

## 📜 License

This project is created for educational purposes and follows CBSE curriculum guidelines.

## 🎯 Roadmap

- [ ] Complete all 14 CBSE chapters
- [ ] Advanced knowledge base search
- [ ] Progress tracking and analytics
- [ ] Mobile-responsive design
- [ ] Offline functionality
- [ ] Multi-language support

## 📧 Support

For questions and support, please open an issue in the repository.

---

**Happy Learning! 🎓✨**
