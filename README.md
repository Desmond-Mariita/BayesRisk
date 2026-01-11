# BayesRisk

**Explainable Credit Default Prediction with Uncertainty Quantification**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

BayesRisk is a comprehensive credit default prediction system that combines:
- **Bayesian inference** for uncertainty quantification
- **Deep learning** for complex pattern recognition  
- **Explainable AI (XAI)** for regulatory compliance

This project implements all core algorithms **from scratch** using only NumPy, 
demonstrating deep understanding of the underlying mathematics.

## 📁 Project Structure

```
bayesrisk/
├── src/                    # Source code
│   ├── data/              # Data loading and acquisition
│   ├── preprocessing/     # Encoders, scalers, imputers
│   ├── statistics/        # Descriptive stats, hypothesis tests
│   ├── models/            # ML models (from scratch)
│   ├── metrics/           # Evaluation metrics
│   ├── bayesian/          # Bayesian inference (Phase 2)
│   ├── neural/            # Neural networks (Phase 3)
│   ├── explainability/    # XAI methods (Phase 4)
│   └── pipeline/          # End-to-end pipelines
├── data/                   # Data directory
│   ├── raw/               # Original data
│   ├── interim/           # Intermediate data
│   └── processed/         # Final datasets
├── notebooks/              # Jupyter notebooks
├── reports/                # Generated reports
├── tests/                  # Unit and integration tests
└── docs/                   # Documentation
```

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-github-username/bayesrisk.git
cd bayesrisk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

## 📊 Dataset

This project uses the [Lending Club Loan Dataset](https://www.kaggle.com/datasets/wordsforthewise/lending-club) 
containing ~2.2M loans with 150+ features.

## 🛠️ Implementation Phases

| Phase | Period | Focus | Status |
|-------|--------|-------|--------|
| 1 | Feb-Apr | Data Engineering & Statistical Foundations | 🔄 In Progress |
| 2 | May-Jul | Bayesian Statistics Mastery | ⏳ Planned |
| 3 | Aug-Oct | Deep Learning from Scratch | ⏳ Planned |
| 4 | Nov-Dec | XAI Integration | ⏳ Planned |

## 📝 Research Log

See [research_log.md](research_log.md) for weekly progress updates.

## 👤 Author

**Desmond Momanyi Mariita**
- Email: dmariita@keragita.com
- LinkedIn: 
- GitHub: https://github.com/Desmond-Mariita

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Lending Club for the dataset
- University of Potsdam - MSc Cognitive Systems program
