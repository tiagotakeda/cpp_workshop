# C++ Basics



### Mission

This guide was developed to help members from Skyrats - Autonomous Drones Team from Escola Politécnica da Universidade de São Paulo - to understand the basic concepts of C++.



**It assumes that the person who is reading this guide already have some basic programming experience in any other language, or even C++ and this can be used as a refreshing material.**

Since it is a routine for the members to be asked to install Linux (Ubuntu 16.04 LTS) when they enter the team, some instructions are given to be inserted on a Linux Terminal.

If that may be an issue, you can easily follow this guide using an IDE (Codeblocks is a good starting IDE).



### Prerequisites

* **Compilers**:

  * GCC (Linux)

  * MinGW (Windows)

    

## Contents

* Basic Programming 
* What is C++?
* Quick Start - Hello World
* Variables
* Operators
* References and Pointers
* Defining Functions
* Hands On - Examples



## Basic Programming
To start programming you first need to understand what is a program

### What is a Program?
A program is a set of instructions that the computer executes.
(To be more precise, a program is a set of instructions loaded in the CPU that the CPU executes to achieve an outcome).
![](https://res.cloudinary.com/practicaldev/image/fetch/s--z5YCFTsZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/vr95ldiwraw9h36ae1ma.png)

### Core Hardware Components to Run a Program
The two major components to execute a program are
i) CPU
ii) Memory (RAM)

CPU (Central Processing Unit) runs a set of instructions.
RAM (Random Access Memory) works as a temporary storage to help the CPU achieve the desired output/outcome.

Why we are discussing these boring hardware stuff before moving on to programming? To make you a better programmer by getting your fundamentals right.



### Now on to Programming, but First ..
a little bit of maths to begin with.

Here is a simple equation
Z = X + Y
Suppose, the value of X is 100 and Y = 200, then
we know Z = 300.

Now here comes the twist of the programming world which shatters down the known world of an aspiring beginner. What if we change the equation to:

Y = X + Y

Believe it or not, this is a valid expression in almost all programming languages.

A programming language is a language which the computer understands. It is just like any other language with its own syntax and constructs. The programmer uses it to make the computer follow his/her instructions.

Now going back to that famous expression:

Z = X + Y (If you know your maths well, then you should know that X, Y, Z etc. are all variables)

Suppose we know X = 100, Y = 200 and we ask the computer to calculate the value of X + Y (which mathematically equates to Z).

Here is how we achieve it:

(I will use the syntax similar to C++ , but the language is not important, the concept is)

Since we have three variables, we need to declare them in our program.
Most good programming languages requires that you declare the variables explicitly.

Therefore we write:

```C++ 
int X;
int Y;
int Z;
```

This is called variable declaration. The ``` int ``` is the type of variable that we will later discuss more.

Since we know X is 100 and Y is 200, we write:

```c++
X = 100;
Y = 200;
```

This is called variable assignment.

We could actually write
```c++
int X = 100 
```
In that case we would call it variable declaration with initiation.

Using this trick, we would be reducing some lines if we write the program like this:
```c++
int X = 100;
int Y = 200;
int Z;
```
Now it is very important to understand what goes on behind the scene, otherwise the mind blowing stuff we will be dealing with later (Y = X + Y) would be hard to make sense of.

The moment we write var X or var Y, a space is allocated in RAM because unlike mathematical variables which exist mainly in our brains, the variables of a program resides in an actual physical location.

