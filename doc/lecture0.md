[home](http://tiny.cc/plm18) |
[copyright](https://github.com/txt/plm18/blob/master/LICENSE.md) &copy;2018, tim&commat;menzies.us
<br>
[<img width=900 src="https://raw.githubusercontent.com/txt/plm18/master/img/banner.png">](http://tiny.cc/plm18)<br>
[syllabus](https://github.com/txt/plm18/blob/master/doc/syllabus.md) |
[src](https://github.com/txt/plm18/tree/master/src) |
[submit](http://tiny.cc/plm18give) |
[chat](https://plm18.slack.com/)


______



# Hello!

<img src="https://camo.githubusercontent.com/d4ce92ae049bf5989da6016967a372f3e0670636/687474703a2f2f736531362e756e626f782e6f72672f2e776f726b736974652f696d672f656c6561726e696e675f696d616765312e6a7067" align=right width=400>

Y'all yearning to be learning? Me too!

Education is the not the filling of a pail, but the lighting of a fire.    
-- W.Yeats

If the world merely lived up to our wildest dreamings, what a dull place it would be. Happily...    
-- Me

Learn why the world wags and what wags it. That is the only thing which the mind can never exhaust, never alienate, never be tortured by, never fear or distrust, and never dream of regretting. Learning is the only thing for you. Look what a lot of things there are to learn.    
-- T.H. White (The Once and Future King)


## Q: Which language is best?

A: none of them.

<img width=900 src="../img/tiobe.png">

And the language you use next is probably not the one you are using now:

- Empirical Analysis of Programming Language Adoption Leo A. Meyerovich, Ariel Rabkin, OOPSLA '13.

<img width=700 src="../img/nextLanguage.png">

## So Many Languages

<a href="http://unbox.org/doc/Seven%20Languages%20in%20Seven%20Weeks%20A%20Pragmatic%20Guide%20to%20Learning%20Programming%20Languages.pdf"><img src="https://imagery.pragprog.com/products/195/btlang.jpg?1298589937" width=350></a><a 
href="http://unbox.org/doc/Seven%20More%20Languages%20in%20Seven%20Weeks.pdf"><img width=350 src="https://imagery.pragprog.com/products/410/7lang.jpg?1414690061"></a><br>

If you want to see your favorite 10 lines of code presented in hundreds of different languages:

- [Rosetta Code](http://rosettacode.org/wiki/Category:Programming_Tasks)

Some languages are very silly:

- [Brainf\*ck](https://en.wikipedia.org/wiki/Brainfuck)
- [Whitespace](https://goo.gl/6rmC5);
   e.g. print "hello world" in Whitespace:

<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Whitespace_in_vim2.png">


Some build for very general tasks (e.g. defining an object-oriented language)

[![](http://ecx.images-amazon.com/images/I/61PruSolX%2BL.jpg)](https://pdfs.semanticscholar.org/a679/e05cae9dd36c0d89a5bb27a8e91aac6690f0.pdf)

```lisp
(defclass circle ()
  ((radius :initarg :radius
           :initform 1.0
           :type number
           :reader radius)))
 
(defmethod area ((shape circle))
  (* pi (expt (radius shape) 2)))
 
> (defvar *c* (make-instance 'circle :radius 2))
> (area *c*)
12.566370614359172d0
```

(BTW, CLOS is v.cool. Dispatching on type of all parameters!)

```lisp
 (defmethod collide-with ((x asteroid) (y asteroid))
   ;; deal with asteroid hitting asteroid
   )
 (defmethod collide-with ((x asteroid) (y spaceship))
   ;; deal with asteroid hitting spaceship
   )
 (defmethod collide-with ((x spaceship) (y asteroid))
   ;; deal with spaceship hitting asteroid
   )
 (defmethod collide-with ((x spaceship) (y spaceship))
   ;; deal with spaceship hitting spaceship
   )
```
Many of which tuned to very specific tasks

- See [19. Examples of Domain Specific Languages](https://tomassetti.me/domain-specific-languages/)

## What Matters Most? Languages? or Community?

The [Hersleb hypothesis](https://www.youtube.com/watch?v=v0CSnYvd0C4)  hypothesis starts at 29:45:

- If Developer X and Y..
- ... work on parts A and B in the code ...
- ... and if A interacts with B ..
- ... and if X and Y don't
- ... the expect bugs!

So maybe we should assess languages by the devoition they inspire?

<img
src="../img/pack4.png" width=300><img
src="../img/pack5.png" width=300><img
src="../img/pack6.png" width=300><img
src="../img/pack3.png" width=300>

