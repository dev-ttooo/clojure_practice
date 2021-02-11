(defn prime [x]
    (not-any? zero?
            (map #(rem x %) ;remで余りを求める
                (range 2 (inc (/ x 2))))))

(defn prime-numbers
    []
    (filter prime (drop 2 (range))))
