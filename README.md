# Git Tutorial

Welcome to the Git Tutorial! This repository is designed to teach you the fundamental Git commands through hands-on practice with simple Python files.

## Prerequisites

- Git installed on your computer
- Basic command line knowledge
- A GitHub account (for remote operations)

## Tutorial Structure

This tutorial covers the following Git concepts in order:
1. `git clone` - Copying a repository
2. `git commit` - Saving changes
3. `git add` - Staging changes
4. `git branch` - Creating branches
5. `git checkout` - Switching branches
6. `git merge` - Combining branches
7. `git fetch` - Getting remote changes
8. `git pull` - Fetching and merging

---

## 1. Git Clone

**Concept**: Cloning creates a local copy of a remote repository on your computer.

**Exercise**:
```bash
# Clone this repository (if you haven't already)
git clone https://github.com/project-emory/git-tutorial.git
cd git-tutorial

# Verify the clone
ls -la
git status
```

**What you should see**: The repository files including `hello_world.py` and `greetings.py`.

---

## 2. Git Commit

**Concept**: A commit is a snapshot of your changes. It records what changed, who changed it, and when.

**Exercise**:
```bash
# First, let's view the current status
git status

# Run the hello world program
python3 hello_world.py

# Now modify hello_world.py to add your name
# Open hello_world.py in your favorite editor and change the message
# For example, change "Hello, World!" to "Hello, World! My name is [Your Name]"

# Stage the changes (we'll learn more about this in the next section)
git add hello_world.py

# Commit the changes with a descriptive message
git commit -m "Add personal greeting to hello_world.py"

# View your commit
git log --oneline
```

**Key Points**:
- Commits require a message describing what changed
- Use clear, descriptive commit messages
- Each commit has a unique hash/ID

---

## 3. Git Add

**Concept**: Before committing, you must "stage" changes using `git add`. The staging area lets you prepare exactly which changes to include in your next commit.

### Tracked vs Untracked Files

**Exercise Part A - Untracked Files**:
```bash
# Create a new file (this will be untracked)
echo 'print("This is a new file!")' > new_file.py

# Check the status
git status
# You'll see new_file.py listed as "Untracked"

# Add the untracked file to staging
git add new_file.py

# Check status again
git status
# Now it's listed as "Changes to be committed"

# Commit it
git commit -m "Add new_file.py"
```

**Exercise Part B - Tracked Files**:
```bash
# Modify an existing tracked file
echo 'print("Extra line!")' >> greetings.py

# Check status
git status
# You'll see greetings.py listed as "modified"

# Add specific file to staging
git add greetings.py

# Check what's staged
git status
```

**Exercise Part C - Adding Multiple Files**:
```bash
# Modify multiple files
echo '# Practice file 1' > practice1.py
echo '# Practice file 2' > practice2.py

# Add all new/modified files at once
git add .

# Or add specific files
git add practice1.py practice2.py

# Commit everything
git commit -m "Add practice files"
```

**Key Points**:
- Untracked files: New files Git doesn't know about yet
- Tracked files: Files already in Git's history
- Staging area: A holding area for changes before committing
- `git add .` stages all changes in the current directory
- `git add <filename>` stages specific files

---

## 4. Git Branch

**Concept**: Branches let you work on different versions of your code simultaneously. They're perfect for developing new features without affecting the main code.

**Exercise**:
```bash
# View current branches
git branch

# Create a new branch called "feature-greeting"
git branch feature-greeting

# View branches again (current branch is marked with *)
git branch

# Check current branch status
git status
```

**What to do**: Now let's make some changes on the main branch that we'll later move to our new branch:
```bash
# Make sure you're on main branch
git branch

# Modify hello_world.py
# Add a new function or change the greeting message

# Stage and commit the changes
git add hello_world.py
git commit -m "Update greeting message"
```

**Key Points**:
- `git branch` lists all branches
- `git branch <name>` creates a new branch
- Creating a branch doesn't switch to it automatically
- The `*` indicates your current branch

---

## 5. Git Checkout

**Concept**: Checkout switches your working directory to a different branch or commit.

**Exercise**:
```bash
# Switch to the feature-greeting branch
git checkout feature-greeting

# Verify you're on the new branch
git branch

# Check the files - notice they might differ from main
git log --oneline

# Make changes on this branch
echo '
def advanced_greeting(name, language="en"):
    greetings = {
        "en": f"Hello, {name}!",
        "es": f"¡Hola, {name}!",
        "fr": f"Bonjour, {name}!"
    }
    return greetings.get(language, greetings["en"])
' >> greetings.py

# Stage and commit on this branch
git add greetings.py
git commit -m "Add multi-language greeting support"

# Switch back to main
git checkout main

# Look at greetings.py - your changes are not here!
cat greetings.py
```

