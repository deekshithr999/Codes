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

2. #### What is a preprocessor?
   
   > A preprocessor as the same suggests, is a program for preprocessing.
   > 
   > 1. It runs before compilation.
   > 
   > 2. It does work of macro substitution, File inclusion
   > 
   > 3. **Conditional compilation**: It selectively includes or excludes portions of code based on preprocessor directives such as `#ifdef`, `#ifndef`, `#if`, `#else`, and `#endif`.
