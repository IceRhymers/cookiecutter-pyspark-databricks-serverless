import os
import shutil

def remove_docs_dir():
    """Remove the docs directory if include_docs is set to 'no'."""
    if "{{ cookiecutter.include_docs }}" == "no":
        docs_dir = os.path.join(os.getcwd(), "docs")
        if os.path.exists(docs_dir):
            shutil.rmtree(docs_dir)

if __name__ == "__main__":
    remove_docs_dir() 