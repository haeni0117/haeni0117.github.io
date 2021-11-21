---
title: "[unity] static bool 이랑 static으로 지정해주지 않는 bool의 차이점"
categories:
  - unity
tags:
last_modified_at: 2021-11-20T09:06:00-05:00
---
~~내가 쓸데없는 고민을 하고 있는 줄 알았는데, 역시 인간들은 다 비슷하게 생각한다는 걸 항상 느낀다 ㅋㅋㅋㅋㅋㅋ~~
### [Don't understand static boolean behavior](https://stackoverflow.com/questions/7475553/dont-understand-static-boolean-behavior/7475584)
- ~~예.. 저도 그렇게 생각합니다...~~
- 링크는 stackoverflow에 올라온 질문이다. 본문을 보고 싶으면 제목 클릭 ㄱㄱ
- ![image](https://user-images.githubusercontent.com/69496570/142762088-c38211ef-4321-420d-900b-160c563ff51b.png)
- ![image](https://user-images.githubusercontent.com/69496570/142762122-5b927fde-9678-45e2-baf8-2766990a19e3.png)
- `static` : "local"의 의미를 가진다. ( ↔ '전역'변수 : global variable) : static in this context means "local" (to the translation unit). 
-  로컬 변수라고 하면, 각 로컬마다 다른 값을 가질 수 있다는 거 아닌가..? 내가 static을 잘못 이해하고 있었나?
-  There will be multiple copies of `read_mess` in your program, <u>one per translation unit which is not the same thing as a header file.</u>
-  In your case you can most likely approximate <span style="color:blue">"translation unit"</span> as `.cpp` or `.c` or `.cc` file ~~뭔소리야...~~
-  what you meant to do was <u>to declare an extern variable, or static class member and define it in just one translation unit.</u> ~~ㅇㅇ 나도 그거 하고 싶~~

## Translation Unit?
- In C and C++ programming language terminology
- A translation unit (or more casually a compilation unit) is the ultimate input to a C or C++ compiler from which an object file is generated.
- A translation unit roughly consists of a source file after it has been processed by the C preprocessor 
  - Header files listed in #include directives are literally included, sections of code within #ifndef may be included, and macros have been expanded.

### Reference
- [Translation unit (programming)](https://en.wikipedia.org/wiki/Translation_unit_(programming))
