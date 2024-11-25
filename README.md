<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>SHORTYS</h1>
<p align="left">
	<em><code>Shortys is a simple URL shortener built with Python and Flask, leveraging MongoDB for storage. This project allows users to shorten long URLs easily, providing a clean and user-friendly interface.</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/iamjuaness/shortys?style=flat-square&logo=opensourceinitiative&logoColor=white&color=579c62" alt="license">
	<img src="https://img.shields.io/github/last-commit/iamjuaness/shortys?style=flat-square&logo=git&logoColor=white&color=579c62" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/iamjuaness/shortys?style=flat-square&color=579c62" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/iamjuaness/shortys?style=flat-square&color=579c62" alt="repo-language-count">
</p>
<p align="left">Built with the tools and technologies:</p>
<p align="left">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat-square&logo=Flask&logoColor=white" alt="Flask">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat-square&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
</p>
</div>
<br clear="right">

<details><summary>Table of Contents</summary>

- [📍 Overview](#-overview)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🛠️ Configure Database](#-configure-database)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

</details>
<hr>

## 📍 Overview

**URL Shortener** is a web application developed with **Flask** and built in **Python** 
that allows you to shorten long URLs, making them easier to manage and share. This tool converts long URLs into shorter links, 
ideal for social media posts, emails, or anywhere short and easy to remember links are preferred. 

### Key Features 
  - **URL Shortening**: Converts long URLs into short, customizable links.
  - **Simple and Friendly Interface**: The application includes an intuitive.
  - **HTML** interface so that users can shorten and manage links without hassle.
  - **Efficient Storage**: Uses a **MongoDB** database to store and manage shortened URLs.
  - **Redirected Routes**: Allows quick redirection from the shortened URL to the original URL.

### Who is it designed for? 
This project is ideal for developers who need to implement a custom URL shortener, or for small businesses and 
users who want to shorten and manage links for easy sharing. 

### Technologies Used 
  - **Python** and **Flask** for the backend logic. 
  - **HTML** for the user interface.
  - **MongoDB** for URL and data management.
  
---

## 📁 Project Structure

```sh
└── shortys/
    ├── app.py
    ├── requirements.txt
    ├── static
    │   └── style.css
    ├── templates
    │   └── index.html
    ├── vercel.json
    └── wsgi.py
```


### 📂 Project Index
<details open> 
  <summary><b><code>SHORTYS/</code></b></summary> 
  <details> 
    <summary><b>__root__</b></summary> 
    <blockquote> 
      <table> 
        <tr> 
          <td><b><a href='https://github.com/iamjuaness/shortys/blob/master/vercel.json'>vercel.json</a></b></td> 
          <td><code>❯ Configuration for Vercel deployment.</code></td> 
        </tr> 
        <tr> 
          <td><b><a href='https://github.com/iamjuaness/shortys/blob/master/app.py'>app.py</a></b></td> 
          <td><code>❯ Main application file.</code></td> 
        </tr> 
        <tr> 
          <td><b><a href='https://github.com/iamjuaness/shortys/blob/master/requirements.txt'>requirements.txt</a></b></td> 
          <td><code>❯ Python dependencies.</code></td> 
        </tr> 
        <tr> 
          <td><b><a href='https://github.com/iamjuaness/shortys/blob/master/wsgi.py'>wsgi.py</a></b></td> 
          <td><code>❯ WSGI entry point for the application.</code></td> 
        </tr> 
      </table> 
    </blockquote> 
  </details> 
  <details> 
    <summary><b>templates</b></summary> 
    <blockquote> 
      <table> 
        <tr> 
          <td><b><a href='https://github.com/iamjuaness/shortys/blob/master/templates/index.html'>index.html</a></b></td> 
          <td><code>❯ Main HTML template for the application.</code></td> 
        </tr> 
      </table> 
    </blockquote> 
  </details> 
</details>

---

## Live Demo
Check out the live application [here](https://shortys.vercel.app/).
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with shortys, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install shortys using one of the following methods:

**Build from source:**

1. Clone the shortys repository:
```sh
❯ git clone https://github.com/iamjuaness/shortys
```

2. Navigate to the project directory:
```sh
❯ cd shortys
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```
### 🛠️ Configure DataBase
**Get Connection String**.

For the project to work correctly, it is necessary to set up a database in MongoDB. Follow these steps:

- Log in to [MongoDB Atlas](https://www.mongodb.com/atlas/database) and create a **new project**.
- In the project, create a **Cluster**. You can choose the type of cluster that suits your needs.
- Once the cluster is created, go to the **Connection** section and select **Connect your application**.
- Copy the **Connection String**, which should have a format similar to:
  
     ```
     mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
     ```

**Set up the .env file**.

- In the root of the project, create a `.env` file.
- Add the connection string to the `.env` file, replacing `<username>`, `<password>`, and `<dbname>` with the corresponding values:
  
     ```env
     MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
     ```

### 🤖 Usage
Run shortys using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python wsgi.py
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Shorten URL's.</strike>
- [ ] **`Task 2`**: Optimization Database.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/iamjuaness/shortys/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/iamjuaness/shortys/issues)**: Submit bugs found or log feature requests for the `shortys` project.
- **💡 [Submit Pull Requests](https://github.com/iamjuaness/shortys/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/iamjuaness/shortys
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/iamjuaness/shortys/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=iamjuaness/shortys">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](https://github.com/iamjuaness/shortys/blob/master/LICENSE) file.

---

## 🙌 Acknowledgments

This project would not have been possible without the support of the following tools and resources: 
  - **Flask**: Special thanks to the creators and maintainers of Flask, a Python micro-framework that has made web development fast and accessible.
  - **MongoDB**: Thanks to the MongoDB team for providing a flexible and scalable database, perfect for managing and storing URLs.
  - **Flask and MongoDB documentation**: The tutorials and official documentation for both technologies were instrumental in guiding the development of this project.
  - **Stack Overflow and the Developer Community**: We are grateful to the global community of developers and contributors who share their knowledge and provide constant support, making troubleshooting faster and more efficient.
---
