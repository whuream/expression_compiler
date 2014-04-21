#Expression Compiler

计算表达式的编译器。

##Introdution

一个简单的计算表表达式的编译器，目前是根据输入输出四元组。

例如： `log(log(-1234,sin4+5*-8*(8)),asinatanacos(3^6))` 的输出结果是:

	- 1234 None id1
	* 8 8 id2
	- id2 None id3
	* 5 id3 id4
	+ 4 id4 id5
	sin id5 None id6
	log id1 id6 id7
	^ 3 6 id8
	acos id8 None id9
	atan id9 None id10
	asin id10 None id11
	log id7 id11 id12
	None id12 None id13

##支持符号

*   ###运算符
	*   ####前置一元运算符 `f1` (f1<参数>)
		*   正弦 `sin`
		*   余弦 `cos`
		*   正切 `tan`
		*   反正弦 `asin`
		*   反余弦 `acos`
		*   反正切 `atan`
		*   自然对数 `ln`
		*   常用对数 `lg`
		*   取反 `-`
	*   ####前置二元运算符 `f2` (f2(<参数1>，<参数2>))
		*   对数 `log`
	*   ####中置二元运算符 `m2` (<参数1>m2<参数2>)
		*   加法 `+`
		*   减法 `-`
		*   乘法 `*`
		*   除法 `/`
		*   乘方 `^`
*   ###数字
	*   整数(由数字组成)
	*   e
	*   PI
*   ###其他符号
	*   左括号 `<`
	*   右括号 `>`
	*   逗号 `,`
*   ###注意: 由于支持符号中不包含空格` `，所以切勿在表达式中加入空格。

## 使用方法

1.  执行 `cd expression_compiler/lexical_analysis`
1.  执行 `make`
1.  执行 `cd ..`
1.  执行 `main.py <inputfile> [outputfile]`