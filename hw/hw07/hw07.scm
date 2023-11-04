;cdr就是取除了第一个元素的其它的元素集合
;car就是取第一个元素
(define (cddr s) (cdr (cdr s)))
    
(define (cadr s) 
   (car (cdr s))
)

(define (caddr s) 
    (car (cdr (cdr (s))))
)

(define (ascending? asc-lst) 
    (cond 
        ((null? (cdr asc-lst)) #t)
        ((< (cadr asc-lst) (car asc-lst)) #f)
        (else (< (car asc-lst) (cadr asc-lst)) (ascending? (cdr asc-lst)))
    )  
)

(define (square n) (* n n))

(define (pow base exp) 
    (cond
        ((= base 1) 1)
        ((= exp 1) base)
        ((even? exp) (square (pow base (/ exp 2))))
        (else (* base (pow base (- exp 1))))
    
    )
)