**Alternative Modern Syntax**:
```bash
# Git 2.23+ introduced 'switch' as a clearer alternative to checkout
git switch feature-greeting
git switch main
```

**Key Points**:
- Checkout changes your working directory to match a branch
- Changes on one branch don't affect others
- Always commit or stash changes before switching branches

---

## 6. Git Merge

**Concept**: Merging combines changes from different branches into one branch.

**Exercise**:
```bash
# Make sure you're on main branch
git checkout main

# View the differences between branches
git log --oneline main..feature-greeting

# Merge feature-greeting into main
git merge feature-greeting

# Check the log to see the merge
git log --oneline

# Verify the changes are now in main
cat greetings.py
```

**Exercise - Practice with Another Branch**:
```bash
# Create and switch to a new branch in one command
git checkout -b feature-farewell

# Modify greetings.py to add a new feature
# Add a function or improve existing ones

# Commit your changes
git add greetings.py
git commit -m "Enhance farewell function"

# Switch back to main and merge
git checkout main
git merge feature-farewell
```

**Key Points**:
- Merging combines the history of two branches
- Always merge INTO the branch you're currently on
- Merge conflicts can occur if both branches modified the same lines

---

## 7. Git Fetch

**Concept**: Fetch downloads changes from a remote repository but doesn't automatically merge them into your work.

**Exercise**:
```bash
# View your remote repositories
git remote -v

# Fetch changes from the remote (origin)
git fetch origin

# See what branches exist on the remote
git branch -r

# Compare your local main with remote main
git log main..origin/main

# View what fetch downloaded without merging
git log --oneline origin/main
```

**Simulating Remote Changes** (if working in a team):
```bash
# After a teammate pushes changes:
git fetch origin

# See the new commits without merging
git log HEAD..origin/main

# Inspect the changes
git diff main origin/main
```

**Key Points**:
- Fetch is "safe" - it only downloads data
- Remote branches are prefixed with `origin/` (or your remote name)
- Use fetch to see what changed before integrating changes

---

## 8. Git Pull

**Concept**: Pull combines `git fetch` and `git merge` in one command. It downloads and immediately merges remote changes.

**Exercise**:
```bash
# Pull changes from the remote main branch
git pull origin main

# This is equivalent to:
# git fetch origin
# git merge origin/main
```

**Recommended Workflow**:
```bash
# Start your work session
git pull origin main

# Make your changes
echo '# My changes' >> hello_world.py

# Stage and commit
git add hello_world.py
git commit -m "My changes"

# Pull again before pushing (in case others pushed changes)
git pull origin main

# Push your changes
git push origin main
```

**Key Points**:
- Pull = Fetch + Merge
- Always pull before pushing to avoid conflicts
- If you have uncommitted changes, Git may prevent pulling

---

## Summary of Commands

| Command | Purpose |
|---------|---------|
| `git clone <url>` | Copy a remote repository to your computer |
| `git status` | Check the state of your working directory |
| `git add <file>` | Stage changes for commit |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Save staged changes with a message |
| `git branch` | List branches |
| `git branch <name>` | Create a new branch |
| `git checkout <branch>` | Switch to a branch |
| `git checkout -b <name>` | Create and switch to a new branch |
| `git merge <branch>` | Merge another branch into current branch |
| `git fetch origin` | Download changes from remote |
| `git pull origin <branch>` | Fetch and merge remote changes |
| `git push origin <branch>` | Upload your commits to remote |
| `git log` | View commit history |
| `git log --oneline` | View compact commit history |

---

## Practice Workflow

Here's a complete workflow to practice all concepts:

```bash
# 1. Clone (if starting fresh)
git clone https://github.com/project-emory/git-tutorial.git
cd git-tutorial

# 2. Create a feature branch
git checkout -b my-feature

# 3. Make changes
echo 'print("My feature")' > my_feature.py

# 4. Stage changes
git add my_feature.py

# 5. Commit changes
git commit -m "Add my feature"

# 6. Switch back to main
git checkout main

# 7. Fetch remote changes
git fetch origin

# 8. Pull to update local main
git pull origin main

# 9. Merge your feature
git merge my-feature

# 10. Push your changes
git push origin main
```

---

## Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Git Guides](https://github.com/git-guides)
- [Visualizing Git](https://git-school.github.io/visualizing-git/)

---

## Files in This Repository

- `hello_world.py` - Simple hello world program for basic modifications
- `greetings.py` - Greeting functions for practicing more complex changes
- `README.md` - This tutorial guide

Happy learning! 🚀
