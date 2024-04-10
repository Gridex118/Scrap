(ns add-col)

(defn add-collections [col1 col2]
  (let [addition-pairs (map vector col1 col2)]
    (map (partial reduce +) addition-pairs)))

(let [col1 [2 5 1]
      col2 [5 3 1]]
  (println (add-collections col1 col2)))
