1. #### "Extern" KeyWord

> ****file1.h (header file)****
> 
> ```c
> #ifndef FILE1_H
> #define FILE1_H
> 
> extern int global_var; // declare global variable
> extern void print_message(); // declare function
> 
> #endif // FILE1_H
> ```
> 
> ****file1.c (source file)****
> 
> ```c
> #include "file1.h"
> 
> int main() {
>     global_var = 20; // access and modify global variable
>     print_message(); // call function
>     return 0;
> }
> ```
> 
> **file2.c (another source file)**
> 
> ```c
> #include "file1.h"
> 
> int main() {
>     global_var = 20; // access and modify global variable
>     print_message(); // call function
>     return 0;
> }
> ```

---

2. #### What is a preprocessor?
   
   > A preprocessor as the same suggests, is a program for preprocessing.
   > 
   > 1. It runs before compilation.
   > 2. **Text substitution**: Replacing macros and symbolic constants with their actual values.
   > 3. **File inclusion**: Inserting the contents of included files (like header files) into the source code.
   > 4. **Conditional compilation**: It selectively includes or excludes portions of code based on preprocessor directives such as `#ifdef`, `#ifndef`, `#if`, `#else`, and `#endif`.
   > 5. Also, It strips out the comments.
   > 6. 

---

3. #### main()
   
   > ```cpp
   > int main(int argc, char* argv[]){ //argc is argument_count, argument_vector
   >     // code
   > return 0;
   > }
   > ```
   > 
   > program argument1 arg2
   
   ---

4. #### Namespaces
   
   > ```cpp
   > std::cout<< "Heyy there!"<< endl;
   > ```
   > 
   > ```c
   > #include <iostream>
   > using std::cout;
   > using std::cin;
   > ```
   > 
   > ```c
   > #include <iostream>
   > using namespace std;
   > 
   > int main(){
   >     cin >> "Hey there! "<< endl;
   > }
   > ```

---

5. #### Variables
   
   > * Global variables are defaulted to zero.

---

6. #### Sizeof()
   
   > * Determines the size of a variable.
   > * sizeof(int) // of type
   > * sizeof(a)

---

7. #### DataTypes
   
   > * char - 1b
   > 
   > * short -2b
   > 
   > * int -4b
   > 
   > * long -4b
   > 
   > * long long - 8b
   > 
   > * --
   >   *Floating point integers:*
   > 
   > * Float -4b
   > 
   > * double -8b
   > 
   > * long double -12b
   >   ---
   >   
   >   **MACROS**
   >   
   >   * SHORT_MIN
   >   
   >   * INT_MIN/ INT32_MIN
   >   
   >   * INT64_MIN
   >   
   >   * LONG_MIN
   >   
   >   * **LLONG_MIN**

---

8. #### Constants
   
   > 1. *Literal Constants:*
   >    
   >    - 1.56
   >    
   >    - 12 - integer
   >    
   >    - 12U - Unsigned integer
   >    
   >    - 12L - a long integer
   >    
   >    - 12LL - a long long integer
   > 
   > 2. *Floating point literal constants:*
   > * 12.1 - a double
   > 
   > * 12.1F - a float
   > 
   > * 1L - a long double

---

9. #### Arrays

---

10. #### Vectors
    
    > * #include<vector>
    > 
    > * vector <int> v (100, 0 ) # (size, initial_val)
    > 
    > * v.at(0) = v[0]
    > 
    > * v.size()
    > 
    > * v.push_back()

---

11. #### Typecasting
    
    > static_cast<double>(100) // modern
    > (double)a // old style

---

12. #### Equals to
    
    > 10 == 10.0 // return True since left one is upcasted to higher dim
    > 
    > *Notes: 10 = 9.999999999999999999999999999999999999* returns true because of internal representation // tryout once

---

13. #### Operator precedence and Associativity
    
    > ![](D:\Codes\Docs\c++%20images\operator%20precedence%20.png)

14. #### Character functions
    
    > ![](C:\Users\zen\AppData\Roaming\marktext\images\2024-05-20-17-42-52-image.png)
