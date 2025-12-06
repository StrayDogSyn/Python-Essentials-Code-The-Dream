# Contributing to Code the Dream - Python Essentials

🎉 **Thank you for your interest in contributing!** We're excited to collaborate with educators, developers, and students to make this curriculum even better.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guides](#style-guides)
- [Review Process](#review-process)
- [Community](#community)

---

## 🤝 Code of Conduct

This project follows the **Code the Dream** values of inclusivity, respect, and collaboration. By participating, you agree to:

- **Be Respectful**: Value diverse perspectives and experiences
- **Be Inclusive**: Welcome newcomers and support all skill levels
- **Be Constructive**: Provide helpful feedback and accept it graciously
- **Be Professional**: Maintain a harassment-free, welcoming environment

**Unacceptable behavior** includes harassment, discriminatory language, trolling, or any conduct that creates an unsafe learning environment.

---

## 🌟 How Can I Contribute?

### **1. Report Bugs or Issues**
Found a typo, broken link, or code error?

- Check [existing issues](https://github.com/StrayDogSyn/CTD/issues) first
- Open a new issue with:
  - Clear, descriptive title
  - Steps to reproduce (for bugs)
  - Expected vs. actual behavior
  - Screenshots if applicable
  - Your environment (OS, Python version, browser)

### **2. Suggest Enhancements**
Have ideas for new features or improvements?

- Open an issue with the **enhancement** label
- Describe the feature and its benefits
- Explain how it aligns with learning objectives
- Provide examples or mockups if possible

### **3. Improve Documentation**
Help make the curriculum more accessible:

- Fix typos or grammatical errors
- Clarify confusing explanations
- Add missing setup instructions
- Translate content to other languages
- Improve code comments

### **4. Add Code Examples**
Enhance learning with real-world examples:

- Add practical use cases
- Create visual demonstrations
- Provide alternative solutions
- Include common pitfalls and solutions

### **5. Create Practice Exercises**
Help students solidify their skills:

- Design coding challenges
- Write automated test cases
- Create project templates
- Develop group activities

### **6. Review Pull Requests**
Share your expertise:

- Test proposed changes
- Provide constructive feedback
- Verify educational accuracy
- Check code quality

---

## 🚀 Getting Started

### **1. Fork and Clone**

```bash
# Fork the repository on GitHub (click "Fork" button)

# Clone your fork
git clone https://github.com/YOUR_USERNAME/CTD.git
cd CTD

# Add upstream remote
git remote add upstream https://github.com/StrayDogSyn/CTD.git
```

### **2. Set Up Development Environment**

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r python-essentials-v2/requirements.txt

# Install development dependencies
pip install pytest black flake8 jupyter
```

### **3. Create a Branch**

```bash
# Update your main branch
git checkout main
git pull upstream main

# Create feature branch (use descriptive name)
git checkout -b feature/add-week5-matplotlib-examples
# or
git checkout -b fix/week2-csv-reading-typo
# or
git checkout -b docs/improve-installation-guide
```

---

## 🔄 Development Workflow

### **1. Make Your Changes**

**For Code Examples:**
- Test all code snippets before committing
- Follow PEP 8 style guidelines
- Add comments explaining complex logic
- Include docstrings for functions/classes

**For Jupyter Notebooks:**
- Clear all output before committing: `Cell → All Output → Clear`
- Test notebooks end-to-end
- Use meaningful cell headers
- Include markdown explanations

**For HTML Lessons:**
- Maintain consistent styling with existing lessons
- Test responsiveness on mobile/tablet/desktop
- Ensure accessibility (semantic HTML, alt text)
- Validate HTML syntax

**For Markdown Documentation:**
- Use proper heading hierarchy
- Include code blocks with language tags
- Add links to related resources
- Keep paragraphs concise and scannable

### **2. Test Your Changes**

```bash
# Validate Python code
flake8 your_file.py
black --check your_file.py

# Run tests
pytest python-essentials-v2/tests/

# Validate notebooks (if applicable)
python validate_notebooks.py

# Test HTML lessons in browser
# Open lesson-plans/*.html files and verify functionality
```

### **3. Commit Your Changes**

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add matplotlib scatter plot examples to Week 5

- Created 3 progressive examples (basic, styled, interactive)
- Added explanatory comments for each customization
- Included common pitfalls section
- Updated cheat sheet with plotting tips"
```

**Commit Message Guidelines:**
- Use imperative mood ("Add" not "Added")
- First line: brief summary (50 chars max)
- Blank line
- Detailed description (wrap at 72 chars)
- Reference issues: "Fixes #42" or "Closes #17"

### **4. Push and Create Pull Request**

```bash
# Push to your fork
git push origin feature/add-week5-matplotlib-examples

# Go to GitHub and click "New Pull Request"
```

---

## 📏 Contribution Guidelines

### **General Principles**

✅ **DO:**
- Focus on educational value
- Provide progressive examples (bad → good → best)
- Include both theory and practice
- Test all code thoroughly
- Use inclusive language
- Credit sources and inspirations
- Keep changes focused and atomic

❌ **DON'T:**
- Submit untested code
- Copy content without attribution
- Mix multiple unrelated changes
- Include personal credentials or API keys
- Use offensive or exclusionary language
- Submit AI-generated content without review

### **Content Quality Standards**

**Code Examples:**
- Must be executable and tested
- Include comments explaining key concepts
- Show both correct and incorrect approaches
- Demonstrate real-world applications

**Explanations:**
- Use clear, beginner-friendly language
- Define technical terms on first use
- Include analogies or visual aids
- Provide "why" not just "how"

**Exercises:**
- Align with lesson learning objectives
- Start simple, increase complexity
- Include hints and partial solutions
- Provide automated tests when possible

---

## 🎨 Style Guides

### **Python Code Style**

Follow [PEP 8](https://pep8.org/) with these additions:

```python
# Use descriptive variable names
# ✅ Good
student_scores = [85, 92, 78, 95]
average_score = sum(student_scores) / len(student_scores)

# ❌ Bad
s = [85, 92, 78, 95]
a = sum(s) / len(s)

# Add docstrings for functions
def calculate_grade(score):
    """
    Convert numeric score to letter grade.
    
    Args:
        score (int): Numeric score between 0-100
        
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return 'A'
    # ... rest of implementation

# Use type hints for clarity (optional but recommended)
def process_student_data(name: str, scores: list[int]) -> dict:
    """Process student performance data."""
    return {
        'name': name,
        'average': sum(scores) / len(scores)
    }
```

**Formatting:**
- Indent: 4 spaces (no tabs)
- Line length: 79 characters (code), 72 (comments)
- Blank lines: 2 before top-level functions, 1 between methods
- Imports: standard library → third-party → local

### **Markdown Style**

```markdown
# Main Heading (H1) - One per document

## Section Heading (H2)

### Subsection Heading (H3)

Regular paragraph text with proper spacing.

**Bold for emphasis** and *italics for terms*.

- Unordered list item
- Another item
  - Nested item (2 spaces)

1. Ordered list item
2. Second item

`inline code` for short snippets

\`\`\`python
# Code block with language tag
def example():
    return "Hello, World!"
\`\`\`

> Blockquote for important notes or warnings
```

### **HTML Lesson Style**

Maintain consistency with existing lessons:

```html
<!-- Use semantic HTML5 elements -->
<section id="topic-name" class="section">
    <h2>📚 Topic Title</h2>
    
    <p>Clear explanation with <strong>emphasis</strong> on key points.</p>
    
    <!-- Code container with proper classes -->
    <div class="code-container">
        <div class="code-header">
            <span class="code-label">Python</span>
            <span class="level-badge best">✓ BEST PRACTICE</span>
        </div>
        <pre><code><span class="keyword">def</span> <span class="function">example</span>():
    <span class="comment"># Well-commented code</span>
    <span class="keyword">return</span> <span class="string">"result"</span>
</code></pre>
    </div>
    
    <!-- Explanation boxes for tips/warnings -->
    <div class="explanation-box tip">
        <div class="explanation-title">💡 Pro Tip</div>
        <p>Helpful insight or best practice.</p>
    </div>
</section>
```

### **Commit Message Style**

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature or content
- `fix`: Bug fix or correction
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat: Add regex tutorial to Week 3

- Created progressive examples from basic to advanced
- Included common use cases (email, phone, dates)
- Added interactive regex tester suggestion
- Updated cheat sheet with regex quick reference

Closes #23
```

---

## 🔍 Review Process

### **What to Expect**

1. **Automated Checks** (~2 minutes)
   - Code style validation (flake8)
   - Test suite execution (pytest)
   - Notebook validation

2. **Maintainer Review** (1-3 days)
   - Educational accuracy
   - Code quality
   - Alignment with learning objectives
   - Clarity and accessibility

3. **Feedback Cycle**
   - Reviewers may request changes
   - Discussion in PR comments
   - You update your branch
   - Re-review when ready

4. **Merge**
   - Once approved, maintainer merges
   - Your contribution is live!
   - You're added to contributors list

### **For Reviewers**

When reviewing PRs:

✅ **Check:**
- All code examples work correctly
- Explanations are clear and accurate
- Changes align with educational goals
- Style guidelines are followed
- Tests pass and coverage is maintained

💬 **Provide:**
- Specific, actionable feedback
- Praise for good work
- Suggestions, not demands
- Educational reasoning for requests

---

## 🌐 Community

### **Communication Channels**

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Q&A, ideas, announcements
- **Pull Requests**: Code review and collaboration

### **Getting Help**

- 📖 Read the [README.md](README.md) first
- 🔍 Search existing issues/discussions
- 💬 Ask questions in GitHub Discussions
- 📧 Contact maintainers for sensitive issues

### **Recognition**

Contributors are recognized in:
- GitHub contributors graph
- Release notes
- Special acknowledgments section (for significant contributions)

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make this curriculum better for students worldwide. Whether you fix a typo, add an example, or create an entire lesson, **your work matters**.

**Special thanks to all our contributors:**

[![Contributors](https://contrib.rocks/image?repo=StrayDogSyn/CTD)](https://github.com/StrayDogSyn/CTD/graphs/contributors)

---

<div align="center">

**Questions?** Open an issue or discussion—we're here to help! 🚀

[Back to README](README.md) • [View Issues](https://github.com/StrayDogSyn/CTD/issues) • [Start Contributing](https://github.com/StrayDogSyn/CTD/pulls)

</div>
