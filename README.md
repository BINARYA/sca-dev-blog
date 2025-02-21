# Blog SCA - Dev Blog

This is the repository for the blog developed with [Pelican](https://blog.getpelican.com/), a Python-based static site generator.

## 📌 Requirements

To use this blog, make sure you have installed:

- Python 3.8+
- Virtualenv (optional but recommended)
- Pelican and its dependencies

## 🚀 Installation

1. **Clone the repository:**
   ```sh
   git clone <REPOSITORY_URL>
   cd <FOLDER_NAME>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## 📝 Project Structure

The project is organized as follows:

```
.
├── content/         # Folder for posts and pages
├── output/          # Folder generated with the static site
├── theme/           # Custom themes (optional)
├── pelicanconf.py   # Main configuration file
├── publishconf.py   # Configuration for publishing
├── tasks.py         # Automated task management
├── Makefile         # Automates generation and publishing
├── requirements.txt # Project dependencies
└── README.md        # This file
```

## ✍️ Writing a Post

Posts go inside the `content/` folder and are written in **Markdown** or **reStructuredText**.
Example of a post in Markdown:

```md
Title: Post Title
Date: 2025-02-21
Category: Category
Tags: development, SCA
Author: mrJungle
Summary: Short description of the post.

Post content...
```

## 🔧 Useful Commands

**Generate the static site:**
```sh
pelican content
```

**Start a local server for preview:**
```sh
pelican --listen
```

**Clean and regenerate the site:**
```sh
make clean && make html
```

**Publish to a remote server:**
```sh
make publish
```

## 📢 Notes
- Modify `pelicanconf.py` to customize the blog.
- Use `publishconf.py` for production configurations.
- For custom themes, add them inside the `theme/` folder and update `pelicanconf.py`.

## 📜 License
This blog is distributed under the MIT license. Feel free to use and modify it!

---

Happy Blogging! 🚀
