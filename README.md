
# Clean code practices for data scientists

“When I wrote this code, only God and I understood what I did. Now only God knows.”

If you relate to the above quote, I invite you to a bi-weekly series of “Clean code practices for data scientists.” seminars. As data scientists, there are a lot of design topics we can learn from the software development area. We will cover some of these topics in this seminar.

# What is This?
 We will cover a very brief introduction to the topic and then we will work on a small project together. In these seminars, we will cover the topics to write better codes. 

# Target Audience
This seminar is for data scientists who want to improve their coding skills. It is not for beginners. It is for people who already know how to code and want to improve their coding skills. We will not cover the details of the topic. We will just mention the topic and then we will work on a small project together.

It is up to you to learn the details of the topic. I will provide you with the resources that I used to learn the topic.

# Covered Topics

### 1.	Object-oriented Programming: 
<a href="https://colab.research.google.com/github/jadaliha/DS_coding_practices/blob/main/1_OOP_programming_in_python.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
>**Summery:** 
>1. A class is a user-defined blueprint (Interface is used in more advanced
languages)
>2. In Python, classes are **advanced dictionary**
>3. Each class instance can have attributes attached to it for maintaining its **state**.
>4. Class instances can also have **methods** (defined by their class) for modifying their state.
>5. **setter** and **getter** methods can be used to act as a proxy for interacting with internal states of class
>6. **str**, and **repr** method can be used to prettify a print
>7. **Inheritance** helps to breakdown your code to hierarchy design
>8. **dataclass** is an awesome package to define data-oriented classes (vs. behavioral)
>9. you can **freeze** a class to achieve const behavior
>10. with the help of class, you can use **JSON** to store states



### 2. Functional programming and decorators
<a href="https://colab.research.google.com/github/jadaliha/DS_coding_practices/blob/main/2_Functional_programming_and_decorators.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
>**Summery:** 
>1. functional programming paradigm vs. object-oriented
>2. What is a **decorator** and how to use them
>3. Most useful decorators for DS
>4. Used `@singledispatch`,  `@singleton`,`@lru_cache` decorator
>5. introduction to `functools` package
>6. Learned about **closure** and how to use them

### 3. Modules and packages
<a href="https://colab.research.google.com/github/jadaliha/DS_coding_practices/blob/main/3_Modules_and_packages.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
>**Summery:** 
>1. We created a **modules** and imported it
>2. Package file structure is reviewd
>3. To define a package, `setup.py` file is used 
>4. We used `twine` to publish [funsql](https://github.com/jadaliha/funsql) module
>5. We used `pip` to install `funsql` module


### 4. Testing and logging
<a href="https://colab.research.google.com/github/jadaliha/DS_coding_practices/blob/main/4_Testing_loging_debuging.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
> **Summery:**
> 1. [Design by contract](https://en.wikipedia.org/wiki/Design_by_contract) is a programming paradigm that define the interface (inputs and output types) of a component.
> 2. [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) is a development process that relies on the test cases, then the code is improved so that the tests pass. 
> 3. You have to write the test before you write the code. For any new features, you have to write the test first, then write the code to pass the test.
> 4. `assert` is build-in Python statement for writing test units, which is different from `raise` to handle on the fly errors.
> 5. `pytest` and `unittest` modules, has more variation for `assert`.
> 6. You may use `logging` module to record diagnostic information, while running the program. and define the level of severity and destination of the log seperatly for different part of the code, and change them for **production** and **development** without changing the code again.

### 5. Executable python and debugging
<a href="https://colab.research.google.com/github/jadaliha/DS_coding_practices/blob/main/5_executable_python.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

> **Summary:**
> 1. Jupyter Notebooks is a valuable tool but not suitable for production code
> 2. You can use `sys` and `os` modules to pass arguments to the script
> 3. `InquirerPy` is an excelent library to prompt for user input 
> 4. Add `__main__.py` to your module to make itself independent script
> 5. You may use `rich` library, along with `breakpoint()` to debug your code

### 6. Data Manipulation Challenge

>**Challange**
> 1.	We have transactions for an e-commerce website, and we need to identify users' spending decrease (soft attrition problem). 
You can download data from: https://drive.google.com/file/d/1Q_ZU_IN-igiI16GKrz8FGqXgvLQmeEsD/view?usp=share_link.
> 2.	The transaction table has the following columns: userid, transactionid, transactiontime, numberofitemspurchased, costperitem
> 3.	Write your main.py file that gets input and output CSV file path as parameters 
> 4.	Read the transaction table from the input file.
> 5.	Clean up data removing duplicate data and userid = -1
> 6.	Calculate the "aggregated_table" with each month's dollar value of transactions per user. (hint: what happens if a user does not have transactions in month X?)
> 7.	Add a new column, "soft_attrition", to aggregated_table, which is "1" if the total amount of transactions in the next three months is less than 25% of the past three months; otherwise, it is "0".
> 8.	The final output file should have the following columns: userid, month (in string format like 2021-10), soft_attrition

Two solution to this challenge is provided Here: 

[The first one is using `pandas` which is a very popular library for data manipulation and the code is very concise.](./6_exercise/solution_with_pandas.py)

[and the second one is using `polars` module, which is a new library for data manipulation and it is very fast.](./6_exercise/solution_with_polars.py)

<!-- ### 8. What is next? -->



# Conclusion

Even though you may already know these topics, I still think it might be a good idea to review and see some small tricks that help for better coding.