(ns matrix)

(defn valid-matrix? [matrix]
  ; Each row must have the same number of elements
  (if-not (or (nil? matrix) (empty? matrix))
    (apply = (map count matrix))
    false))

(defn cols [matrix]
  (count (first matrix)))

(defn rows [matrix]
  (count matrix))

(defn square? [matrix]
  (= (rows matrix) (cols matrix)))

(defn matrix-print [matrix]
  (loop [matrix' matrix]
    (when-not (empty? matrix')
      (let [row (reduce #(str %1 %2) (interpose " " (first matrix')))]
        (println row))
      (recur (rest matrix')))))

(defn matrix-add [matrix-a matrix-b]
  (loop [matrix-a' matrix-a
         matrix-b' matrix-b]
    (when-not (or (empty? matrix-a') (empty? matrix-b'))
      (let [rows-to-add (first (map vector matrix-a' matrix-b'))
            addition-pairs (apply map vector rows-to-add)]
        (println (map (partial reduce +) addition-pairs)))
      (recur (rest matrix-a') (rest matrix-b')))))

(let [matrix-a [[1 5 4] [5 8 1] [1 8 9]]
      matrix-b [[3 5 1] [8 1 0] [2 8 5]]]
  (println (matrix-add matrix-a matrix-b)))
