# GitHub Repository Setup Guide
## BayesRisk Project

This guide walks you through setting up your BayesRisk project on GitHub.

---

## Prerequisites

Before you begin, ensure you have:
- [ ] Git installed on your computer
- [ ] A GitHub account (free at [github.com](https://github.com))
- [ ] Python 3.10+ installed

---

## Step 1: Run the Setup Script

First, create your project structure locally:

```bash
# Navigate to where you want your project
cd ~/projects  # or wherever you keep your code

# Run the setup script
python setup_bayesrisk_project.py --path ./bayesrisk

# Navigate into the project
cd bayesrisk
```

You should see output confirming all directories and files were created.

---

## Step 2: Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Step 3: Initialize Git Repository Locally

```bash
# Initialize git
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial project structure for BayesRisk"
```

---

## Step 4: Create GitHub Repository

### Option A: Using GitHub Web Interface (Recommended for Beginners)

1. **Go to GitHub**
   - Open [github.com](https://github.com) and log in

2. **Create New Repository**
   - Click the **+** icon in the top right corner
   - Select **"New repository"**

3. **Configure Repository**
   - **Repository name:** `bayesrisk`
   - **Description:** `Explainable Credit Default Prediction with Uncertainty Quantification`
   - **Visibility:** Choose `Public` (recommended for portfolio) or `Private`
   - **⚠️ IMPORTANT:** Do NOT check any of these boxes:
     - ❌ Add a README file
     - ❌ Add .gitignore
     - ❌ Choose a license
   
   (We already have these files from the setup script!)

4. **Click "Create repository"**

5. **Connect Local to Remote**
   
   GitHub will show you commands. Copy and run these in your terminal:

   ```bash
   # Replace YOUR_USERNAME with your actual GitHub username
   git remote add origin https://github.com/YOUR_USERNAME/bayesrisk.git
   git branch -M main
   git push -u origin main
   ```

### Option B: Using GitHub CLI (gh)

If you have GitHub CLI installed:

```bash
# Create repo and push in one command
gh repo create bayesrisk --public --source=. --remote=origin --push
```

---

## Step 5: Verify Your Repository

1. Refresh your GitHub page
2. You should see your project structure:
   ```
   bayesrisk/
   ├── src/
   ├── data/
   ├── notebooks/
   ├── tests/
   ├── README.md
   ├── requirements.txt
   └── ...
   ```

---

## Step 6: Configure Repository Settings (Optional but Recommended)

### Add Topics/Tags

1. On your repository page, click the ⚙️ gear icon next to "About"
2. Add relevant topics:
   - `machine-learning`
   - `credit-risk`
   - `bayesian-inference`
   - `explainable-ai`
   - `python`
   - `from-scratch`

### Set Up Branch Protection (Optional)

For professional practice:
1. Go to **Settings** → **Branches**
2. Add rule for `main` branch
3. Enable "Require pull request reviews before merging"

---

## Step 7: Update Personal Information

Before pushing more code, update these files with your actual information:

### In `setup_bayesrisk_project.py`:
```python
# Line 27-29
GITHUB_USERNAME = "your-actual-username"  # Change this!
```

### In `README.md`:
- Update the GitHub badge URLs
- Add your LinkedIn profile
- Update any placeholder links

### In `pyproject.toml` and `setup.py`:
- Verify email is correct
- Update repository URL

Then commit these changes:
```bash
git add .
git commit -m "Update personal information"
git push
```

---

## Step 8: Set Up SSH Keys (Recommended)

To avoid entering your password every push:

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Start ssh-agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub
```

Then:
1. Go to GitHub → **Settings** → **SSH and GPG keys**
2. Click **"New SSH key"**
3. Paste your public key
4. Update remote to use SSH:

```bash
git remote set-url origin git@github.com:YOUR_USERNAME/bayesrisk.git
```

---

## Daily Workflow

### Starting Your Work Day

```bash
cd ~/projects/bayesrisk
source venv/bin/activate  # Activate virtual environment
git pull                  # Get any updates
```

### Making Changes

```bash
# After making changes to files
git add .
git commit -m "Week 1: Implement data loader"
git push
```

### Commit Message Convention

Use descriptive commit messages:

```bash
# Format: [Phase/Week]: Brief description

git commit -m "Week 1: Add data loading utilities"
git commit -m "Week 2: Implement mean imputation from scratch"
git commit -m "Week 6: Add Welch's t-test (addresses BSc gap)"
git commit -m "Fix: Correct variance calculation bug"
git commit -m "Docs: Update research log for Week 3"
```

---

## Updating Research Log

Every Friday, update your research log:

```bash
# Edit the research log
nano research_log.md  # or use your preferred editor

# Commit your progress
git add research_log.md
git commit -m "Week X: Update research log"
git push
```

---

## Troubleshooting

### "Permission denied" when pushing

```bash
# Check your remote URL
git remote -v

# If using HTTPS, try:
git remote set-url origin https://YOUR_USERNAME@github.com/YOUR_USERNAME/bayesrisk.git

# Or switch to SSH (recommended)
```

### "Repository not found"

- Verify the repository exists on GitHub
- Check spelling of username and repo name
- Ensure you have access to the repository

### "Updates were rejected"

```bash
# Pull remote changes first
git pull --rebase origin main
git push
```

---

## Project Milestones to Commit

Here's a suggested commit schedule aligned with your roadmap:

| Week | Suggested Commits |
|------|------------------|
| 1 | `Initial setup`, `Data loader implementation` |
| 2 | `Missing value analysis`, `Imputation from scratch` |
| 3 | `OneHot encoder`, `Target encoder` |
| 4 | `Descriptive statistics engine` |
| 5 | `Pearson correlation`, `VIF calculator` |
| 6 | `Welch's t-test`, `Chi-squared test` |
| 7 | `IQR outlier detection`, `Mahalanobis distance` |
| 8 | `StandardScaler`, `Box-Cox transform` |
| 9 | `Linear regression (OLS + GD)` |
| 10 | `Logistic regression`, `ROC/AUC` |
| 11 | `Ridge`, `Lasso`, `Cross-validation` |
| 12 | `Phase 1 complete`, `Technical report` |

---

## Making Your Repository Portfolio-Ready

### Add a Project Board

1. Go to **Projects** tab in your repository
2. Create a new project board
3. Add columns: `To Do`, `In Progress`, `Done`
4. Create issues for each week's tasks

### Add Badges to README

After you have some code, add these badges:

```markdown
![Tests](https://github.com/YOUR_USERNAME/bayesrisk/workflows/tests/badge.svg)
![Code Coverage](https://codecov.io/gh/YOUR_USERNAME/bayesrisk/branch/main/graph/badge.svg)
```

### Create Releases

At the end of each phase, create a release:
1. Go to **Releases** → **Create new release**
2. Tag: `v0.1.0-phase1` 
3. Title: "Phase 1: Data Engineering & Statistics Complete"
4. Describe what's included

---

## Quick Reference Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# Create a new branch
git checkout -b feature/week-2-imputation

# Switch branches
git checkout main

# Merge branch
git merge feature/week-2-imputation

# Discard changes to a file
git checkout -- filename.py

# Stash work in progress
git stash
git stash pop
```

---

## Next Steps

1. ✅ Run `setup_bayesrisk_project.py`
2. ✅ Initialize git and push to GitHub
3. ⬜ Download the Lending Club dataset
4. ⬜ Start Week 1 tasks
5. ⬜ Update research log weekly

---

**Good luck with your project, Desmond!** 🚀

Remember: Commit often, push daily, and update your research log weekly. This creates a visible trail of your progress that employers can see.
