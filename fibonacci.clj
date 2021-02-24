(defn fib [n]
    (if (= n 0) 0
      (if (= n 1) 1
        (+ (fib (- n 2)) (fib (- n 1))))))
  
  (defn fibs [n]
    (loop [result [], count 0]
      (if (> count n)
        result
        (recur (conj result (fib count)) (+ count 1)))))