Here is a conceptual diagram for better understanding:
![](https://res.cloudinary.com/practicaldev/image/fetch/s--tfL9inZ---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/4w2ejuxzzlngv2xli5lg.png)

X and Y are like rooms in a building (which is our RAM) and they have the capabilities of holding values that we assign to them. We might say Room Number X holds value 100 and Room Number Y holds value 200 because we had assigned the values through the assignment operator '=' to them.

To calculate the value of X + Y, we could simply write X + Y

However, doing this operation (every mathematical operation takes place in the CPU) and not storing the result somewhere would mean the result of this operation will be lost forever. Therefore we need to store the operation result somewhere and luckily we have enough room in our RAM to make provision for Z which will hold the value of the X + Y result.

Therefore, when we write
```c++
Z = X + Y;
```
we are telling the computer to fetch the value of X and Y from RAM, add them in the CPU and then store the result in another space called Z.

![](https://res.cloudinary.com/practicaldev/image/fetch/s--FiZ7M2Qz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/yecpi29n5x6ckkmsqmlc.png)

"CPU instructions" in the above image are nothing but the program we have written which goes like this:
```c++
int X;
int Y;
int Z;

X = 100;
Y = 200;

Z = X + Y;
```
Here Z is assigned a value which is the result of the operation of X + Y

Now on to the expression
Y = X + Y, which should make some sense now.

What we are doing here is, fetch values of X and Y from RAM, add them in CPU and put the value back into Y.

I hope by now you have understood computer programming languages are best read from right to left, almost a bit like Arabic isn't it :)? No, just scaring you a little! It is pretty intuitive. We just have to remember everything on the right side of an assignment operator ( '=' ) is processed first and then the assignment happens.

Again, an image for illustration purpose:

![](https://res.cloudinary.com/practicaldev/image/fetch/s--3jBq-EAx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/2lzb42odthffmf3abx75.png)

To round it off,

* We declare variables - which allocates room for them in memory ( I hope after you read this, you would be a little careful about the memory from here on, after all everything has a price). ex. var X;

* We assign variables - which puts values inside the room. ex. X = 100;

* For performing an operation, we fetch these/refer to these assigned values by simply referring to the variables, mentioning the operation between them. For example,
  X + Y means fetch value of X and fetch value of Y and perform the operation ('+') between these variables;

* We store operation results by simply assigning to a room of our choice (either Z or Y);

If you are observant, you'd see that an expression such as Y = X + Y doesn't need Z, hence we don't need to declare Z. This saves a bit of space in the memory. For basic programming it of-course doesn't matter. However, to be mindful of space and other resources will help you to become a great programmer some day.
Yes, in modern day programming we have a lot of hardware resource, but sometimes we are abusing them by being careless with our approach to programming.

After all set and done, you might be wondering what should we do with Y or Z. How about showing the calculated result to the user of your program? In some languages we do that by invoking an instruction called print. If you write something like print(Z), it will show Z as the output to the end user in a DOS like black screen (console). In case of Javascript we can show the value in a message box with alert(Z). However, displaying an output to the computer/mobile screen is another discussion.

For now, do try to grasp the concepts mentioned here before jumping directly into programming.



## What is C++?

C++ was developed by Bjarne Stroustrup at Bell labs in 1979, as an extension to the C laguage.

It can be used to create high-performance applications and ate the same time it gives programmers a high level of control over system resources and memory.

Why use it?

It is one of the world's most popular programming languages, so used that it's usually found in operating systems, Graphical User Interfaces and embedded systems. It also is an object oriented language, giving a clear structure to programs and allowing code to be reused, lowering development costs.

As C++ is close to C# and Java, it makes it easy for programmers to switch to C++ or vice versa.




## Quick Start - Hello World

Traditionally we almost always start a language by printing "Hello World". So I don't see a problem to do same here. Therefore, the code bellow is from my helloworld.cpp file.



```c++
#include <iostream> // standard library

using namespace std; // accept this for now, I'll explain it later

// a c++ program will always have its 'int main()' function
// functions are any code inside its curly bracktes {'code that will be executed'}

int main() {
  cout << "Hello World!" << endl; // cout is an object that prints the text
    							  // Every statement in C/C++ ends with ';'
    							  // endl is a function to skip to the next line
  return 0;						  // return 0 ends the main function
}

//  there are 2 types of comments, single-line and multi-line comments
/*  single-line comments come after 2 slash, 
	and multi-line comments come between slashs and asterisks */
```



For those who are already used to programming with C, C++ won't be any issue.

If you do not fit in that profile don't worry we will explain every line of code.



In the beginning of the code, the first thing to do is to include the Standard Library "iostream" which is the C's correspondent to "stdio.h".

To include it just type down: 

> #include <iostream>
>
> 
>
> using namespace std;

This will allow you mainly to use the input and output objects ("cin" and cout"). 



The same Hello World program without "using namespace std;" would look like this:

```c++ 
#include <iostream>

int main() {
  std::cout << "Hello World!" << std::endl;
  return 0;
}
```

So in order to not having to type "std::" before each "cout" or any other object, we add "using namespace std;" right after including <iostream>.



**Note 1:** The same code could also be written as:

```c++
#include <iostream> 
int main(){std::cout << "Hello World" << std::endl; return 0;}
```

The compiler ignores white spaces. However, multiple lines make the code better to read.



**Note 2:** instead of using the object "endl;" you can also use "\n" to  insert a new line:

```c++
#include <iostream>
using namespace std;

int main() {
  cout << "I am learning C++ \n";
  return 0;
}
```

Similar syntax is used when you need to add a TAB, in this case you have to type "\t".



**Note 3:** All standard libraries are included between "<>":

```c++
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
```







## Variables

If you are **NOT** used to programming in C language this part is mandatory for better understanding of the whole content. If this is not your case you may skip it. 



Variables are containers for storing data values, in other words, is the memory size that the compiler will allocate to store that type of information that you are manipulating. and it surely depends on the type of variable you are using.



The most common type of variables are:

* int - stores integers (whole numbers), such as 123 or -123

* double - stores floating point numbers, such as 19.99 or -19.99

* char - stores single characters, such as 'a' or 'B', or even '%'

* string - stores text, such as "Hello World"

* bool - stores values with two states: true or false



#### Declaring Variables

To create a variable, you **must** specify the type and assign it a value.



**Syntax**

> type variable = value;



**Example**

```c++
int myVar = 15; // myVar is 15
myVar = 10; // now myVar is 10
cout << myVar; // outputs 10
```



#### Constants

You can add 'const' keyword if you don't want others (or yourself) to override existing values (this will declare the variable as **read-only**).

```c++
const int myVar = 15; // myVar will always be 15
myVar = 10;  // error: assignment of read-only variable 'myVar'
```



**Other Examples**

```c++
int myNum = 5;
double myFloatNum = 5.99;
char myLetter = 'L';
string myText = "Skyrats";
bool myBoolean = true;
```



#### Basic Data Types Sizes

|     TYPE      | STORAGE SIZE (in bytes) |           VALUE RANGE           |
| :-----------: | :---------------------: | :-----------------------------: |
|   short int   |            2            |        -32,768 to 32,767        |
|      int      |            4            |    -2147483648 to 2147483647    |
|   long int    |            4            | -2,147,483,648 to 2,147,483,647 |
| unsigned int  |            4            |         0 to 4294967295         |
|     char      |            1            |     -127 to 127 or 0 to 255     |
| unsigned char |            1            |            0 to 255             |
|     float     |            4            |       1.2E-38 to 3.4E+38        |
|    double     |            8            |      2.3E-308 to 1.7E+308       |
|  long double  |           12            |     3.4E-4932 to 1.1E+4932      |
|    string     |           32            |                -                |
|     bool      |            1            |                -                |





## Operators



### Arithmetic Operators

| Operator |              Description               |
| :------: | :------------------------------------: |
|    +     |        Adds together two values        |
|    -     |    Subtracts one value from another    |
|    *     |         Multiplies two values          |
|    /     |     Divides one value from another     |
|    %     |     Returns the division remainder     |
|    ++    | Increases the value of a variable by 1 |
|    --    | Decreases the value of a variable by 1 |



### Assignment Operators

| Operator |  Same as   |
| :------: | :--------: |
|    +=    | x = x + 3  |
|    -=    | x = x - 3  |
|    *=    | x = x * 3  |
|    /=    | x = x / 3  |
|    %=    | x = x % 3  |
|    &=    | x = x & 3  |
|   \|=    | x = x \| 3 |
|    ^=    | x = x ^ 3  |
|   >>=    | x = x >> 3 |
|   <<=    | x = x << 3 |



### Comparison Operators

| Operator |           Name           |
| :------: | :----------------------: |
|    ==    |         Equal to         |
|    !=    |        Not equal         |
|    >     |       Greater than       |
|    <     |        Less than         |
|    >=    | Greater than or equal to |
|    <=    |  Less than or equal to   |



### Logical Operators

| Operator |    Name     |
| :------: | :---------: |
|    &&    | Logical and |
|   \|\|   | Logical or  |
|    !     | Logical not |





## References and Pointers



### References

A reference variable is a "reference" to an existing variable. Check the code below:

```c++
string food = "Pizza";
string &meal = food;

// now we can use either the variable name 'food' or the
// reference name 'meal' to refer to the 'food' variable

cout << food << "\n";  // Outputs Pizza
cout << meal << "\n";  // Outputs Pizza
```



##### Memory Address

In the example above, the '&' operator was used to create a reference variable. But it can also be used to get the memory address of a variable, which is the location of where the variable is stored on the computer.

Obs: When a variable is created, a memory address is assigned to the variable. And when we assign a value to the variable, it is stored in this memory address.

To access it, use the '&' operator, and the result will represent where the variable is stored:

```c++
string food = "Pizza";

cout << &food; // Outputs 0x6dfed4
```



### Pointers

A pointer is simply a variable that **stores the memory address as its value**.

A pointer variable points to a data type (like int or string) of the same type, and is created with the '*' operator. The address of the variable you are working with is assigned to the pointer:

```c++
string food = "Pizza";  // A food variable of type string
string* ptr = &food;    // A pointer variable, with the name ptr, that stores the address of food

// Output the value of food (Pizza)
cout << food << "\n";

// Output the memory address of food (0x6dfed4)
cout << &food << "\n";

// Output the memory address of food with the pointer (0x6dfed4)
cout << ptr << "\n";

// Output the value of food, using ist pointer (Pizza)
cout << *ptr << "\n";
```







## Defining Functions

The next example is here to show how we can define other functions.



The first thing to define on a function is the type that it will return (int, char, string, float, double, etc), or set "void" if it does not return anything.

If the function has any parameter you have to set it between parenthesis "()" and set each parameter type, for example:



```c++
int sum (int parameter1, int parameter2){
      return parameter1 + parameter2;
}
```



Not every function has to return some value, check the example below:



```c++
#include <iostream>

using namespace std;

void printSum (int a, int b){
    int c = a + b;
    cout << a << " + " << b << " = " << c << endl;
}

int main(){
    int num1 = 2;
    int num2 = 3;
    
    printSum(num1, num2);
    
    return 0;
}
```

The output of this program would look like this

```
2 + 3 = 5
```







## Hands On - Examples



#### Compiling and Running

Usually the C++ files have the ".cpp" extension and to compile it on a Linux terminal is quite simple if you already have the GCC complier installed.



Let's say I want to compile a file and its name is "file.cpp", the command I should put on the Terminal is:

```sh
g++ file.cpp -o executable
```



The "-o" is to indicate what is going to be called the executable program that is generated after the compiling, in this case I named it as "executable", but you can named it as you like.



To run the program just do it as any other script on a Linux Terminal:

```sh
./executable
```





#### Examples

After all this new information, the best thing to do is to make it become something that may be useful for your daily life. Check out the examples below.



**Example 1:**

```c++
#include <iostream> // std Library

using namespace std;

int multiply (int banana, int apple) {
    int result;

    result = banana * apple;
    
    return result;
}

int main() {
    int x = 0, y = 0; 	// initiate the two variables

    cout << "Type x: ";
    cin >> x; 			// reads the first input

    cout << "Type y: ";
    cin >> y;			// reads the second input

    cout << endl;		// skips a line
    cout << x;			// prints only the variable x, 
    					// not skipping the line in the end
    
    cout << " * " << y << " = " << multiply (x, y) << endl;
    
    return 0; 			// convention to finish the main() function
}
```



**Example 2:**

```c++
#include <string>		// string std library
#include <iostream>

using namespace std;

int main() {
    string name;
    
    cout << "Type the name: ";
    cin >> name;

   if(name == "Peter"){
       cout << "It is the same as Peter" << endl;
   }else if(name == "Joe"){
       cout << "It is the same as Joe" << endl;
   }else{
       cout << "It is not the same" << endl;
   }
    
   // the following condition is just to show how for works in C++
    
   for(int i = 0; i < 10; i++){
       cout << " " << i;
   }

    char initial = name[0]; // a string is just an char array
    						// and it can be manipulated as one

    cout << endl;
    cout << initial << endl; // it will print the first name's character
    cout << endl;
    cout << name << endl;

    return 0;
}
```



Go ahead and test out those programs checking their outputs. 

# cpp_workshop
