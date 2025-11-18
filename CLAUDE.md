# CLAUDE.md - AI Assistant Guide for psychoApps

## Project Overview

**psychoApps** is a Streamlit-based application project. Streamlit is a Python framework for building interactive data applications and dashboards with minimal code.

### Project Status
- **Current State**: Early initialization phase
- **Primary Technology**: Python + Streamlit
- **Repository Type**: Git-based version control
- **Development Branch**: Feature branches prefixed with `claude/`

## Repository Structure

```
psychoApps/
├── README.md                 # Project description
├── CLAUDE.md                 # This file - AI assistant guidelines
├── requirements.txt          # Python dependencies (to be created)
├── .gitignore               # Git ignore patterns (to be created)
├── app.py                   # Main Streamlit application (to be created)
├── .streamlit/              # Streamlit configuration (to be created)
│   └── config.toml          # Streamlit settings
├── src/                     # Application source code (to be created)
│   ├── __init__.py
│   ├── components/          # Reusable Streamlit components
│   ├── utils/               # Helper functions and utilities
│   └── pages/               # Multi-page app pages
├── tests/                   # Test suite (to be created)
│   ├── __init__.py
│   └── test_*.py            # Test files
├── data/                    # Data files (to be created)
│   ├── raw/                 # Raw data
│   └── processed/           # Processed data
└── assets/                  # Static assets (to be created)
    ├── images/
    └── styles/
```

## Development Workflows

### Setting Up Development Environment

When setting up the project for the first time:

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

### Git Workflow

- **Main Branch**: Usually `main` or `master`
- **Feature Branches**: Use descriptive names prefixed with `claude/`
- **Current Branch**: `claude/claude-md-mi488ncsz30ysjfs-01DEudi6v6EphTy53nzF5r7M`

#### Committing Changes
```bash
# Stage changes
git add <files>

# Commit with descriptive message
git commit -m "Add: [description of feature/fix]"

# Push to feature branch
git push -u origin <branch-name>
```

#### Git Best Practices
- Write clear, descriptive commit messages
- Use conventional commit format: `Add:`, `Fix:`, `Update:`, `Refactor:`
- Commit logical units of work
- Never force push to main/master
- Always push to branches starting with `claude/`

## Python Coding Conventions

### Style Guide
- Follow **PEP 8** Python style guide
- Use **type hints** for function signatures
- Maximum line length: 88 characters (Black formatter default)
- Use **docstrings** for all functions, classes, and modules

### Code Example
```python
from typing import List, Dict, Optional
import streamlit as st


def process_data(
    data: List[Dict[str, any]],
    filter_key: Optional[str] = None
) -> List[Dict[str, any]]:
    """
    Process and filter data based on provided key.

    Args:
        data: List of dictionaries containing data
        filter_key: Optional key to filter data

    Returns:
        Processed and filtered data
    """
    if filter_key:
        return [item for item in data if filter_key in item]
    return data
```

### Code Organization
- One class/major function per file when reasonable
- Group related utilities in modules
- Keep functions small and focused (single responsibility)
- Use descriptive variable and function names

## Streamlit-Specific Guidelines

### Application Structure

#### Single-Page App
```python
import streamlit as st

# Page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="psychoApps",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("psychoApps")
    st.write("Welcome to the application")

    # Your app logic here

if __name__ == "__main__":
    main()
```

#### Multi-Page App
- Create `pages/` directory
- Name files with numbers: `1_page_name.py`, `2_another_page.py`
- Streamlit automatically creates navigation

### State Management
```python
# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Update state
st.session_state.counter += 1

# Access state
st.write(f"Counter: {st.session_state.counter}")
```

### Caching Best Practices
```python
@st.cache_data  # For data transformations
def load_data(file_path: str):
    return pd.read_csv(file_path)

@st.cache_resource  # For resources like DB connections
def get_database_connection():
    return create_connection()
```

### Performance Tips
- Use `st.cache_data` for expensive computations
- Use `st.cache_resource` for singleton resources
- Minimize rerun frequency with careful widget placement
- Use `st.spinner()` or `st.progress()` for long operations

## Dependencies Management

### Core Dependencies (to be added to requirements.txt)
```txt
streamlit>=1.29.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
```

