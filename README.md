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
- config: Adding class HttpRequest to Http_types
- feat: Implementing View for tag creator with Http Types

**__init__.py**:
```
This file is responsible for allow imports inside the folders. All folders that needs imports in their functions must have one of this file. Even if the folders were in cascating, each folder must have a file __init__.py .
```
**Code refactoring**
```
As responsabilidades principais da aplicação foram melhor distribuidas, ou melhor organizadas. Por exemplo, a pasta main concentrou a responsabilidade pelo framework, de modo que qualquer alteração que se queira realizar no framework é lá, e apenas lá, que terei que fazer alterções. Além disso, essas mudanças visam tornar a aplicação mais escalável.
```
**Blueprints**
```
As Blueprints facilitam na rápida identificação do papel de cada rota da aplicação, contruibuindo também para a melhor organização e legebilidade do código. É uma bibioteca muito útil dentro do framework Flask.
```
**Controller folder**
```
É o lugar onde se localiza nossa regra de negócio.
```
</details>

<details>

<summary>⏰Day-3</summary>

</details>