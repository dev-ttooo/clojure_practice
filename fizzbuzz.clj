(defn fizzbuzz []
 (for [i (range 1 30)]
   (if (= (rem i 3) 0)
     (if (= (rem i 5) 0)
       (println "fizzbuzz")
       (println "fizz"))
     (if (= (rem i 5) 0)
       (println "buzz")
     )
   )
 )
)
