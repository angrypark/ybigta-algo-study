# 1. Mismatched Brackets

#### 문제

Best White is a mathematics graduate student at T1 University. Recently, he finished writing a paper and he decided to polish it. As he started to read it from the beginning, he realized that some of the formulas have problems: some of the brackets are mismatched! Since there are so many formulas in his paper, he decided to check their validity with a computer program.

The following kinds of brackets are included in Best White’s paper.

- Round brackets are opened by a `(` and closed by a `)`.
- Curly brackets are opened by a `{` and closed by a `}`.
- Square brackets are opened by a `[` and closed by a `]`.

A formula is said well-matched when the following conditions are met:

1. Every bracket has a corresponding pair. `(` corresponds to `)`, `[` corresponds to `]`, et cetera.
2. Every bracket pair is opened first, and closed later.
3. No two pairs "*cross*" each other. For example, `[(])` is not well-matched.

Write a program to help Best White by checking if each of his formulas is well-matched. To make the problem easier, everything other than brackets are removed from the formulas.



#### 입력

The first line of the input will contain the number of test cases C (1≤C≤100). Each test is given in a single line as a character string. The strings will only include characters in "`[](){}`" (quotes for clarity). The length of the string will not exceed 10,000



#### 출력

For each test case, print a single line "`YES`" when the formula is well-matched; print "`NO`" otherwise. (quotes for clarity)



#### 예제 입력

```
3
()()
({[}])
({}[(){}])
```



#### 예제 출력

```
YES
NO
YES
```

