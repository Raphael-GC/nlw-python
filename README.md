<h1 align="center">
  <img 
  alt="Python-barcode" 
  title="Python-barcode Logo" 
  src=".github/logo.svg" 
  width="300px"/>
</h1>
 
<h4 align="center">A Python project using Flask for generating barcodes. This project belongs to Rocketseat's event called NLW-Experts.</h4> 

<center>

![Progress](https://progress-bar.dev/33/?title=done) 

</center>

## ⚙️Techs:
- [Virtualenv](https://pypi.org/project/virtualenv/)
- [Pylint](https://pypi.org/project/pylint/)
- [Pre-commit](https://pre-commit.com/)
- [Flask](https://pypi.org/project/Flask/)
- [Python-barcode](https://pypi.org/project/python-barcode/)
- [Pillow](https://pypi.org/project/pillow/)

## 🔗Useful links:
- [Notion](https://efficient-sloth-d85.notion.site/NLW-14-Expert-9e11ff472de64b08a5f9e277a20c3ecc)
- [Event Website](https://www.rocketseat.com.br/eventos/nlw)
- [Wallpapers](https://drive.google.com/drive/folders/1bdX5SIrw6MBBqBkZgryc4H_omPQhuPx-)

## 📋Notes:
<details>

<summary>⏰Day-1</summary>
- Adding Pylint to project <br>
- Adding pre-commit to project <br>
- Adding server base params, including route and feature for generating barcode <br>
- Adding and update the requirements <br>
- Adding README.md and LICENSE <br><br>

---

**Pylint and naming conventions**:
```py
def my_func(): # snake_case -> Functions, Variables, Methods
    print('Ola')

def myFunc(): # camelCase -> It's not the usual default.
    print('Ola2')

class MyFunc: # PascalCase -> Classes

SCREAMING_SNAKE_CASE:  # -> Const

```
----
**Requirements**: <br>
When we want to keep a record of installed dependencies and their versions, we use this command in the terminal.
```sh
 .venv\Scripts\pip3 freeze > requirements.txt
```
</details>

<details>

<summary>⏰Day-2</summary>
- Implementing App in Src <br>
- Adding class HttpRequest to Http_types
- Implementing View for tag creator with Http Types
- Adding class BarcodeHandler to Drivers

**__init__.py**:
```
This file is responsible for allowing imports inside the folders. All folders that need imports in their functions must have one of these files. Even if the folders were cascading, each folder must have a file __init__.py.
```
**Code refactoring**
```
The application's main responsibilities have been better organized and distributed. For instance, the framework's primary folder is now solely responsible for any changes to the framework, making it easier to manage and maintain. Additionally, all components related to the HTTP protocol and business rules logic have been consolidated in specific locations. These changes have been implemented to enhance the application's scalability.
```
**Blueprints**
```
Blueprints simplify the identification of each application route's role and contribute to better code organization and readability, making it a valuable library in the Flask framework.
```
**Controllers folder**
```
Our business rules are located in this place.
```

**Drivers folder e Barcode_handler.py**
```
'Drivers' is the place where we concentrate all external libraries. In our code, 'Barcode_handler.py' acts as a central point for accessing the external libraries. This means that if any other file needs to access an external library, it can only do so through barcode_handler.py. This is a principle of good practice.
```
</details>

<details>

<summary>⏰Day-3</summary>

</details>