### Development Dependencies
```txt
pytest>=7.4.0
black>=23.0.0
flake8>=6.1.0
mypy>=1.7.0
```

### Adding New Dependencies
1. Add to `requirements.txt`
2. Install: `pip install -r requirements.txt`
3. Update this document if it's a major dependency

## Testing Conventions

### Test Structure
```python
import pytest
from src.utils import process_data


def test_process_data_basic():
    """Test basic data processing"""
    data = [{"key": "value"}]
    result = process_data(data)
    assert len(result) == 1
    assert result[0]["key"] == "value"


def test_process_data_with_filter():
    """Test data processing with filter"""
    data = [{"name": "Alice"}, {"name": "Bob"}]
    result = process_data(data, filter_key="name")
    assert len(result) == 2
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_utils.py
```

## Configuration Management

### Streamlit Configuration (.streamlit/config.toml)
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

### Environment Variables
- Use `.env` file for secrets (add to `.gitignore`)
- Access via `st.secrets` or `os.getenv()`
- Never commit secrets to repository

## Security Best Practices

1. **Secrets Management**
   - Use Streamlit secrets: `.streamlit/secrets.toml`
   - Never hardcode credentials
   - Add secrets.toml to .gitignore

2. **Input Validation**
   - Validate all user inputs
   - Sanitize data before processing
   - Use try-except blocks for error handling

3. **Data Privacy**
   - Don't log sensitive user data
   - Implement proper session management
   - Clear sensitive data from session state when done

## Common Patterns

### File Upload Handler
```python
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
```

### Form Handling
```python
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Hello {name}, you are {age} years old")
```

### Sidebar Navigation
```python
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Analysis", "Settings"])

if page == "Home":
    show_home_page()
elif page == "Analysis":
    show_analysis_page()
elif page == "Settings":
    show_settings_page()
```

## Debugging Tips

### Streamlit Debugging
```python
# Display variable content
st.write(variable_name)

# Display session state
st.write(st.session_state)

# Use st.echo() to display code
with st.echo():
    x = 10
    y = 20
    result = x + y
```

### Common Issues
1. **State not persisting**: Use `st.session_state`
2. **Page rerunning unexpectedly**: Check widget keys and callbacks
3. **Cache not working**: Ensure cached functions are pure
4. **Import errors**: Check virtual environment activation

## AI Assistant Guidelines

### When Working on This Project

1. **Always Read Before Write**
   - Use Read tool to check existing files before editing
   - Understand context before making changes

2. **Prefer Editing Over Creating**
   - Edit existing files rather than creating new ones
   - Only create new files when absolutely necessary

3. **Follow Python Conventions**
   - Use type hints
   - Write docstrings
   - Follow PEP 8
   - Use meaningful variable names

4. **Test Your Changes**
   - Consider test coverage for new features
   - Suggest test cases for critical functionality

5. **Document Changes**
   - Update docstrings when changing functions
   - Add comments for complex logic
   - Update this CLAUDE.md if conventions change

6. **Git Operations**
   - Stage only relevant files
   - Write clear commit messages
   - Push to designated feature branch
   - Never force push without explicit permission

7. **Error Handling**
   - Add try-except blocks for risky operations
   - Provide user-friendly error messages in Streamlit
   - Log errors appropriately

8. **Performance Considerations**
   - Use caching for expensive operations
   - Avoid unnecessary reruns
   - Optimize data loading and processing

### Communication Style
- Be concise and technical
- Provide code references with `file:line` format
- Explain reasoning for architectural decisions
- Ask for clarification when requirements are ambiguous

## Resources

### Streamlit Documentation
- Official Docs: https://docs.streamlit.io
- API Reference: https://docs.streamlit.io/library/api-reference
- Gallery: https://streamlit.io/gallery

### Python Resources
- PEP 8: https://peps.python.org/pep-0008/
- Type Hints: https://docs.python.org/3/library/typing.html
- pytest: https://docs.pytest.org/

## Project-Specific Notes

### Current Development Focus
- Initial application setup and structure
- Core functionality implementation
- User interface design

### Known Limitations
- None yet (project in early stages)

### Future Enhancements
- To be documented as project evolves

---

**Last Updated**: 2025-11-18
**Version**: 1.0.0
**Maintainer**: takishun (shun.takinami@gmail.com)
