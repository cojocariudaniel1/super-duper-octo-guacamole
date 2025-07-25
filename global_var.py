base_dir = "D:\GithubReositories\GitHub\super-duper-octo-guacamole"

import os
user_id = None
def get_absolute_file_path(relative_path):
    """
    Obține calea absolută pentru un fișier, pornind de la directorul rădăcină al aplicației.

    Args:
    - relative_path (str): Calea relativă către fișier (ex: 'frontend/assets/UserInterface/test.ui').

    Returns:
    - str: Calea absolută către fișier.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_parts = relative_path.split(os.sep)  # Împarte calea relativă într-o listă de părți
    file_path = os.path.join(base_dir, *file_parts)

    return file_path
